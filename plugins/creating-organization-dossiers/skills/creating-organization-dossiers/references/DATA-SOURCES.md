# Data Sources for Organizational Research

Additional sources beyond the automated scripts for comprehensive research.

## Primary Sources (Automated)

### Website Content
**Script:** `scripts/scrape_website.py`

Automatically discovers and extracts:
- About/Mission pages
- Team/Leadership
- Board of Directors
- Programs/Services
- Impact/Outcomes
- Partners/Funders

### IRS 990 Data
**Script:** `scripts/fetch_990.py`

Via ProPublica Nonprofit Explorer:
- Tax filings (up to 5 years)
- Revenue breakdown
- Expense categories
- Asset information
- Employee/volunteer counts

## Secondary Sources (Manual)

### Financial & Nonprofit Data

| Source | URL | What It Provides |
|--------|-----|------------------|
| GuideStar/Candid | guidestar.org | Comprehensive nonprofit profiles, 990s, ratings |
| Charity Navigator | charitynavigator.org | Ratings, financial health scores |
| BBB Wise Giving | give.org | Standards compliance, governance info |
| Foundation Directory | foundationdirectory.com | Funder research, grant history |

### News & Media

| Source | Use For |
|--------|---------|
| Google News | Recent coverage, press releases |
| LinkedIn | Staff profiles, company updates |
| Local news archives | Community impact, local presence |
| Trade publications | Sector-specific coverage |

### Government & Public Records

| Source | What It Provides |
|--------|------------------|
| State charity registration | Registration status, annual filings |
| Secretary of State | Corporate filings, registered agent |
| IRS Tax Exempt Organization Search | Tax-exempt status verification |
| SAM.gov | Federal grants, contracts |
| USASpending.gov | Federal funding received |

## Research Strategies

### For Comprehensive Financial Picture

1. Start with 990 data (automated)
2. Check GuideStar for additional context
3. Review annual reports if available
4. Search for news about major grants/donations

### For Leadership Background

1. Extract from website (automated)
2. LinkedIn profiles for detailed backgrounds
3. Board member affiliations
4. Previous positions and organizations

### For Program Effectiveness

1. Website impact pages (automated)
2. Annual reports with outcome data
3. Third-party evaluations if published
4. News coverage of program results

### For Partnership Landscape

1. Website partner pages (automated)
2. 990 Schedule I (grants made)
3. 990 Schedule B (major donors, if disclosed)
4. News about collaborations

## When Automated Sources Fail

### Website Scraping Issues

**Problem:** Site blocks scraping
**Solutions:**
- Ask user to provide specific page URLs
- User manually copies content
- Try accessing via web.archive.org

**Problem:** Content in JavaScript/dynamic pages
**Solutions:**
- Ask user to provide page content directly
- Use browser-based extraction tools

### 990 Data Not Available

**Reasons:**
- Organization doesn't e-file
- Recently formed (no filings yet)
- Not a 501(c)(3)
- Foreign organization

**Alternative approaches:**
- Ask user for annual reports
- Check state charity filings
- Search GuideStar directly
- Review website financial disclosures

## Data Quality Notes

### Website Content
- May be outdated (check for dates)
- Represents organization's self-presentation
- Verify key claims with third-party sources

### 990 Data
- Lags 1-2 years behind current
- Self-reported by organization
- Larger orgs have more detailed filings
- Schedule O contains narrative explanations

### News Coverage
- May reflect point-in-time situations
- Consider source bias
- Cross-reference multiple sources

## Privacy & Ethics

- Only use publicly available information
- Respect robots.txt and terms of service
- Don't access private/password-protected content
- Note data sources in final dossier
- Recommend verification for critical decisions
