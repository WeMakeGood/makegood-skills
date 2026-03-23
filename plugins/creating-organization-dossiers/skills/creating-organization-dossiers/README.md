# Creating Organization Dossiers

A skill for Claude that creates comprehensive organizational profiles through systematic research.

## What It Does

This skill guides Claude through a 6-phase workflow to research an organization and produce a structured dossier covering:

- Executive Summary
- Organizational Overview (mission, vision, values, history)
- Programs & Services
- Leadership & Governance
- Financial Profile (from IRS 990 data for nonprofits)
- Partnerships & Collaborations
- Digital Presence
- Strategic Analysis (when requester context is available)
- Information Gaps & Next Steps

## When to Use It

**Trigger phrases that work well:**

- "Create a dossier on [Organization Name]"
- "I need prospect research on [Organization]"
- "Run a due diligence report on [Organization]"
- "Generate an organization report on [Organization]"
- "Build an org profile for [Organization]"

**Use cases:**

- Prospect research before client outreach
- Due diligence for partnerships or grants
- Client onboarding background research
- Preparing for meetings with new organizations
- Evaluating potential grantees or partners

## How It Works

The skill auto-adapts to available tools:

### web_search + web_fetch (preferred)

When web_search and web_fetch tools are available (Claude API, Claude AI, or Claude Code), the skill uses them directly to collect website content and 990 data. This produces cleaner results and works in sandboxed environments without internet access from code execution.

- **Website content:** Fetches homepage, discovers internal pages, fetches key sections (About, Team, Programs, etc.)
- **990 data:** Queries the ProPublica Nonprofit Explorer API via web_fetch, or searches for ProPublica pages via web_search

### Python scripts (bash environments)

When bash is available and web_search/web_fetch are not, the skill falls back to bundled Python scripts:

1. **Website Scraper** (`scripts/scrape_website.py`)
   - Discovers pages via sitemap.xml or navigation crawling
   - Extracts content from About, Team, Board, Programs, Impact pages
   - Outputs markdown files for each category

2. **990 Fetcher** (`scripts/fetch_990.py`)
   - Searches ProPublica Nonprofit Explorer API
   - Retrieves 5 years of financial data
   - Outputs formatted markdown with revenue, expenses, assets

If scripts fail (no internet, missing packages), the skill switches to web_search/web_fetch automatically.

## Outputs

By default, the skill returns the dossier inline in the conversation. You can change this with a keyword in your request:

| Request | Output |
|---------|--------|
| "Create a dossier on Acme Corp" | Returns dossier inline |
| "Create a dossier on Acme Corp **as a file**" | Writes `acme-corp-dossier.md` to disk |
| "Create a dossier on Acme Corp **as an artifact**" | Creates a Claude artifact |

When outputting as a file or artifact, the skill shows progress checkpoints as it works. When outputting inline, it runs silently and returns only the final dossier.

- **Source files:** `tmp/[org-name]/` - raw scraped content and 990 data (in Claude Code)

## Script Dependencies

Only needed if using the Python scripts (bash environments without web_search/web_fetch):

```bash
pip install requests beautifulsoup4 html2text lxml
```

## Example

**Input:**
```
Create a dossier on Community Foundation of Greater Memphis
Website: https://cfgm.org
Purpose: Evaluating as potential funder
```

**Output:** A 200-400 line markdown dossier with:
- Financial trends from 990 filings
- Board composition and leadership bios
- Program areas and grantmaking focus
- Strategic fit analysis based on your stated purpose

## Tips for Best Results

1. **Provide the website URL** - helps the scraper find the right pages
2. **State your purpose** - enables relevant strategic analysis
3. **Mention if it's a nonprofit** - triggers 990 data lookup
4. **Provide EIN if known** - more reliable 990 retrieval

## Limitations

- 990 data lags 1-2 years behind current (IRS filing delays)
- Website scraping depends on site structure and accessibility
- Private companies have limited public financial data
- Some organizations don't e-file 990s (paper filers not in ProPublica)

## File Structure

```
creating-organization-dossiers/
├── SKILL.md                 # Main skill instructions
├── README.md                # This file
├── references/
│   ├── DOSSIER-TEMPLATE.md  # Output template structure
│   └── DATA-SOURCES.md      # Additional research sources
└── scripts/
    ├── scrape_website.py    # Website content extraction
    └── fetch_990.py         # IRS 990 data retrieval
```
