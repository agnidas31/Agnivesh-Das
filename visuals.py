"""
Content for the visual one-page project summaries (each BP repo's index.html).

Rules (see PORTFOLIO.md):
- Every number in a chart, table or example here is FICTITIOUS, chosen only to show how the
  method and the output worked. No real BP data.
- Headline results in `results` / `impact.results` are Agnivesh's confirmed, published outcomes
  (the same numbers as content.py and the hub cards), and are labelled as reported results.
- Role, problem and approach text follows the confirmed case studies in each repo.
"""
from charts import (C1, C2, C3, columns, data_table, dbars, esc, hbars, line, stacked_hbars, waterfall)


def source_cards(cards, footer):
    """cards = [(name, tagline, [(k, v), ...])]; footer = the 'what's missing' line."""
    out = ['<div class="srcs">']
    for name, tag, rows in cards:
        dl = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in rows)
        out.append(f'<div class="src"><b>{esc(name)}</b><em>{esc(tag)}</em><dl>{dl}</dl></div>')
    out.append(f'</div><div class="nokey"><span>✕</span>{esc(footer)}</div>')
    return "".join(out)


def formula(lines):
    return '<div class="formula">' + "".join(f"<div>{l}</div>" for l in lines) + "</div>"


def chips(items):
    return '<div class="chips">' + "".join(f"<span>{esc(i)}</span>" for i in items) + "</div>"


def table(headers, rows, hl_col=None):
    th = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def ok(t):
    return f'<span class="st ok">✓ {esc(t)}</span>'


def warn(t):
    return f'<span class="st warn">! {esc(t)}</span>'


# ---------------------------------------------------------------------------------------------
# Single Customer Identifier
# ---------------------------------------------------------------------------------------------
SCI = {
    "role_line": "I owned the path from raw source data to a linked, scored customer view.",
    "eyebrow": "BP · Fuel & Convenience Retail · Customer data",
    "title": "Single Customer Identifier",
    "hook": "Three transaction systems that never shared a key, linked into one confidence-scored view of "
            "every customer, including the ones who never swipe a loyalty card.",
    "role": "Senior Data Analyst, Dataworx AI",
    "stack": ["SQL", "Python", "Cosine similarity", "Layered data model"],
    "results": [("38%", "increase in fuel-to-store conversion"), ("3 → 1", "datasets in one customer view"),
                ("3", "markets: UK, Germany, Poland")],
    "problem": {
        "headline": "One purchase, three records, no way to connect them",
        "text": "A single forecourt purchase could create a till record, a loyalty swipe and a card payment, "
                "each in a different system. The business could see a basket, a member or a card, but never the "
                "customer behind all three.",
        "visual": source_cards([
            ("EPOS (till)", "What was bought", [("Records / month", "2.4M baskets"), ("Knows", "items, value, site")]),
            ("Loyalty", "Who bought it", [("Records / month", "0.7M swipes"), ("Knows", "member, points")]),
            ("Payment", "How it was paid", [("Records / month", "1.9M card payments"), ("Knows", "card token, amount")]),
        ], "No common key between any of the three systems"),
        "points": [
            ("Only a fraction was visible", "Loyalty covered a minority of spend; every non-swiping customer was invisible."),
            ("No ground truth", "Matching was unsupervised: no labelled list of true matches to train or test against."),
            ("Clocks disagreed", "Timestamps and values drifted between systems; busy sites had near-identical baskets."),
        ],
    },
    "approach": {
        "headline": "Block, score, dampen, link",
        "text": "A tolerance-based matching model that says how confident it is in every link it makes.",
        "steps": [
            ("Refine", "Clean all three sources into one common data model, market by market."),
            ("Block", "Only compare records from the same site, date, country and basket type."),
            ("Score", "Cosine similarity across time, value and quantity: 0 at the tolerance edge, 1 for exact."),
            ("Dampen", "Scale each score by its share of all competing candidates."),
            ("Link", "Keep the best match above 0.7 and chain EPOS, Payment and Loyalty into one record."),
            ("Measure", "Roll linked transactions up into customer KPIs, reported with coverage and confidence."),
        ],
        "extra_title": "The confidence score, worked through (illustrative transactions)",
        "extra": formula([
            "<b>Confidence</b> = Similarity × Dampening",
            "<b>Dampening</b> = Similarity ÷ Σ similarity of all feasible matches",
        ]) + table(["Pair", "Similarity", "Competing candidate", "Confidence", "Decision"], [
            ["E1 ↔ P1", "0.85", "none", "<b>0.85</b>", ok("Linked")],
            ["E2 ↔ P2", "0.94", "E3", "<b>0.61</b>", warn("Linked, flagged as contested")],
            ["E3 ↔ P2", "0.52", "E2", "<b>0.19</b>", "<span class='st no'>✕ Rejected</span>"],
        ]),
    },
    "contribution": [
        ("Sourcing", "Brought the raw data in",
         "Pulled raw EPOS, Loyalty and Payment data from each source system, per market.",
         ["Till baskets", "Loyalty swipes", "Card payments"]),
        ("Modelling", "Built the common data model",
         "Cleaned and standardised all three sources so they could be compared like for like.",
         ["Refine layer", "Market-specific tolerances", "Scope definitions"]),
        ("Matching", "Built the matching models",
         "Wrote the statistical models that find approximate matches and score every link.",
         ["Blocking keys", "Similarity + dampening", "0.7 threshold"]),
    ],
    "output": {
        "headline": "A linked customer base you can size, segment and trust",
        "panels": [
            {"title": "Link rate by dataset pair", "sub": "% of in-scope transactions linked",
             "html": stacked_hbars([("EPOS ↔ Payment", [58, 24]), ("EPOS ↔ Loyalty", [71, 17]),
                                    ("Payment ↔ Loyalty", [44, 21])],
                                   ["Exact-key match", "Confidence-scored match"], [C1, C2], suf="%")},
            {"title": "Coverage vs. confidence threshold", "sub": "% of in-scope transactions retained",
             "html": line([("Coverage", C1, [(.5, 84.1), (.55, 83.8), (.6, 83.5), (.65, 83.0), (.7, 82.2),
                                             (.75, 80.4), (.8, 76.5), (.85, 70.3), (.9, 61.0), (.95, 44.2)])],
                          [(.5, "0.5"), (.6, "0.6"), (.7, "0.7"), (.8, "0.8"), (.9, "0.9"), (.95, "0.95")],
                          .5, .95, 40, 90, [40, 50, 60, 70, 80, 90], suf="%", vline=(.7, "Chosen: 0.7"))},
            {"title": "Customers now visible, by segment", "sub": "Thousands of customers; copper = newly visible",
             "wide": True,
             "html": columns([("Engaged loyalty", 310), ("Semi-engaged", 420), ("Unengaged loyalty", 560),
                              ("Card-only (non-loyalty)", 1840), ("Fleet", 95)],
                             suf="k", highlight=("Card-only (non-loyalty)",))},
        ],
    },
    "impact": {
        "results": [("38%", "fuel-to-store conversion", "Cross-shopping insight from the unified view powered targeted promotions."),
                    ("3 → 1", "customer view", "EPOS, Loyalty and Payment joined into one record per customer."),
                    ("3 markets", "on one model", "UK, Germany and Poland on the same layered model, tuned per market."),
                    ("1 source", "of customer truth", "bp's Customer Lifetime Value model was built on SCI.")],
        "before_after": [("View of the customer", "Loyalty members only", "Loyalty and non-loyalty, linked by card token"),
                         ("Trust in a match", "Not measured", "Every link carries a 0–1 confidence score"),
                         ("Unmatched records", "Looked like failures", "Scope vs. coverage separates unmatchable from missed"),
                         ("New market", "Rebuild from scratch", "Same layered model, tuned per market")],
        "closing": "From “we know our loyalty members” to “we know our customers, and how sure we are of every link.”",
    },
}

# ---------------------------------------------------------------------------------------------
# Customer Lifetime Value
# ---------------------------------------------------------------------------------------------
CLV = {
    "role_line": "I built the data foundation the model stands on, and partnered with the data scientists on the rest.",
    "eyebrow": "BP · Fuel & Convenience Retail · Customer value",
    "title": "Customer Lifetime Value",
    "hook": "A forward-looking value for every customer: what they have been worth, and what they are likely "
            "to be worth over the next five years.",
    "role": "Senior Data Analyst, Dataworx AI",
    "stack": ["SQL", "Survival analysis", "Amazon SageMaker", "Athena / S3"],
    "results": [("4×", "increase in average customer spend"), ("$8M", "marketing cost savings"),
                ("8", "segment-level survival models")],
    "problem": {
        "headline": "Every customer looked the same size, because only the past was visible",
        "text": "Two customers with identical past spend can be worth very different amounts in the future. "
                "A historical report can't tell them apart.",
        "visual": stacked_hbars([("Customer A: steady weekly visitor", [432, 522]),
                                 ("Customer B: drifting away", [432, 283])],
                                ["Past margin (what reports showed)", "Future value (what nobody saw)"],
                                [C1, C2], pre="€", max_total=1000),
        "points": [
            ("No churn event", "Fuel customers don't cancel, they just stop coming. Churn had to be defined first."),
            ("Censored data", "Most customers are still active, so their true lifetime is unknown. That needs survival analysis."),
            ("Not one population", "An “Ultimate Fan” and a “Low Fuel Occasional” churn at very different rates."),
        ],
    },
    "approach": {
        "headline": "Past margin + predicted survival + discounting",
        "text": "CLV = Historical Customer Margin (24 months) + Net Present Value of the next 5 years.",
        "steps": [
            ("Link", "Start from SCI's unified customer view: loyalty, card and till data in one record."),
            ("Segment", "Assign each customer to one of eight behavioural segments."),
            ("Build the CAR", "A Customer Analytic Record of ~580 features, built in SQL in five stages."),
            ("Predict survival", "A gradient-boosting survival model (Cox loss) per segment."),
            ("Value the future", "Survival × expected margin, inflation-adjusted and discounted to today."),
            ("Score monthly", "Re-score every customer monthly; retrain every 12–18 months."),
        ],
        "extra_title": "How one customer's CLV builds up (illustrative customer, €)",
        "extra": waterfall([("Past 24 mo.", 432), ("Year 1", 160.0), ("Year 2", 124.7), ("Year 3", 98.1),
                            ("Year 4", 77.5), ("Year 5", 62.1), ("CLV", None, "total")], f="{:,.0f}", pre="€", height=220),
    },
    "contribution": [
        ("Pipeline", "Fed SCI into CLV",
         "Built and maintained the pipelines that delivered linked customer and transaction data into the model inputs.",
         ["SCI → CLV feeds", "Card-paid visits included"]),
        ("Features", "Engineered the CAR",
         "Wrote the SQL for the staged build of the ~580-feature Customer Analytic Record.",
         ["Transactions", "Loyalty & campaigns", "Products", "Behaviour flags", "Competitor pricing"]),
        ("Partnership", "Worked with the data scientists",
         "Partnered with the modelling team so the data the model learned from was accurate, complete and fit for purpose.",
         ["Data quality", "Feature reduction support"]),
    ],
    "output": {
        "headline": "One shared number for loyalty, marketing and pricing",
        "panels": [
            {"title": "Predicted survival by segment", "sub": "Probability a customer is still active",
             "html": line([("Fuel Card Professionals", C3, [(0, 100), (1, 86), (2, 75), (3, 66), (4, 58), (5, 52)]),
                           ("Ultimate Fans", C1, [(0, 100), (1, 80), (2, 66), (3, 55), (4, 46), (5, 39)]),
                           ("Low Fuel Occasionals", C2, [(0, 100), (1, 55), (2, 38), (3, 27), (4, 19), (5, 13)])],
                          [(0, "Now"), (1, "Y1"), (2, "Y2"), (3, "Y3"), (4, "Y4"), (5, "Y5")],
                          0, 5, 0, 100, [0, 25, 50, 75, 100], suf="%")},
            {"title": "Model selection", "sub": "Concordance index on held-out customers (higher is better)",
             "html": hbars([("Cox proportional hazards", .71), ("Random survival forest", .74),
                            ("Gradient boosting (Cox loss)", .78)], f="{:.2f}", max_value=1,
                           highlight=("Gradient boosting (Cox loss)",))},
            {"title": "Average CLV by customer decile", "sub": "€ per customer; top decile highlighted", "wide": True,
             "html": columns([("D1", 2380), ("D2", 1510), ("D3", 1090), ("D4", 820), ("D5", 610), ("D6", 450),
                              ("D7", 320), ("D8", 210), ("D9", 130), ("D10", 60)], pre="€", highlight=("D1",))},
        ],
    },
    "impact": {
        "results": [("4×", "average customer spend", "Value insight steered marketing toward the right customers."),
                    ("$8M", "marketing cost savings", "With customer retention improving alongside."),
                    ("5 years", "of forward view", "From looking back 24 months to looking ahead five years per customer."),
                    ("Monthly", "re-scoring", "Every customer's value and churn risk tracked over time.")],
        "before_after": [("View of value", "Past spend only", "Past margin + 5-year predicted margin"),
                         ("Churn", "Noticed after the customer left", "Predicted per customer, month by month"),
                         ("Customers treated as", "One population", "Eight segments, each with its own model"),
                         ("Time value", "Ignored", "Inflation-adjusted and discounted to today")],
        "closing": "From “what did this customer spend?” to “what is this customer worth, and how is that changing?”",
    },
}

# ---------------------------------------------------------------------------------------------
# Global Fleet KPI
# ---------------------------------------------------------------------------------------------
FLEET = {
    "role_line": "I owned the data behind the report end to end.",
    "eyebrow": "BP · Global Fleet Cards · KPI reporting",
    "title": "Global Fleet KPI Report",
    "hook": "Three regions measuring “the same” fleet business three different ways, brought into one trusted, "
            "comparable view.",
    "role": "Data Analyst",
    "stack": ["SQL", "Power BI", "Data modelling", "KPI governance"],
    "results": [("85%", "less report preparation"), ("3×", "faster decisions"), ("3 → 1", "regions in one report")],
    "problem": {
        "headline": "One global business, three local scoreboards",
        "text": "Every region reported the same KPIs in its own units, with its own definitions and time windows. "
                "Side by side, the numbers looked comparable but weren't.",
        "visual": source_cards([
            ("ESA", "Europe & South Africa", [("Volume", "litres"), ("Margin", "card contribution, local currency"),
                                               ("Active cards", "this month")]),
            ("ANZ", "Australia & New Zealand", [("Volume", "litres"), ("Margin", "site waterfall + card margin − costs"),
                                                 ("Active cards", "rolling 3 months")]),
            ("US", "United States", [("Volume", "gallons"), ("Margin", "site margin × card volume − offers"),
                                      ("Active cards", "this month")]),
        ], "No shared units, definitions or time windows"),
        "points": [
            ("Different units", "Litres and cents per litre in two regions, gallons and cents per gallon in the third."),
            ("Different margins", "Each region calculated fleet contribution its own way."),
            ("Different scope", "Some counted only bp cards; others included partner and third-party networks."),
        ],
    },
    "approach": {
        "headline": "A common model, definitions made explicit, validation built in",
        "text": "Rather than force one artificial definition, every regional definition was documented and every "
                "comparison made like for like.",
        "steps": [
            ("Ingest", "Monthly extracts from each region's fleet system."),
            ("Standardise", "One common data model, with unit and currency carried as columns."),
            ("Calculate", "KPIs per region, each using that region's documented definition."),
            ("Compare", "Cross-region views use trends and year-on-year change, not raw totals."),
            ("Validate", "Reconcile every refresh against each region's own reporting."),
            ("Report", "Global summary, regional drill-down, definitions and validation pages."),
        ],
        "extra_title": "The KPI set",
        "extra": chips(["Fleet volume", "Fleet contribution margin", "Active cards (1 & 3 month)",
                        "Active customers (1 & 3 month)", "Average volume per card", "Fleet share of volume"]),
    },
    "contribution": [
        ("Data preparation", "Brought the regions together",
         "Pulled fleet card volume, margin, card and customer data from three regional systems.",
         ["ESA", "ANZ", "US"]),
        ("Transformation", "Made the definitions explicit",
         "Standardised each region into one model, documented every KPI per region and built the validation checks.",
         ["Common data model", "KPI dictionary", "Reconciliation rules"]),
        ("Reporting", "Built the Power BI report",
         "Global summary, by-region views, a definitions page and a KPI validation page.",
         ["4 report pages", "Monthly + YTM views"]),
    ],
    "output": {
        "headline": "Regions compared on what actually matters: direction of travel",
        "panels": [
            {"title": "Fleet volume, indexed", "sub": "Each region indexed to January = 100, so units don't matter",
             "html": line([("ESA", C1, list(enumerate([100, 100.4, 100.1, 100.8, 101.0, 100.7, 101.3, 101.6, 101.2, 101.8, 101.7, 102.0]))),
                           ("ANZ", C3, list(enumerate([100, 99.6, 99.9, 99.2, 98.9, 99.1, 98.6, 98.4, 98.7, 98.1, 97.9, 97.7]))),
                           ("US", C2, list(enumerate([100, 99.3, 98.9, 98.0, 97.6, 97.1, 96.4, 95.9, 95.2, 94.6, 94.0, 93.5])))],
                          [(0, "Jan"), (2, "Mar"), (4, "May"), (6, "Jul"), (8, "Sep"), (11, "Dec")],
                          0, 11, 92, 104, [92, 96, 100, 104], f="{:.1f}")},
            {"title": "Fleet volume, year on year", "sub": "% change vs. same month last year",
             "html": dbars([("ESA", 2.0), ("ANZ", -2.3), ("US", -6.5)], suf="%")},
            {"title": "KPI validation page", "sub": "Report vs. each region's own figures, this month", "wide": True,
             "html": table(["Region", "Report", "Regional source", "Difference", "Status"], [
                 ["ESA", "500.0M litres", "499.6M litres", "0.08%", ok("Reconciled")],
                 ["ANZ", "185.0M litres", "185.0M litres", "0.00%", ok("Reconciled")],
                 ["US", "46.0M gallons", "46.3M gallons", "0.65%", warn("Under review")],
             ])},
        ],
    },
    "impact": {
        "results": [("85%", "less report preparation", "The monthly cross-region pack no longer had to be built by hand."),
                    ("3×", "faster decisions", "Fleet managers got answers from one trusted view."),
                    ("3 → 1", "regions, one report", "ESA, ANZ and the US on a single page."),
                    ("100%", "of KPIs defined", "Every KPI documented for every region.")],
        "before_after": [("Source of numbers", "Separate regional reports", "One report, one data model"),
                         ("Definitions", "Implicit, different per region", "Documented per KPI, per region"),
                         ("Comparisons", "Raw totals, often misleading", "Trends and year-on-year, like for like"),
                         ("Trust", "“Which number is right?”", "Validation page reconciles to source")],
        "closing": "Making the differences visible, instead of hiding them, is what let leaders compare regions with confidence.",
    },
}

# ---------------------------------------------------------------------------------------------
# Inventory Over & Short
# ---------------------------------------------------------------------------------------------
INVENTORY = {
    "role_line": "I owned the data behind the report end to end.",
    "eyebrow": "BP · US Convenience Retail · Loss prevention",
    "title": "Inventory Over & Short",
    "hook": "Thousands of store audit adjustments turned into a ranked view of where stock is being lost, how fast, "
            "and which stores need attention first.",
    "role": "Data Analyst",
    "stack": ["SQL", "Power BI", "Outlier detection", "Category mapping"],
    "results": [("22%", "better inventory recovery"), ("4×", "faster prioritization"), ("2 → 1", "brands in one view")],
    "problem": {
        "headline": "Raw audit totals pointed teams at the wrong stores",
        "text": "Stores are audited at different intervals, so a bigger dollar loss isn't always the bigger problem. "
                "Ranking by raw adjustment sent loss prevention to the wrong door.",
        "visual": '<div class="pair">'
                  '<div><h4>Ranked by raw audit loss</h4>'
                  + hbars([("Store A (90 days)", 3000), ("Store B (30 days)", 2000), ("Store C (45 days)", 1200)],
                          pre="$", highlight=("Store A (90 days)",)) +
                  '</div><div><h4>Ranked by loss per day</h4>'
                  + hbars([("Store B", 67), ("Store A", 33), ("Store C", 27)], pre="$", suf="/day",
                          highlight=("Store B",)) + "</div></div>",
        "points": [
            ("Different audit intervals", "A 90-day loss and a 30-day loss can't be compared as totals."),
            ("Two brands, two vocabularies", "Thorntons and ampm used different audit categories."),
            ("Big stores lose more dollars", "Ranking by dollars favoured busy stores, not badly run ones."),
        ],
    },
    "approach": {
        "headline": "Normalise by time, standardise by category, rank by exception",
        "text": "Make every store comparable first, then let the outliers surface on their own.",
        "steps": [
            ("Ingest", "Audit results, item hierarchy, store attributes and sales."),
            ("Standardise", "Map both brands' audit categories into one hierarchy."),
            ("Align", "Link each audit to the store's previous audit to get the period length."),
            ("Calculate", "Over/short in $, loss per day, and loss as a share of sales."),
            ("Rank", "Flag stores far above their region's normal, and worsening trends."),
            ("Report", "Monthly, item, category and outlier-store views in Power BI."),
        ],
        "extra_title": "The two formulas that change the ranking",
        "extra": formula(["<b>Loss per day</b> = audit adjustment ÷ days since previous audit",
                          "<b>Outlier</b> = loss per day &gt; region mean + 2 standard deviations"]),
    },
    "contribution": [
        ("Data preparation", "Brought two brands together",
         "Pulled audit results, item and department hierarchies, store attributes and sales for Thorntons and ampm.",
         ["Audits", "Item master", "Store master", "Sales"]),
        ("Transformation", "Made stores comparable",
         "Standardised categories across brands, aligned audits to periods and built the loss-per-day logic.",
         ["Category mapping", "Audit periods", "Loss per day"]),
        ("Reporting", "Built the Power BI report",
         "Monthly analysis, item level, category time series, outlier stores, latest audits and loss per day.",
         ["9 report pages", "Brand / region / store filters"]),
    ],
    "output": {
        "headline": "Where to go first, and what to look for when you get there",
        "panels": [
            {"title": "Outlier stores", "sub": "Loss per day; copper = above the region's outlier line",
             "html": hbars([("Store B", 67), ("Store F", 58), ("Store K", 51), ("Store D", 47), ("Store A", 33),
                            ("Store H", 31), ("Store C", 27), ("Store J", 22)], pre="$",
                           highlight=("Store B", "Store F", "Store K", "Store D"), ref=45, ref_label="Outlier line $45")},
            {"title": "Store B: loss by category", "sub": "$ per day; most of the loss sits in two categories",
             "html": hbars([("Cigarettes", 31), ("Beer", 16), ("Fresh food", 8), ("Candy", 5), ("Grocery", 4),
                            ("Other", 3)], pre="$", highlight=("Cigarettes", "Beer"))},
            {"title": "Network loss per store per day", "sub": "Average across stores, $", "wide": True,
             "html": line([("Loss per day", C1, list(enumerate([41, 42, 40, 43, 41, 39, 36, 34, 33, 32, 31, 32])))],
                          [(0, "Jan"), (2, "Mar"), (4, "May"), (6, "Jul"), (8, "Sep"), (11, "Dec")],
                          0, 11, 25, 45, [25, 30, 35, 40, 45], f="${:,}", vline=(4.5, "Targeting starts"))},
        ],
    },
    "impact": {
        "results": [("22%", "better inventory recovery", "Loss-prevention effort went where stock was actually being lost."),
                    ("4×", "faster prioritization", "The stores needing attention first surfaced in a fraction of the time."),
                    ("2 → 1", "brands, one hierarchy", "Thorntons and ampm audits in one consistent structure."),
                    ("Per day", "comparable stores", "Loss per day removed the distortion of different audit intervals.")],
        "before_after": [("View of loss", "Raw audit adjustments", "Loss per day, comparable across stores"),
                         ("Categories", "Different per brand", "One hierarchy across both brands"),
                         ("Prioritisation", "Biggest dollar figure", "Outlier stores and worsening trends"),
                         ("Root cause", "Store total only", "Drill-down to department, category and item")],
        "closing": "From “here are this month's adjustments” to “here is where we're losing stock fastest, and in what.”",
    },
}

# ---------------------------------------------------------------------------------------------
# Fuel Margin Waterfall
# ---------------------------------------------------------------------------------------------
FUEL = {
    "role_line": "I owned the data behind the report end to end.",
    "eyebrow": "BP · US Fuels Pricing · Margin analytics",
    "title": "Fuel Margin Waterfall",
    "hook": "One cents-per-gallon margin number broken into the drivers behind it, so pricing and supply teams "
            "could see not just what the margin was, but why.",
    "role": "Data Analyst",
    "stack": ["SQL", "Tableau", "Volume weighting", "Reconciliation"],
    "results": [("2×", "faster root-cause analysis"), ("3", "margin layers in one view"), ("Site", "level drill-down, every grade")],
    "problem": {
        "headline": "A margin number with no story behind it",
        "text": "When margin dropped a cent, nobody could say why without a manual investigation across systems. "
                "One cent across hundreds of millions of gallons is millions of dollars.",
        "visual": '<div class="onenum"><div class="big"><small>Standard margin, this month</small>7.5 <span>cpg</span>'
                  '<em>▼ 1.0 cpg vs. last month · ≈ $5M</em></div><div class="why"><b>But why?</b>'
                  '<span>Market moved?</span><span>Brand premium changed?</span><span>Supply terms worse?</span>'
                  '<span>Volume vs. invoice?</span><span>Environmental costs?</span></div></div>',
        "points": [
            ("Every driver in a different system", "Market prices by terminal, invoices by delivery, volumes by site, terms by contract."),
            ("Averages lie", "A simple average gives a small site the same weight as a large one."),
            ("The parts must add up", "A waterfall is only trusted if the bars sum exactly to the reported margin."),
        ],
    },
    "approach": {
        "headline": "One grain, volume-weighted, every driver as its own bar",
        "text": "Store each component in dollars at site × day × grade; convert to cents per gallon only at report time, "
                "so the bars always sum to the total.",
        "steps": [
            ("Ingest", "Market reference prices, retail prices, invoices, contract terms and volumes."),
            ("Align", "Map everything to site × day × fuel grade, with site attributes attached."),
            ("Weight", "Store components in dollars; divide by total gallons at the last step."),
            ("Decompose", "Calculate each driver so components sum exactly to the total."),
            ("Reconcile", "Check against the finance margin every refresh; watch the “others” bar."),
            ("Report", "Tableau waterfalls: monthly, YTD and year on year, from network to site."),
        ],
        "extra_title": "Three layers of margin (illustrative, cents per gallon)",
        "extra": waterfall([("Standard", 8.5), ("Logistics", 1.4), ("Supply & trading", 0.9),
                            ("Integrated", None, "total"), ("Lag effect", -0.6), ("RINs", 1.1),
                            ("Programme costs", -0.3), ("Total", None, "total")], height=220),
    },
    "contribution": [
        ("Data preparation", "Brought the drivers together",
         "Combined pricing, supply cost, invoice and volume data from multiple source systems.",
         ["Market prices", "Invoices", "Contract terms", "Volumes"]),
        ("Transformation", "Made the parts add up",
         "Aligned everything to site × day × grade, volume-weighted every component and built the decomposition.",
         ["Common grain", "Volume weighting", "Reconciliation"]),
        ("Reporting", "Built the Tableau waterfalls",
         "Monthly, year-to-date and year-on-year views, filterable from channel of trade down to site and grade.",
         ["5 views", "10 filters"]),
    ],
    "output": {
        "headline": "The answer to “why did margin move?” read straight off the chart",
        "panels": [
            {"title": "Standard margin waterfall", "sub": "One month, network view, cents per gallon", "wide": True,
             "html": waterfall([("Market (rack low)", 7.0), ("Brand value", 10.0), ("bp premium", -8.5),
                                ("Terms", -1.2), ("Volume variance", 1.3), ("Others", -0.1),
                                ("Standard margin", None, "total")])},
            {"title": "What moved this month", "sub": "Change vs. last month, cpg",
             "html": dbars([("Market (rack low)", 0.2), ("Brand value", 0.0), ("bp premium", -1.1), ("Terms", -0.1),
                            ("Volume variance", 0.0), ("Others", 0.0), ("Standard margin", -1.0)],
                           highlight=("Standard margin",))},
            {"title": "Reading it", "sub": "Illustrative month",
             "html": '<div class="readout"><p><b>Brand value held.</b> Pricing at the pump wasn\'t the problem.</p>'
                     '<p><b>The bp premium widened by 1.1 cpg.</b> Branded supply cost more relative to the market low.</p>'
                     '<p><b>So the conversation goes to supply, not pricing</b>, with the size of the gap already on the table.</p>'
                     '<p class="calc">8.5 cpg × 500M gallons = $42.5M standard margin</p></div>'},
        ],
    },
    "impact": {
        "results": [("2×", "faster root-cause analysis", "Margin moves explained straight from the chart, sharpening supply decisions."),
                    ("3 layers", "in one view", "Standard, integrated and environmental margin together."),
                    ("Every cent", "explained", "Each change traced to a specific driver and owner."),
                    ("Network → site", "same breakdown", "At every level, for every fuel grade.")],
        "before_after": [("What you see", "One margin number", "Every driver as its own bar"),
                         ("Explaining a change", "Manual investigation", "Read straight off the chart"),
                         ("Weighting", "Inconsistent averages", "Volume-weighted throughout"),
                         ("Trust", "Didn't always tie to finance", "Components reconcile to the total")],
        "closing": "From “what was our margin?” to “what moved our margin, and who owns it?”",
    },
}

VISUALS = {
    "Single-Customer-Identifier-BP": SCI,
    "Customer-Lifetime-Value-BP": CLV,
    "Global-Fleet-BP": FLEET,
    "Inventory-Over-Short-BP": INVENTORY,
    "Fuel-Margin-Waterfall-BP": FUEL,
}
