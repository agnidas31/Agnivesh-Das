"""
Website-only content for agnidas31's portfolio. Everything shared with the résumé
(profile, summary, signature metrics, capabilities, experience, education) lives in
content.py, so both always say the same thing.

To add a project: write its case study (see PORTFOLIO.md), add an entry to PROJECTS,
then run `python3 build.py all`.
"""

SITE = {
    # Change to the custom domain (e.g. "https://agniveshdas.com") once DNS is set up,
    # and add a CNAME file at the repo root containing just the bare domain.
    "base_url": "https://agnidas31.github.io/Agnivesh-Das/",
    "custom_domain": "",
    "github_user": "agnidas31",
    "resume_file": "Agnivesh_Das_Resume.pdf",
    "linkedin_url": "https://www.linkedin.com/in/agnivesh-das/",
    "hero_title": "Data Analytics & AI Leader",
    "hero_line": "I turn fragmented enterprise data into decisions leaders trust, and build the AI that puts "
                 "those answers in their hands.",
}

# Each project lives in its own GitHub repo (Victor's pattern). `repo` is the exact repo name;
# its page is published at https://<github_user>.github.io/<repo>/.
# `story` / `technical` are the Markdown files inside that repo that build.py turns into pages.
PROJECTS = [
    {
        "repo": "Single-Customer-Identifier-BP",
        "title": "Single Customer Identifier",
        "company": "BP",
        "metric": "38%",
        "metric_label": "fuel-to-store conversion",
        "summary": "Linking till, loyalty and card-payment records into one view of each customer, with "
                   "confidence-scored matching built for data that never shared a key.",
        "tags": ["Customer 360", "Identity resolution", "SQL"],
        "story": "single-customer-identifier.md",
        "technical": "sci-matching-models.md",
        "status": "live",
    },
    {
        "repo": "Customer-Lifetime-Value-BP",
        "title": "Customer Lifetime Value",
        "company": "BP",
        "metric": "4×",
        "metric_label": "average customer spend",
        "summary": "Turning a unified customer view into a forward-looking value for every customer, using "
                   "survival models and discounted future margin.",
        "tags": ["Survival analysis", "Customer value", "Marketing"],
        "story": "customer-lifetime-value.md",
        "technical": "clv-calculation-method.md",
        "status": "live",
    },
    {
        "repo": "Global-Fleet-BP",
        "title": "Global Fleet KPI Report",
        "company": "BP",
        "metric": "3 → 1",
        "metric_label": "regions on one view",
        "summary": "Three regions measuring the same fleet business three different ways, brought into one "
                   "trusted, comparable report.",
        "tags": ["KPI design", "Data governance", "Power BI"],
        "story": "global-fleet-kpi.md",
        "technical": None,
        "status": "live",
    },
    {
        "repo": "Inventory-Over-Short-BP",
        "title": "Inventory Over & Short",
        "company": "BP",
        "metric": "22%",
        "metric_label": "better inventory recovery",
        "summary": "Store audits turned into a ranked view of where stock is being lost, how fast, and which "
                   "stores need attention first.",
        "tags": ["Shrink", "Loss prevention", "Power BI"],
        "story": "inventory-over-short.md",
        "technical": None,
        "status": "live",
    },
    {
        "repo": "Fuel-Margin-Waterfall-BP",
        "title": "Fuel Margin Waterfall",
        "company": "BP",
        "metric": "2×",
        "metric_label": "faster root-cause analysis",
        "summary": "One cents-per-gallon margin number broken into the drivers behind it, so pricing and "
                   "supply teams can see why margin moved.",
        "tags": ["Pricing analytics", "Fuel retail", "Tableau"],
        "story": "fuel-margin-waterfall.md",
        "technical": None,
        "status": "live",
    },
    # Walmart case studies: repos exist, content pending source material from Agnivesh.
    # Set status to "live" (and fill the fields) once each write-up is approved for publishing.
    {"repo": "AIsleOne-Walmart", "title": "AISLE1", "company": "Walmart", "status": "pending"},
    {"repo": "Smart-Woofie-Walmart", "title": "Smart Woofie", "company": "Walmart", "status": "pending"},
    {"repo": "Call-Complexity-Walmart", "title": "Call Complexity", "company": "Walmart", "status": "pending"},
    {"repo": "Call-Complexity-vs-SSR-Walmart", "title": "Call Complexity vs. Self-Serve Rate",
     "company": "Walmart", "status": "pending"},
]
