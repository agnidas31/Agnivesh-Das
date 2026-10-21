"""
Single source of truth for Agnivesh Das's résumé AND portfolio website.

Every role, date and metric here is confirmed by Agnivesh. Do not add outcomes,
employers, tools or scope that are not supported by his confirmed history.
Placeholders are wrapped in [square brackets] so they are easy to find.
"""

PROFILE = {
    "name": "Agnivesh Das",
    "tagline": "Data Analytics & AI Leadership · Customer Insights · Data Engineering",
    "location": "Bentonville, Arkansas",
    "email": "agnivesh.das@gmail.com",
    "phone": "",  # kept out of this public repo; pass --phone to build.py for the private résumé
    "linkedin": "linkedin.com/in/agnivesh-das",
    "portfolio": "agnidas31.github.io/Agnivesh-Das",  # switch to the custom domain once it is live
}

SUMMARY = (
    "<b>Data Analytics & AI Leader</b> with <b>13+ years</b> across <b>Walmart, BP and Nike</b>, currently leading a "
    "<b>team of 8+ across Operations, Workforce Management, CRM and Self-Serve AI</b> for Walmart Customer Engagement "
    "Services. Builds the foundations that make enterprise data trustworthy (governed metric "
    "repositories, measurement frameworks, data pipelines) and the AI agents that put answers in leaders' hands the "
    "moment they need them. Expertise spans conversational AI, customer analytics and lifetime value, fuel and fleet "
    "operations, and data engineering, consistently turning analytics from a rear-view mirror into a steering wheel. "
    "Just as comfortable shaping the data strategy as building the first working version of it."
)

# Signature Work: the metric callout band. Keep each metric attached to its project.
SIGNATURE = [
    {"metric": "$17M", "label": "CRM AI Savings", "tag": "Walmart · CRM",
     "detail": "Championed Agent Assist voice and chat AI across CRM, cutting average handle time 23% on the way "
               "to realized savings."},
    {"metric": "25% → 62%", "label": "Self-Serve Rate", "tag": "Walmart · Sierra Voice AI",
     "detail": "Lifted self-service on the AI voice assistant, with CSAT climbing steadily alongside it."},
    {"metric": "45% → 71%", "label": "Appeasement Strategy", "tag": "Walmart · Customer Engagement",
     "detail": "Sharpened how appeasements are matched to customers; the findings fed directly into Walmart+ "
               "adoption strategy."},
    {"metric": "AISLE1", "label": "AI Insights Product", "tag": "Agentic AI · Claude + BigQuery",
     "detail": "VPs and senior directors now pull core metrics themselves in plain English, no ad hoc request needed."},
    {"metric": "38%", "label": "Fuel-to-Store Conversion", "tag": "BP · Single Customer Identifier",
     "detail": "Fuel and store data unified into one customer view, powering cross-shopping promotions."},
    {"metric": "4×", "label": "Average Customer Spend", "tag": "BP · Customer Lifetime Value",
     "detail": "Customer-value insights steered marketing to the right customers, saving $8M and lifting retention."},
    {"metric": "3 → 1", "label": "One Global Fleet View", "tag": "BP · Global Fleet",
     "detail": "ESA, ANZ and the US on a single trusted KPI view; report prep cut 85%, decisions 3× faster."},
    {"metric": "22%", "label": "Better Inventory Recovery", "tag": "BP · Inventory Over & Short",
     "detail": "Store audits turned into a ranked shrink-prevention view; priority stores flagged 4× faster."},
]

# Three columns: Leadership & Strategy · AI & Customer Analytics · Data Foundations & Engineering.
# The first item in each column is its lead capability (rendered as the dark box).
CAPABILITIES = [
    [
        "AI & Analytics Strategy",
        "Team Leadership & Delivery",
        "Executive Data Storytelling",
        "Stakeholder Management",
        "Self-Service Analytics Enablement",
    ],
    [
        "Agentic AI & GenAI Applications",
        "Conversational AI Analytics",
        "Customer Data Unification",
        "Customer Lifetime Value Modeling",
        "Fuel, Fleet & Shrink Analytics",
    ],
    [
        "Governed Metrics & Semantic Layers",
        "Measurement Frameworks & KPIs",
        "Data Pipelines & ETL at Scale",
        "Data Modeling & Governance",
        "BI & Dashboard Development",
    ],
]

# Experience, most recent first. "lead" bullets are rendered as prominent paragraphs.
EXPERIENCE = [
    {
        "employer": "Walmart",
        "tenure": "",
        "roles": [
            {
                "title": "Manager, Strategic Insights & AI — Customer Engagement Services",
                "dates": "Sep 2025 — Present",
                "location": "Bentonville, Arkansas",
                "context": "Conversational AI, CRM, customer service analytics",
                "lead": [
                    "<b>Championed AI initiatives across CRM that delivered $17M in savings and cut average handle "
                    "time 23%</b>: bringing Agent Assist voice and chat agents from pilot through adoption, with pilot "
                    "design, adoption tracking, scale-or-stop calls, and measurement through to realized savings.",
                    "<b>Built AISLE1, an agentic AI insights product that lets VPs and senior directors query core "
                    "metrics in plain English</b>: a Claude-powered analytics suite on a BigQuery backend that serves "
                    "as the organization's governed metric repository. A semantic layer keeps every definition "
                    "certified and consistent, so leaders get narrative answers on demand instead of raising ad hoc "
                    "requests.",
                    "<b>Drove appeasement utilization from 45% to 71%</b> by sharpening how service appeasements are "
                    "matched to customers. The insights went on to help shape Walmart+ adoption strategy.",
                ],
                "bullets": [
                    "<b>Built the measurement framework for Sierra, Walmart's AI voice assistant, lifting self-serve "
                    "rate from 25% to 62%</b>, with CSAT improving consistently as adoption grew.",
                    "<b>Lead a team of 8+ across four pillars (Operations, Workforce Management, CRM and Self-Serve "
                    "AI)</b>, setting analytics priorities and tying each team's work to service cost and customer "
                    "experience.",
                    "<b>Built the Agent Performance Scorecard</b>, one performance management view for Walmart's "
                    "internal and outsourced agents, holding both workforces to the same measurable standard.",
                ],
            },
        ],
    },
    {
        "employer": "British Petroleum (BP)",
        "tenure": "8+ years",
        "roles": [
            {
                "title": "Senior Data Analyst — Dataworx AI Team",
                "dates": "Feb 2021 — Aug 2025",
                "location": "Chicago, Illinois",
                "context": "Customer 360, identity resolution and customer value modeling across UK and European markets",
                "lead": [
                    "<b>Led development of the Single Customer Identifier (SCI), BP's Customer 360 foundation, lifting "
                    "fuel-to-store conversion 38%</b>: unified till (EPOS), loyalty and card-payment data across fuel "
                    "and convenience into a single customer profile across the UK, Germany and Poland.",
                    "<b>Designed the deterministic and probabilistic matching logic behind SCI</b>: cleansed each "
                    "source, matched exactly on site, date and basket type, then confidence-scored candidates within "
                    "time and value tolerances.",
                    "<b>Delivered $8M in marketing savings and a 4× increase in average customer spend through "
                    "Customer Lifetime Value (CLV)</b>: built on the unified SCI view, value and retention insights "
                    "pinpointed the highest-value customer segments and steered targeted marketing toward them, "
                    "improving retention.",
                ],
                "bullets": [
                    "<b>Engineered the CLV data foundation</b>, building the ~580-feature customer analytic record in "
                    "SQL from SCI's linked data and partnering with data scientists on survival-based churn models and "
                    "NPV valuation.",
                    "<b>Mapped cross-channel behavior</b> (loyalty vs. card-only, fleet vs. non-fleet, fuel vs. shop), "
                    "revealing customers who never swipe a loyalty card.",
                ],
            },
            {
                "title": "Data Analyst — NA Fuel Analytics Team",
                "dates": "Feb 2017 — Jan 2021",
                "location": "Chicago, Illinois",
                "context": "Fuel, fleet and convenience retail analytics; owned data preparation, transformation and reporting end to end",
                "lead": [
                    "<b>Unified BP's global fleet card KPIs across ESA, ANZ and the US into one trusted report, cutting "
                    "report preparation 85% and enabling 3× faster decisions by fleet managers</b>: standardized three "
                    "regional systems into a common data model while keeping each region's definitions explicit "
                    "(litres vs. gallons, cents per litre vs. cents per gallon, region-specific contribution margin).",
                    "<b>Turned store inventory audits into a ranked shrink-prevention tool across Thorntons and ampm, "
                    "identifying priority stores 4× faster and improving inventory recovery 22%</b>: consolidated audit "
                    "adjustments by store, department and category (tobacco, beer, beverages, fresh food) and "
                    "normalized losses to a per-day rate so stores on different audit cycles compared fairly.",
                    "<b>Decomposed fuel margin against market and competitor prices into its drivers, cutting "
                    "root-cause analysis time by 2× and improving supply decisions</b>: built a cents-per-gallon "
                    "waterfall separating market (OPIS) margin, brand value, supply premium, contract terms and "
                    "invoice-volume variance, rolling up to standard, integrated and environmental margin.",
                ],
                "bullets": [
                    "<b>Built a fleet KPI dictionary and validation layer</b> reconciling volume, contribution margin and "
                    "active cards and customers (monthly and rolling 3-month) to each region's source reporting, so "
                    "leaders compared regions on trends and year-on-year change with confidence.",
                    "<b>Delivered the inventory reporting suite in Power BI</b>, from monthly analysis and item-level "
                    "detail to outlier-store rankings, latest audits and department and category trends, giving "
                    "loss-prevention and store leaders a clear list of where to act first.",
                    "<b>Aligned pricing, supply-cost, invoice and volume data to a single site × day × grade grain</b> "
                    "and volume-weighted every margin component so the Tableau waterfall summed to total margin, with "
                    "monthly, year-to-date and year-on-year views down to individual site and fuel grade.",
                ],
            },
        ],
    },
    {
        "employer": "Nike",
        "tenure": "",
        "roles": [
            {
                "title": "Business Intelligence Engineer",
                "dates": "Feb 2015 — Jan 2017",
                "location": "Beaverton, Oregon",
                "context": "Supply Chain Planning Analytics, Nike Digital; legacy Cognos to Tableau modernization",
                "lead": [
                    "<b>Owned the move of Nike's supply chain planning reporting from legacy Cognos to Tableau, "
                    "speeding up decision-making 25%</b>: rebuilt aging static reports as interactive dashboards on "
                    "SQL and Teradata, giving planning teams a faster read on supply against consumer demand for "
                    "Nike Digital.",
                    "<b>Built the data foundation underneath</b>: Teradata pipelines ingesting transactional and "
                    "customer data from four primary sources, with ETL automated across billions of rows to cut "
                    "manual workload <b>20% a month</b>.",
                ],
                "bullets": [
                    "<b>Drove adoption of the new dashboards</b>, training 30+ team members and lifting dashboard "
                    "utilization <b>40%</b>.",
                ],
            },
        ],
    },
    {
        "employer": "EmblemHealth",
        "tenure": "",
        "roles": [
            {
                "title": "Business Analyst",
                "dates": "Feb 2013 — Jan 2015",
                "location": "New York City, New York",
                "context": "Health insurance (payer); ICD-9 to ICD-10 regulatory migration",
                "lead": [
                    "<b>Bridged business, clinical coding and IT teams through EmblemHealth's ICD-9 to ICD-10 "
                    "migration</b>, a federally mandated overhaul that expanded diagnosis codes roughly five-fold: "
                    "assessed the impact on data models, claims workflows and reporting, and turned it into Business "
                    "Requirements and Functional Specifications documents.",
                ],
                "bullets": [
                    "<b>Built the Requirements Traceability Matrix (RTM)</b>, tracing every business and regulatory "
                    "rule from requirement through development and testing so nothing was missed in the cutover.",
                    "<b>Led user acceptance testing for end-to-end claims processing</b>, translating business scenarios "
                    "into test cases that confirmed claims processed correctly under ICD-10 rules.",
                    "<b>Ran requirements sessions with claims, coding and compliance stakeholders</b> and supported "
                    "code mapping from ICD-9 to ICD-10.",
                ],
            },
        ],
    },
]

TECH_ENVIRONMENT = [
    ("AI & Analytics", "LLM applications, agentic AI, conversational AI, natural-language querying, predictive "
                       "analytics, customer lifetime value, survival analysis, customer segmentation"),
    ("Data & Cloud", "AWS (S3, Glue, Redshift, Athena, Lambda, Step Functions, CloudFormation), BigQuery, "
                     "Teradata, Palantir Foundry, semantic and metric layers, data modeling, ETL"),
    ("Languages & Tools", "SQL, Python, PySpark, Apache Spark, Pandas, Tableau, Power BI, DAX, Claude"),
]

EDUCATION = [
    {"degree": "Master's Degree, Engineering Management", "school": "George Washington University",
     "place": "Washington, D.C.", "years": "2010 — 2012"},
    {"degree": "Bachelor's Degree, Electronics & Instrumentation", "school": "West Bengal University of Technology",
     "place": "Kolkata, India", "years": "2006 — 2010"},
]

CREDENTIALS = ["[Add certifications, if any]"]
