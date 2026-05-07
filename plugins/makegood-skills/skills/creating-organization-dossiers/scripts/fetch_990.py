#!/usr/bin/env python3
"""
IRS 990 fetcher and parser for organizational dossiers.

Retrieves nonprofit tax filings from ProPublica Nonprofit Explorer API
and extracts key financial data.

Usage:
    python fetch_990.py "Organization Name" [--ein 12-3456789] [--output ./output]
    python fetch_990.py --ein 12-3456789 --output ./output

Requirements:
    pip install requests
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

try:
    import requests
except ImportError:
    print("Missing dependency. Install with:")
    print("  pip install requests")
    sys.exit(1)


# ProPublica Nonprofit Explorer API
PROPUBLICA_SEARCH = "https://projects.propublica.org/nonprofits/api/v2/search.json"
PROPUBLICA_ORG = "https://projects.propublica.org/nonprofits/api/v2/organizations/{ein}.json"


def clean_ein(ein) -> str:
    """Remove dashes and spaces from EIN. Handles both string and int inputs."""
    return re.sub(r"[^\d]", "", str(ein))


def search_organization(name: str) -> List[Dict]:
    """Search for organizations by name via ProPublica."""
    print(f"Searching for '{name}'...")

    try:
        response = requests.get(
            PROPUBLICA_SEARCH,
            params={"q": name},
            timeout=30
        )
        response.raise_for_status()
        data = response.json()

        organizations = data.get("organizations", [])
        print(f"Found {len(organizations)} matching organization(s)")

        return organizations

    except requests.RequestException as e:
        print(f"Error searching: {e}")
        return []


def get_organization_filings(ein: str) -> Optional[dict]:
    """Get organization details and filings from ProPublica."""
    ein = clean_ein(ein)
    print(f"Fetching filings for EIN {ein}...")

    try:
        response = requests.get(
            PROPUBLICA_ORG.format(ein=ein),
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Organization with EIN {ein} not found")
        else:
            print(f"Error fetching organization: {e}")
        return None
    except requests.RequestException as e:
        print(f"Error fetching organization: {e}")
        return None


def extract_990_data(org_data: dict) -> dict:
    """Extract key financial data from 990 filings."""
    result = {
        "organization": {
            "name": org_data.get("organization", {}).get("name", "Unknown"),
            "ein": org_data.get("organization", {}).get("ein", ""),
            "city": org_data.get("organization", {}).get("city", ""),
            "state": org_data.get("organization", {}).get("state", ""),
            "ntee_code": org_data.get("organization", {}).get("ntee_code", ""),
            "subsection_code": org_data.get("organization", {}).get("subsection_code", ""),
        },
        "filings": [],
        "summary": {},
    }

    filings = org_data.get("filings_with_data", [])

    if not filings:
        print("No filings with data found")
        return result

    for filing in filings[:5]:  # Get last 5 years
        filing_data = {
            "tax_period": filing.get("tax_prd_yr", ""),
            "form_type": filing.get("formtype", "990"),
            "pdf_url": filing.get("pdf_url", ""),
            "financials": {},
        }

        # Extract key financial fields
        financial_fields = {
            "total_revenue": "totrevenue",
            "total_expenses": "totfuncexpns",
            "net_assets": "totnetassetend",
            "contributions": "totcntrbgfts",
            "program_services_revenue": "totprgmrevnue",
            "investment_income": "invstmntinc",
            "other_revenue": "othrevenue",
            "salaries": "compnsatncurrofcr",
            "total_salaries": "payaborexpns" ,
            "employee_count": "noemploy",
            "volunteer_count": "totvoluntrs",
        }

        for key, api_key in financial_fields.items():
            value = filing.get(api_key)
            if value is not None:
                filing_data["financials"][key] = value

        result["filings"].append(filing_data)

    # Calculate summary from most recent filing
    if result["filings"]:
        latest = result["filings"][0]["financials"]
        result["summary"] = {
            "latest_year": result["filings"][0]["tax_period"],
            "total_revenue": latest.get("total_revenue"),
            "total_expenses": latest.get("total_expenses"),
            "net_assets": latest.get("net_assets"),
            "employee_count": latest.get("employee_count"),
        }

        # Calculate revenue trend if multiple years
        if len(result["filings"]) > 1:
            revenues = [f["financials"].get("total_revenue", 0)
                       for f in result["filings"] if f["financials"].get("total_revenue")]
            if len(revenues) >= 2:
                if revenues[-1] > 0:
                    growth = ((revenues[0] - revenues[-1]) / revenues[-1]) * 100
                    result["summary"]["revenue_growth_pct"] = round(growth, 1)

    return result


def format_currency(value: Optional[int]) -> str:
    """Format number as currency."""
    if value is None:
        return "N/A"
    return f"${value:,.0f}"


def generate_markdown(data: dict) -> str:
    """Generate markdown summary of 990 data."""
    org = data["organization"]
    summary = data.get("summary", {})
    filings = data.get("filings", [])

    md = f"""# IRS 990 Data: {org['name']}

**EIN:** {org['ein']}
**Location:** {org['city']}, {org['state']}
**NTEE Code:** {org['ntee_code'] or 'N/A'}

## Financial Summary ({summary.get('latest_year', 'N/A')})

| Metric | Value |
|--------|-------|
| Total Revenue | {format_currency(summary.get('total_revenue'))} |
| Total Expenses | {format_currency(summary.get('total_expenses'))} |
| Net Assets | {format_currency(summary.get('net_assets'))} |
| Employees | {summary.get('employee_count', 'N/A')} |
"""

    if summary.get("revenue_growth_pct") is not None:
        md += f"| Revenue Growth (multi-year) | {summary['revenue_growth_pct']:+.1f}% |\n"

    md += "\n## Filing History\n\n"

    for filing in filings:
        year = filing["tax_period"]
        form = filing["form_type"]
        fin = filing["financials"]

        md += f"### {year} ({form})\n\n"

        if filing.get("pdf_url"):
            md += f"[View PDF]({filing['pdf_url']})\n\n"

        md += "| Category | Amount |\n|----------|--------|\n"

        if fin.get("contributions"):
            md += f"| Contributions/Grants | {format_currency(fin['contributions'])} |\n"
        if fin.get("program_services_revenue"):
            md += f"| Program Service Revenue | {format_currency(fin['program_services_revenue'])} |\n"
        if fin.get("investment_income"):
            md += f"| Investment Income | {format_currency(fin['investment_income'])} |\n"
        if fin.get("total_revenue"):
            md += f"| **Total Revenue** | **{format_currency(fin['total_revenue'])}** |\n"
        if fin.get("total_expenses"):
            md += f"| **Total Expenses** | **{format_currency(fin['total_expenses'])}** |\n"
        if fin.get("net_assets"):
            md += f"| Net Assets (EOY) | {format_currency(fin['net_assets'])} |\n"

        md += "\n"

    md += """## Data Source

Data from [ProPublica Nonprofit Explorer](https://projects.propublica.org/nonprofits/).
ProPublica sources data from IRS e-filed 990s.

*Note: This data may not reflect the most recent filing if the organization
hasn't e-filed recently. Always verify with the organization directly for
current information.*
"""

    return md


def main():
    parser = argparse.ArgumentParser(
        description="Fetch and parse IRS 990 data for nonprofit organizations"
    )
    parser.add_argument(
        "name",
        nargs="?",
        help="Organization name to search for"
    )
    parser.add_argument(
        "--ein",
        help="Specific EIN to look up (format: 12-3456789 or 123456789)"
    )
    parser.add_argument(
        "--output", "-o",
        default="./990_data",
        help="Output directory (default: ./990_data)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Also output raw JSON data"
    )

    args = parser.parse_args()

    if not args.name and not args.ein:
        parser.print_help()
        print("\nError: Provide either organization name or --ein")
        sys.exit(1)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # If we have an EIN, use it directly
    if args.ein:
        org_data = get_organization_filings(args.ein)
        if not org_data:
            print("Could not fetch organization data")
            sys.exit(1)

    # Otherwise search by name
    else:
        results = search_organization(args.name)

        if not results:
            print("No organizations found. Try:")
            print("  - Using the exact legal name")
            print("  - Providing the EIN with --ein")
            sys.exit(1)

        # Show results and let user choose if multiple
        print("\nMatching organizations:")
        for i, org in enumerate(results[:10], 1):
            print(f"  {i}. {org['name']}")
            print(f"     EIN: {org['ein']} | {org.get('city', '')}, {org.get('state', '')}")
            print(f"     Score: {org.get('score', 0):.2f}")

        if len(results) == 1:
            selected = results[0]
        else:
            print(f"\nUsing top result: {results[0]['name']}")
            print("To use a different result, run again with --ein")
            selected = results[0]

        org_data = get_organization_filings(selected["ein"])
        if not org_data:
            print("Could not fetch organization filings")
            sys.exit(1)

    # Extract and format data
    extracted = extract_990_data(org_data)
    markdown = generate_markdown(extracted)

    # Save outputs
    org_name_safe = re.sub(r"[^\w\s-]", "", extracted["organization"]["name"])
    org_name_safe = re.sub(r"\s+", "-", org_name_safe).lower()[:50]

    md_path = output_dir / f"{org_name_safe}-990.md"
    with open(md_path, "w") as f:
        f.write(markdown)
    print(f"\nSaved: {md_path}")

    if args.json:
        json_path = output_dir / f"{org_name_safe}-990.json"
        with open(json_path, "w") as f:
            json.dump(extracted, f, indent=2)
        print(f"Saved: {json_path}")

    print(f"\n990 data extraction complete!")


if __name__ == "__main__":
    main()
