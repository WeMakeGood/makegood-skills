# Planning Social Campaigns

Plans social media campaigns from source content, producing individually filed assets ready for production.

## When to Use

Use this skill when you need to:
- Plan a multi-channel social media campaign from a brief, announcement, or content source
- Generate a campaign calendar with asset IDs and publish dates
- Produce per-asset content files structured for each channel (email, Instagram, YouTube, etc.)
- Create an engagement/activation plan for a campaign

## How to Invoke

Say things like:
- "Plan a social media campaign for our product launch"
- "Create a social campaign from this announcement"
- "Build campaign assets for our fundraising event"
- "I need a content calendar and assets for this campaign"

## What You'll Need

- Source content to campaign about (article, announcement, brief, event details, etc.)
- Campaign goals (what the campaign should accomplish)
- Target audience(s)
- Active channels and any channel constraints
- Campaign dates (start, end, any fixed milestones)
- Brand voice guidelines or context library (optional)

## What You'll Get

1. **Campaign Strategy** (`strategy.md`) — Goals, audience, strategic approach, channel strategy, campaign segments
2. **Campaign Calendar** (`calendar.md` or `.csv`) — Asset manifest with IDs, channels, types, dates
3. **Per-Asset Files** (`assets/[ID].md`) — One markdown file per asset with channel-specific content and metadata
4. **Engagement Plan** (`engagement-plan.md`, optional) — Team activation, response guidelines, success metrics
5. **Verification Report** (`verification.md`) — Cross-reference confirming all calendar assets were created correctly

## Example

**Input:** A product launch brief, targeting Instagram, Email, and LinkedIn over 3 weeks

**Output:**
```
summer-product-launch/
├── strategy.md
├── calendar.md
├── assets/
│   ├── SPL-IG-001.md
│   ├── SPL-IGC-001.md
│   ├── SPL-EM-001.md
│   ├── SPL-EM-002.md
│   ├── SPL-LI-001.md
│   └── ...
├── engagement-plan.md
└── verification.md
```

## Tips

- Provide as much source content as possible upfront — the skill flags gaps rather than inventing content
- The skill will ask you to confirm the strategy and calendar before building assets, so you can adjust course early
- If you use Teamwork for project management, the skill can hand off to the `generating-teamwork-imports` skill after verification
- Asset IDs follow the format `CAMPAIGN_CODE-CHANNEL-###` — bring your own code or let the skill derive one
