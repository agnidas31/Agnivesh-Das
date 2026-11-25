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
    # Headshot: put the image in this repo (e.g. "photo.jpg") and set its file name here.
    # While empty, the hero shows an initials monogram in the photo's place.
    "photo": "",
    "vcard_file": "Agnivesh_Das.vcf",
    "hero_line": "I turn fragmented enterprise data into decisions leaders trust, and build the AI that puts "
                 "those answers in their hands.",
}

# Each project lives in its own GitHub repo (Victor's pattern). `repo` is the exact repo name;
# its page is published at https://<github_user>.github.io/<repo>/.
# `story` / `technical` are the Markdown files inside that repo that build.py turns into pages.
PROJECTS = [
    {
        "repo": "Single-Customer-Identifier-BP",
        "category": "Customer analytics",
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
        "category": "Customer analytics",
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
        "category": "Retail & operations",
        "title": "Global Fleet KPI Report",
        "company": "BP",
        "metric": "3 → 1",
        "metric_label": "regions on one view",
        "summary": "Fragmented operational data from three regions unified into one view, to monitor asset "
                   "utilisation and transportation demand and guide commercial and safety decisions.",
        "tags": ["KPI design", "Data governance", "Power BI"],
        "story": "global-fleet-kpi.md",
        "technical": None,
        "status": "live",
    },
    {
        "repo": "Inventory-Over-Short-BP",
        "category": "Retail & operations",
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
        "category": "Retail & operations",
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
    # Walmart work samples: live, self-contained demos (synthetic data) in their own repos.
    # They have no Markdown case study, so build.py links straight to each repo's own index.html.
    {
        "repo": "AIsleOne-Walmart",
        "category": "Customer care",
        "title": "AISLE One CRM Dashboards",
        "company": "Walmart",
        "metric": "6",
        "metric_label": "dashboards in one suite",
        "summary": "The AISLE One CRM reporting suite as portable demos: AHT savings and deep-dive, Fixit Ops, "
                   "QSR and Spark dashboards, each a self-contained page with synthetic data.",
        "tags": ["Product analytics", "Contact center", "Chart.js"],
        "status": "live", "link_label": "Open the demos",
    },
    {
        "repo": "CRM-Analysis-Walmart",
        "category": "AI & agents",
        "title": "Agent Assist Impact",
        "company": "Walmart",
        "metric": "23%",
        "metric_label": "lower average handle time",
        "summary": "How agents using AI Agent Assist compare with those who don't on handle time, CSAT and "
                   "NPS, by endpoint and over time.",
        "tags": ["Conversational AI", "CRM", "Measurement"],
        "status": "live", "link_label": "Open the demo",
    },
    {
        "repo": "Smart-Woofie-Walmart",
        "category": "AI & agents",
        "title": "Smart Woffie",
        "company": "Walmart",
        "metric": "4B+",
        "metric_label": "rows of CES data covered",
        "summary": "An AI strategic-insights agent that queries BigQuery, writes executive reports and keeps a "
                   "validated knowledge base of metric definitions that grows with every analysis.",
        "tags": ["Agentic AI", "BigQuery", "Knowledge base"],
        "status": "live", "link_label": "Open the demo",
    },
    {
        "repo": "Appeasement-Analysis-Walmart",
        "category": "Customer analytics",
        "title": "Appeasement & Promo Analysis",
        "company": "Walmart",
        "metric": "45% → 71%",
        "metric_label": "appeasement utilization",
        "summary": "Promo-code issuance and redemption by category, GMV lift, diminishing returns by promo "
                   "size, and Walmart+ versus non-member behavior.",
        "tags": ["Customer strategy", "Walmart+", "Experimentation"],
        "status": "live", "link_label": "Open the demo",
    },
    {
        "repo": "Agent-Performance-Scorecard-Walmart",
        "category": "Customer care",
        "title": "Agent Performance Scorecard",
        "company": "Walmart",
        "metric": "10",
        "metric_label": "KPIs in one weighted score",
        "summary": "Grades internal and outsourced contact-center agents month by month on quality, "
                   "productivity and adherence, with every grade traceable to its benchmarks.",
        "tags": ["Workforce management", "KPI design", "Coaching"],
        "status": "live", "link_label": "Open the demo",
    },
    {
        "repo": "Call-Complexity-Walmart",
        "category": "Customer care",
        "title": "Call Complexity Scorecard",
        "company": "Walmart",
        "metric": "6",
        "metric_label": "factors, scored Low / Medium / High",
        "summary": "Scores every contact on six weighted factors to show which calls are genuinely hard, "
                   "with drill-downs to individual contacts and recommended actions.",
        "tags": ["Contact center", "Scoring model", "Operations"],
        "status": "live", "link_label": "Open the demo",
    },
    {
        "repo": "Call-Complexity-vs-SSR-Walmart",
        "category": "Customer care",
        "title": "Self-Serve vs. Call Complexity",
        "company": "Walmart",
        "metric": "SSR",
        "metric_label": "against call complexity",
        "summary": "Where self-service is winning, and where the calls left for agents are getting harder, "
                   "by workflow and over time.",
        "tags": ["Self-serve AI", "Operations", "Trend analysis"],
        "status": "live", "link_label": "Open the demo",
    },
]

# Homepage structure (modelled on Victor Chowdhury's layout, own wording).
WORK_CATEGORIES = ["AI & agents", "Customer care", "Customer analytics", "Retail & operations"]
FEATURED = ["Smart-Woofie-Walmart", "CRM-Analysis-Walmart", "Single-Customer-Identifier-BP"]  # 3 cards, in order
WORKED_WITH = ["Walmart", "BP", "Nike", "EmblemHealth"]
EDUCATION_BADGE = "George Washington University"
OVERVIEW_TITLE = "From rear-view reporting to steering the business"
# "What I bring": skill chips. The first SKILLS_VISIBLE show; the rest sit behind "+N more".
SKILLS = [
    "AI & analytics strategy", "Agentic AI", "Conversational AI analytics", "Team leadership", "Executive storytelling",
    "Measurement frameworks", "Governed metrics & semantic layers", "Customer data unification",
    "Customer lifetime value", "Survival analysis", "Customer segmentation", "Self-service analytics",
    "Data modeling & governance", "Data pipelines & ETL", "BI & dashboard development", "Stakeholder management",
    "Fuel, fleet & shrink analytics", "Natural-language querying",
    "SQL", "Python", "PySpark", "BigQuery", "AWS", "Teradata", "Palantir Foundry", "Tableau", "Power BI", "Claude",
]
SKILLS_VISIBLE = 18

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
