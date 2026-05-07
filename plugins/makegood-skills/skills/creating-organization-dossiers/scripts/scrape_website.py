#!/usr/bin/env python3
"""
Website scraper for organizational dossiers.

Discovers and extracts content from key organizational pages like About, Team,
Board, Mission, Programs, etc. Uses sitemap.xml when available for reliable
page discovery.

Usage:
    python scrape_website.py https://example.org [--output ./output]

Requirements:
    pip install requests beautifulsoup4 html2text lxml
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    import html2text
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install requests beautifulsoup4 html2text lxml")
    sys.exit(1)


# Keywords to identify relevant organizational pages
# Format: category -> list of path patterns to match
# Patterns are matched against URL path segments, not substrings
PAGE_KEYWORDS = {
    "about": ["about", "about-us", "who-we-are", "our-story", "overview"],
    "mission": ["mission", "vision", "values", "purpose"],
    "team": ["team", "staff", "leadership", "our-team", "our-people"],
    "board": ["board", "directors", "trustees", "governance", "board-of-directors"],
    "programs": ["programs", "services", "what-we-do", "our-work", "initiatives"],
    "impact": ["impact", "outcomes", "results", "success-stories", "annual-report"],
    "partners": ["partners", "partnerships", "supporters", "funders", "sponsors"],
    "history": ["history", "timeline", "milestones", "our-history"],
    "contact": ["contact", "contact-us", "get-in-touch", "locations"],
    "careers": ["careers", "jobs", "work-with-us", "join-us"],
    "news": ["news", "blog", "press", "media", "announcements"],
}

# URL patterns to exclude (these are typically not organizational info pages)
EXCLUDE_PATTERNS = [
    r"/partners/[^/]+",      # Individual partner profile pages (e.g., /partners/company-name/)
    r"/blog/\d{4}/",         # Individual blog posts by date
    r"/news/\d{4}/",         # Individual news posts by date
    r"/\d{4}/\d{2}/\d{2}/",  # Date-based URLs (blog/news posts)
    r"/author/",             # Author pages
    r"/tag/",                # Tag archives
    r"/category/",           # Category archives
    r"/page/\d+",            # Pagination
    r"/dashboard",           # User dashboards
    r"/login",               # Login pages
    r"/register",            # Registration pages
    r"/cart",                # Shopping cart
    r"/checkout",            # Checkout
]

# Common navigation elements to look for links
NAV_SELECTORS = [
    "nav",
    "header nav",
    "[role='navigation']",
    ".nav",
    ".navigation",
    ".menu",
    ".main-menu",
    "#menu",
    "#nav",
    "footer nav",
    "footer",
]


def normalize_url(base_url: str, href: str) -> Optional[str]:
    """Convert relative URLs to absolute and validate."""
    if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
        return None

    absolute = urljoin(base_url, href)
    parsed = urlparse(absolute)
    base_parsed = urlparse(base_url)

    # Only follow links on same domain
    if parsed.netloc != base_parsed.netloc:
        return None

    return absolute


def is_excluded_url(url: str) -> bool:
    """Check if URL matches any exclusion pattern."""
    path = urlparse(url).path.lower()
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, path):
            return True
    return False


def categorize_url(url: str) -> Optional[str]:
    """Determine which category a URL belongs to based on path segments."""
    # First check exclusions
    if is_excluded_url(url):
        return None

    path = urlparse(url).path.lower()
    # Split path into segments for more precise matching
    segments = [s for s in path.split("/") if s]

    for category, keywords in PAGE_KEYWORDS.items():
        for keyword in keywords:
            # Match if keyword is a complete path segment or the path starts with it
            # This prevents "mission" from matching "/partners/some-mission-company/"
            if keyword in segments:
                return category
            # Also match if the first or second segment starts with the keyword
            # e.g., /about/team/ should match "about"
            for i, seg in enumerate(segments[:2]):  # Only check first 2 segments
                if seg == keyword or seg.startswith(keyword + "-"):
                    return category

    return None


def fetch_sitemap(base_url: str) -> List[str]:
    """Try to fetch and parse sitemap.xml for URLs."""
    sitemap_urls = []

    # Common sitemap locations
    sitemap_locations = [
        urljoin(base_url, "/sitemap.xml"),
        urljoin(base_url, "/sitemap_index.xml"),
        urljoin(base_url, "/wp-sitemap.xml"),  # WordPress
        urljoin(base_url, "/sitemap/sitemap.xml"),
    ]

    for sitemap_url in sitemap_locations:
        try:
            print(f"Checking for sitemap at {sitemap_url}...")
            response = requests.get(sitemap_url, timeout=15, headers={
                "User-Agent": "Mozilla/5.0 (compatible; DossierBot/1.0; research purposes)"
            })

            if response.status_code != 200:
                continue

            # Check if it's actually XML
            content_type = response.headers.get("content-type", "")
            if "xml" not in content_type and not response.text.strip().startswith("<?xml"):
                continue

            print(f"Found sitemap at {sitemap_url}")

            # Parse XML
            root = ET.fromstring(response.content)

            # Handle namespace
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

            # Check if this is a sitemap index (contains other sitemaps)
            sitemap_refs = root.findall(".//sm:sitemap/sm:loc", ns)
            if sitemap_refs:
                print(f"Found sitemap index with {len(sitemap_refs)} sub-sitemaps")
                for ref in sitemap_refs[:5]:  # Limit to first 5 sub-sitemaps
                    sub_urls = fetch_sitemap_direct(ref.text)
                    sitemap_urls.extend(sub_urls)
            else:
                # Regular sitemap with URLs
                url_elements = root.findall(".//sm:url/sm:loc", ns)
                if not url_elements:
                    # Try without namespace
                    url_elements = root.findall(".//url/loc")

                for url_elem in url_elements:
                    if url_elem.text:
                        sitemap_urls.append(url_elem.text)

            if sitemap_urls:
                print(f"Extracted {len(sitemap_urls)} URLs from sitemap")
                return sitemap_urls

        except (requests.RequestException, ET.ParseError) as e:
            print(f"  Could not parse {sitemap_url}: {e}")
            continue

    return sitemap_urls


def fetch_sitemap_direct(sitemap_url: str) -> List[str]:
    """Fetch URLs from a specific sitemap URL."""
    urls = []
    try:
        response = requests.get(sitemap_url, timeout=15, headers={
            "User-Agent": "Mozilla/5.0 (compatible; DossierBot/1.0; research purposes)"
        })
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            url_elements = root.findall(".//sm:url/sm:loc", ns)
            if not url_elements:
                url_elements = root.findall(".//url/loc")
            for url_elem in url_elements:
                if url_elem.text:
                    urls.append(url_elem.text)
    except Exception:
        pass
    return urls


def discover_pages_from_sitemap(sitemap_urls: List[str]) -> Dict[str, List[str]]:
    """Categorize URLs from sitemap into relevant pages."""
    discovered = {cat: [] for cat in PAGE_KEYWORDS}

    for url in sitemap_urls:
        category = categorize_url(url)
        if category and url not in discovered[category]:
            discovered[category].append(url)

    return discovered


def discover_pages_from_navigation(base_url: str) -> Dict[str, List[str]]:
    """Discover organizational pages by crawling navigation links."""
    discovered = {cat: [] for cat in PAGE_KEYWORDS}
    visited_urls = set()

    print(f"Discovering pages from navigation at {base_url}...")

    try:
        response = requests.get(base_url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (compatible; DossierBot/1.0; research purposes)"
        })
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching homepage: {e}")
        return discovered

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all links in navigation areas first
    nav_links = []
    for selector in NAV_SELECTORS:
        try:
            for nav in soup.select(selector):
                nav_links.extend(nav.find_all("a", href=True))
        except Exception:
            continue

    # Also get all links on the page
    all_links = soup.find_all("a", href=True)

    # Process navigation links first (higher priority)
    for link in nav_links + all_links:
        href = link.get("href", "")
        url = normalize_url(base_url, href)

        if not url or url in visited_urls:
            continue

        visited_urls.add(url)

        # Check URL path for category
        category = categorize_url(url)

        # Also check link text
        if not category:
            link_text = link.get_text().lower().strip()
            for cat, keywords in PAGE_KEYWORDS.items():
                if any(kw in link_text for kw in keywords):
                    category = cat
                    break

        if category and url not in discovered[category]:
            discovered[category].append(url)

    return discovered


def discover_pages(base_url: str) -> Dict[str, List[str]]:
    """Discover organizational pages, trying sitemap first then navigation."""

    # Try sitemap first
    sitemap_urls = fetch_sitemap(base_url)

    if sitemap_urls:
        discovered = discover_pages_from_sitemap(sitemap_urls)
        total = sum(len(urls) for urls in discovered.values())
        if total > 0:
            print(f"Discovered {total} relevant pages from sitemap:")
            for cat, urls in discovered.items():
                if urls:
                    print(f"  {cat}: {len(urls)} page(s)")
            return discovered
        else:
            print("Sitemap found but no relevant pages matched. Falling back to navigation...")
    else:
        print("No sitemap found. Falling back to navigation discovery...")

    # Fall back to navigation discovery
    discovered = discover_pages_from_navigation(base_url)

    # Report findings
    total = sum(len(urls) for urls in discovered.values())
    print(f"Discovered {total} relevant pages from navigation:")
    for cat, urls in discovered.items():
        if urls:
            print(f"  {cat}: {len(urls)} page(s)")

    return discovered


def extract_content(url: str) -> Dict:
    """Extract main content from a page as markdown."""
    result = {
        "url": url,
        "title": "",
        "content": "",
        "error": None,
    }

    try:
        response = requests.get(url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (compatible; DossierBot/1.0; research purposes)"
        })
        response.raise_for_status()
    except requests.RequestException as e:
        result["error"] = str(e)
        return result

    soup = BeautifulSoup(response.text, "html.parser")

    # Get page title
    title_tag = soup.find("title")
    result["title"] = title_tag.get_text().strip() if title_tag else ""

    # Remove unwanted elements
    for selector in ["nav", "header", "footer", "script", "style", "aside", "noscript",
                     ".navigation", ".menu", ".sidebar", ".comments", ".social",
                     "[role='navigation']", "[role='banner']", "[role='contentinfo']"]:
        try:
            for el in soup.select(selector):
                el.decompose()
        except Exception:
            continue

    # Find main content area
    main_content = None
    for selector in ["main", "article", "[role='main']", ".content", "#content",
                     ".main-content", ".entry-content", ".post-content", ".page-content",
                     "#main", "#main-content"]:
        try:
            main_content = soup.select_one(selector)
            if main_content:
                break
        except Exception:
            continue

    if not main_content:
        main_content = soup.body if soup.body else soup

    # Convert to markdown
    h2t = html2text.HTML2Text()
    h2t.ignore_links = False
    h2t.ignore_images = True
    h2t.ignore_emphasis = False
    h2t.body_width = 0  # Don't wrap
    h2t.skip_internal_links = True

    result["content"] = h2t.handle(str(main_content))

    return result


def scrape_organization(base_url: str, output_dir: Path) -> Dict:
    """Main scraping function."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # Discover pages
    pages = discover_pages(base_url)

    results = {
        "base_url": base_url,
        "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "pages": {},
    }

    # Also scrape the homepage
    print(f"Scraping homepage: {base_url}")
    homepage_content = extract_content(base_url)
    results["homepage"] = homepage_content

    # Save homepage
    homepage_path = output_dir / "homepage.md"
    with open(homepage_path, "w") as f:
        f.write(f"# Homepage\n\n")
        f.write(f"*Source: {base_url}*\n\n")
        f.write(f"## {homepage_content['title'] or 'Homepage'}\n\n")
        f.write(homepage_content["content"])
    print(f"Saved: {homepage_path}")

    # Scrape each discovered page
    for category, urls in pages.items():
        if not urls:
            continue

        results["pages"][category] = []

        for url in urls[:3]:  # Limit to 3 pages per category
            print(f"Scraping {category}: {url}")

            content = extract_content(url)
            results["pages"][category].append(content)

            # Be polite
            time.sleep(0.5)

    # Save results
    # JSON manifest
    manifest_path = output_dir / "scrape_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump({
            "base_url": results["base_url"],
            "scraped_at": results["scraped_at"],
            "homepage_title": results.get("homepage", {}).get("title", ""),
            "pages": {cat: [{"url": p["url"], "title": p["title"]}
                          for p in pages_list]
                     for cat, pages_list in results["pages"].items()},
        }, f, indent=2)

    # Individual markdown files per category
    for category, page_results in results["pages"].items():
        if not page_results:
            continue

        md_path = output_dir / f"{category}.md"
        with open(md_path, "w") as f:
            f.write(f"# {category.title().replace('-', ' ')}\n\n")
            f.write(f"*Source: {base_url}*\n\n")

            for page in page_results:
                if page.get("error"):
                    f.write(f"## Error fetching {page['url']}\n\n{page['error']}\n\n")
                else:
                    f.write(f"## {page['title'] or page['url']}\n\n")
                    f.write(f"*URL: {page['url']}*\n\n")
                    f.write(page["content"])
                    f.write("\n\n---\n\n")

        print(f"Saved: {md_path}")

    print(f"\nScraping complete. Results in {output_dir}/")
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Scrape organizational website for dossier content"
    )
    parser.add_argument("url", help="Organization homepage URL")
    parser.add_argument(
        "--output", "-o",
        default="./scraped_content",
        help="Output directory (default: ./scraped_content)"
    )

    args = parser.parse_args()

    # Validate URL
    if not args.url.startswith(("http://", "https://")):
        args.url = "https://" + args.url

    output_dir = Path(args.output)

    try:
        scrape_organization(args.url, output_dir)
    except KeyboardInterrupt:
        print("\nScraping interrupted.")
        sys.exit(1)


if __name__ == "__main__":
    main()
