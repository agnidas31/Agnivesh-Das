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

# "Ways I work" lenses: tabbed section on the hub. Each item is a short, confirmed anecdote.
LENSES = [
    {
        "id": "lead",
        "title": "Leadership & Strategy",
        "blurb": "Setting the analytics agenda, building teams, and turning results into decisions leaders act on.",
        "items": [
            ("Four pillars, one agenda",
             "Leads a team of 8+ across Operations, Workforce Management, CRM and Self-Serve AI for Walmart "
             "Customer Engagement Services."),
            ("From pilot to realized savings",
             "Championed Agent Assist voice and chat AI across CRM: $17M in savings and a 23% cut in average "
             "handle time, measured all the way through."),
            ("Insights that reached strategy",
             "Appeasement work lifted utilization from 45% to 71%, and the findings helped shape Walmart+ "
             "adoption strategy."),
            ("Adoption is part of the job",
             "At Nike, trained 30+ colleagues on new Tableau dashboards and lifted utilization 40%."),
        ],
    },
    {
        "id": "ai",
        "title": "AI & Customer Analytics",
        "blurb": "Applying AI and customer analytics to questions the business actually asks.",
        "items": [
            ("AISLE1",
             "An agentic AI insights product on Claude and BigQuery; VPs and senior directors query certified "
             "metrics in plain English instead of raising ad hoc requests."),
            ("Measuring an AI voice assistant",
             "Built the measurement framework for Sierra as self-serve rose from 25% to 62%, with CSAT "
             "improving alongside."),
            ("One view of the customer",
             "Led BP's Single Customer Identifier, linking till, loyalty and card data; fuel-to-store "
             "conversion rose 38%."),
            ("What a customer is worth",
             "Customer Lifetime Value on top of SCI: a 4× increase in average customer spend and $8M in "
             "marketing savings."),
        ],
    },
    {
        "id": "data",
        "title": "Data Foundations & Engineering",
        "blurb": "The pipelines, models and governed metrics that everything else stands on.",
        "items": [
            ("Matching data that never shared a key",
             "Designed SCI's deterministic and probabilistic matching: exact keys, then confidence-scored "
             "candidates within time and value tolerances."),
            ("Three regions, one KPI view",
             "Unified fleet KPIs across ESA, ANZ and the US: report prep cut 85%, decisions 3× faster."),
            ("Finding where stock goes missing",
             "Ranked stores by audit loss across Thorntons and ampm: priority stores found 4× faster, "
             "inventory recovery up 22%."),
            ("Legacy BI, modernized",
             "Moved Nike's supply chain planning reporting from Cognos to Tableau on Teradata, automating ETL "
             "across billions of rows."),
        ],
    },
]
