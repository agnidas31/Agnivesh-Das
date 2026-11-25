"""
Narrative project pages (format modelled on a question-led case study: each section is a plain
question, answered with a framing sentence, one chart or table, and a short "so what").

Each page is a list of blocks rendered in order by templates/narrative.html:
  ("p", html)                       paragraph
  ("h3", text)                      finding heading (a plain question or claim)
  ("figure", title, sub, html)      chart/visual with an "illustrative" tag
  ("callouts", [(label, html)...])  side-by-side labelled notes
  ("tiles", [(metric, label)...])   stat tiles

Rules (see PORTFOLIO.md): every chart/table number is FICTITIOUS; only `results` hold confirmed outcomes.
"""
from charts import C1, C2, C3, columns, dbars, hbars, line, stacked_hbars, waterfall
from visuals import chips, formula, ok, source_cards, table, warn

SCI = {
    "repo": "Single-Customer-Identifier-BP",
    "eyebrow": "BP · Single Customer Identifier · Customer data",
    "title": "From Loyalty Members to Every Customer",
    "intro": "Every purchase on a bp forecourt left three separate records behind: a till receipt, a card payment "
             "and, sometimes, a loyalty swipe. None of them shared a key, so the business could count baskets, "
             "cards or members, but never customers. The Single Customer Identifier linked all three into one "
             "view, and said how confident it was in every link.",
    "role": "Senior Data Analyst, Dataworx AI",
    "note": "All figures, charts and examples on this page are illustrative. Values, volumes and site details "
            "have been altered or replaced with fictitious numbers; no real BP data is shown. Only the headline "
            "results are reported outcomes.",
    "project_label": "The project",
    "project_title": "One view of every forecourt customer",
    "overview": "The goal was simple to say and hard to do: take three transaction systems that were never designed to "
                "talk to each other, and join them into one record per customer, across the UK, Germany and Poland. "
                "I brought in the raw data, built the common data model, and wrote the matching models that make the links.",
    "blocks": [
        ("h3", "The starting point: one purchase, three records"),
        ("p", "A single visit could show up in the till system (<em>what</em> was bought), the payment system "
              "(<em>how</em> it was paid) and the loyalty system (<em>who</em> bought it, but only if they swiped). "
              "Each system had its own IDs, its own clocks and its own idea of a transaction."),
        ("figure", "Three systems, three partial views", "Illustrative monthly volumes for one market",
         source_cards([
             ("EPOS (till)", "What was bought", [("Records / month", "2.4M baskets"), ("Knows", "items, value, site")]),
             ("Payment", "How it was paid", [("Records / month", "1.9M card payments"), ("Knows", "card token, amount")]),
             ("Loyalty", "Who bought it", [("Records / month", "0.7M swipes"), ("Knows", "member, points")]),
         ], "No common key between any of the three systems")),
        ("p", "Loyalty only ever covered a minority of spend. Everyone who paid by card but never swiped a loyalty "
              "card was, in effect, invisible."),

        ("h3", "The method: narrow, score, link"),
        ("p", "There was no list of known matches to train against, so this was an unsupervised problem. I narrowed "
              "the search first: a till record could only match a payment from the same site, date, country and "
              "basket type. Within that small window, I scored each candidate pair on how closely their time, value "
              "and quantity agreed, and kept the best one."),
        ("figure", "Link rate by dataset pair", "% of in-scope transactions linked",
         stacked_hbars([("EPOS ↔ Payment", [58, 24]), ("EPOS ↔ Loyalty", [71, 17]), ("Payment ↔ Loyalty", [44, 21])],
                       ["Exact-key match", "Confidence-scored match"], [C1, C2], suf="%")),
        ("p", "Exact keys did most of the work, but the scored matches added roughly a fifth more coverage on every "
              "pair. That's the slice a simple join would have thrown away."),

        ("h3", "How sure is each match?"),
        ("p", "At a busy site, two or three baskets of a similar value can land in the same minute. So every link "
              "carries a confidence score: the similarity of the pair, scaled down by how many other candidates "
              "were nearly as close. Only links above a threshold are kept."),
        ("figure", "Coverage at each confidence threshold", "% of in-scope transactions retained",
         line([("Coverage", C1, [(.5, 84.1), (.55, 83.8), (.6, 83.5), (.65, 83.0), (.7, 82.2), (.75, 80.4), (.8, 76.5),
                                 (.85, 70.3), (.9, 61.0), (.95, 44.2)])],
              [(.5, "0.5"), (.6, "0.6"), (.7, "0.7"), (.8, "0.8"), (.9, "0.9")],
              .5, .95, 40, 90, [40, 50, 60, 70, 80, 90], suf="%", vline=(.7, "Chosen: 0.7"))),
        ("p", "Most real matches score very high, so coverage barely moves until the threshold passes 0.7, then "
              "falls away fast. That knee is where we set it: strict enough to trust, loose enough to keep almost "
              "everything worth keeping."),

        ("h3", "When two baskets look the same"),
        ("p", "The dampening step matters most in exactly the cases a join gets wrong. Here, two till records "
              "compete for the same card payment:"),
        ("figure", "One payment, two candidate baskets", "Illustrative transactions",
         table(["Pair", "Similarity", "Competing with", "Confidence", "Decision"], [
             ["E1 ↔ P1", "0.85", "none", "<b>0.85</b>", ok("Linked")],
             ["E2 ↔ P2", "0.94", "E3", "<b>0.61</b>", warn("Linked, flagged")],
             ["E3 ↔ P2", "0.52", "E2", "<b>0.19</b>", "<span class='st no'>✕ Rejected</span>"],
         ])),
        ("p", "E2 still wins, but its confidence drops from 0.94 to 0.61 because E3 was a plausible rival. "
              "Reporting can then treat contested links differently from clean ones, instead of pretending "
              "every match is equally certain."),

        ("h3", "Who we could suddenly see"),
        ("p", "Once the links were in place, linked transactions rolled up into one record per customer, "
              "including the people loyalty data had never captured."),
        ("figure", "Customers visible, by segment", "Thousands of customers; amber = newly visible",
         columns([("Engaged loyalty", 310), ("Semi-engaged", 420), ("Unengaged loyalty", 560),
                  ("Card-only", 1840), ("Fleet", 95)], suf="k", highlight=("Card-only",))),
        ("p", "The largest group by far was customers who paid by card but never swiped loyalty. They had been "
              "shopping with bp all along; the business just couldn't see them."),

        ("h3", "What I handed over"),
        ("callouts", [
            ("The data foundation", "Raw EPOS, Payment and Loyalty data brought in from each source system, cleaned "
                                    "into one common model per market, with the in-scope population defined for "
                                    "every pair so “unmatchable” never counted as “missed”."),
            ("The matching models", "Blocking keys, similarity scoring, dampening and a 0.7 threshold, tuned per "
                                    "market, producing a customer ID that downstream reporting and models could "
                                    "build on."),
        ]),
    ],
    "results_label": "Results",
    "results": [("38%", "increase in fuel-to-store conversion"), ("3 → 1", "datasets joined into one customer view"),
                ("3", "markets on one model: UK, Germany, Poland"), ("CLV", "bp's lifetime-value model was built on SCI")],
    "why_title": "A customer key, built once and used everywhere",
    "why": "Matching three datasets was never the point. The point was being able to ask customer questions at all: "
           "who shops with us, who crosses from the pump to the store, who is drifting away. The cross-shopping "
           "insight behind the 38% conversion lift came straight from this view, and the Customer Lifetime Value "
           "model that followed was built on top of it.",
    "scale": [("3", "source systems linked"), ("4", "blocking keys narrow every search"),
              ("0.7", "confidence threshold for a link"), ("1", "customer ID for reporting and models")],
}


# ---------------------------------------------------------------------------------------------
# Customer Lifetime Value
# ---------------------------------------------------------------------------------------------
CLV = {
    "repo": "Customer-Lifetime-Value-BP",
    "eyebrow": "BP · Customer Lifetime Value · Customer value",
    "title": "From What Customers Spent to What They're Worth",
    "intro": "Every team at bp could see what a customer had spent, but none could see what that customer was "
             "likely to be worth next. Customer Lifetime Value gave every customer a forward-looking number: past "
             "margin, plus five years of predicted margin, adjusted for the chance they would still be around to "
             "earn it.",
    "role": "Senior Data Analyst, Dataworx AI",
    "note": "All figures, charts and examples on this page are illustrative. Customers, margins, survival rates and "
            "model scores have been replaced with fictitious numbers; no real BP data is shown. Only the headline "
            "results are reported outcomes.",
    "project_label": "The project",
    "project_title": "A lifetime value for every customer",
    "overview": "CLV was built on top of the Single Customer Identifier. I built the pipelines that fed "
                "the linked customer view into the model, engineered the Customer Analytic Record it learned from, "
                "and worked alongside the data scientists who built the survival models.",
    "blocks": [
        ("h3", "The starting point: two customers who looked the same"),
        ("p", "Loyalty, marketing, pricing and store teams each had their own partial view, and every one of them "
              "looked backwards. Two customers with identical spend over the last two years looked identical in "
              "every report, even when one was a weekly regular and the other was quietly drifting away."),
        ("figure", "Same past, different future", "Illustrative customers, € margin",
         stacked_hbars([("Customer A: steady weekly visitor", [432, 522]), ("Customer B: drifting away", [432, 283])],
                       ["Past margin (what reports showed)", "Future value (what nobody saw)"], [C1, C2],
                       pre="€", max_total=1000)),
        ("p", "Their past is the same; their future value differs by more than half. That gap is exactly where "
              "retention spend should go, and no historical report could show it."),

        ("h3", "The hard part: customers never say they've left"),
        ("p", "A phone customer cancels a contract. A fuel customer just stops coming. So churn had to be defined "
              "first: six months after the last transaction. And because most customers are still active at any "
              "point, their true lifetime is unknown. That is <em>censored</em> data, and it calls for survival "
              "analysis rather than ordinary regression."),
        ("figure", "Predicted survival by segment", "Probability a customer is still active",
         line([("Fuel Card Professionals", C3, [(0, 100), (1, 86), (2, 75), (3, 66), (4, 58), (5, 52)]),
               ("Ultimate Fans", C1, [(0, 100), (1, 80), (2, 66), (3, 55), (4, 46), (5, 39)]),
               ("Low Fuel Occasionals", C2, [(0, 100), (1, 55), (2, 38), (3, 27), (4, 19), (5, 13)])],
              [(0, "Now"), (1, "Y1"), (2, "Y2"), (3, "Y3"), (4, "Y4"), (5, "Y5")],
              0, 5, 0, 100, [0, 25, 50, 75, 100], suf="%")),
        ("p", "Segments churn at very different rates, so one model for everyone would have blurred exactly the "
              "differences the business needed. Each of the eight behavioural segments got its own model."),

        ("h3", "The method: past margin, predicted survival, discounting"),
        ("p", "Lifetime value has two parts. The past is known: margin over the last 24 months. The future is "
              "predicted: expected margin for each of the next five years, multiplied by the probability the "
              "customer is still active, adjusted for inflation and discounted back to today."),
        ("figure", "How one customer's CLV builds up", "Illustrative Ultimate Fan, €",
         formula(["<b>CLV</b> = Historical Customer Margin (24 months) + NPV of the next 5 years"])
         + waterfall([("Past 24 mo.", 432), ("Year 1", 160.0), ("Year 2", 124.7), ("Year 3", 98.1),
                      ("Year 4", 77.5), ("Year 5", 62.1), ("CLV", None, "total")], f="{:,.0f}", pre="€", height=220)),
        ("p", "Each future year adds less than the one before: the customer is less likely to still be active, and "
              "a euro later is worth less than a euro now. Both effects are built into every score."),

        ("h3", "Feeding the model: one record per customer"),
        ("p", "The model learned from a Customer Analytic Record: one row per customer with roughly 580 features, "
              "built in SQL in five stages. For each segment, that was cut down to the 60–130 features that "
              "actually carried signal."),
        ("figure", "What went into the Customer Analytic Record", "Five build stages",
         chips(["Transaction KPIs", "Loyalty events & campaigns", "Product usage", "Customer behaviour flags",
                "Competitor pricing"])),
        ("p", "Because the CAR was built on SCI, the model could see the visits customers paid for by card, not "
              "just the ones where they swiped loyalty."),

        ("h3", "Picking the model"),
        ("p", "Three survival techniques were tested on the same segment. Each was scored on how well it ranked "
              "customers by how long they would stay."),
        ("figure", "Model comparison", "Concordance index on held-out customers (higher is better)",
         hbars([("Cox proportional hazards", .71), ("Random survival forest", .74),
                ("Gradient boosting (Cox loss)", .78)], f="{:.2f}", max_value=1,
               highlight=("Gradient boosting (Cox loss)",))),
        ("p", "Gradient boosting with a Cox loss won: the best ranking accuracy, built for censored data, and still "
              "explainable through feature importance."),

        ("h3", "Who's worth the most"),
        ("p", "Scored monthly, every customer could be ranked by value and tracked as that value moved."),
        ("figure", "Average CLV by customer decile", "€ per customer; top decile highlighted",
         columns([("D1", 2380), ("D2", 1510), ("D3", 1090), ("D4", 820), ("D5", 610), ("D6", 450), ("D7", 320),
                  ("D8", 210), ("D9", 130), ("D10", 60)], pre="€", highlight=("D1",))),
        ("p", "Value is heavily concentrated at the top. Knowing who sits there, and who is sliding out of it, is "
              "what let marketing spend less and earn more."),

        ("h3", "What I built"),
        ("callouts", [
            ("The SCI → CLV pipelines", "Built and maintained the feeds that delivered linked customer and "
                                       "transaction data into the model inputs."),
            ("The Customer Analytic Record", "Wrote the SQL for the staged build of the ~580-feature record, and "
                                             "partnered with the data scientists so the data the model learned "
                                             "from was accurate, complete and fit for purpose."),
        ]),
    ],
    "results_label": "Results",
    "results": [("4×", "increase in average customer spend"), ("$8M", "in marketing cost savings"),
                ("8", "segment-level survival models"), ("5 yrs", "of forward-looking value per customer")],
    "why_title": "From a report about the past to a forecast of value",
    "why": "CLV changed the question every customer team asked. Instead of “what did this customer spend?”, it "
           "became “what is this customer worth, and is that rising or falling?” That shift is what moved "
           "marketing toward the customers who mattered most, behind the 4× lift in average spend and $8M in "
           "savings.",
    "scale": [("~580", "features per customer in the CAR"), ("8", "behavioural segments"),
              ("5", "year forecast horizon"), ("Monthly", "re-scoring of every customer")],
}

# ---------------------------------------------------------------------------------------------
# Global Fleet KPI
# ---------------------------------------------------------------------------------------------
FLEET = {
    "repo": "Global-Fleet-BP",
    "eyebrow": "BP · Global Fleet KPI Report · KPI reporting",
    "title": "From Three Scoreboards to One Global View",
    "intro": "bp's fleet card business ran in three regions, and each one reported its operations in its own units, "
             "with its own definitions and its own time windows. The Global Fleet KPI Report unified that fragmented "
             "data into one view, so leaders could monitor asset utilisation and transportation demand, and guide "
             "high-value commercial and safety decisions across global operations.",
    "role": "Data Analyst",
    "note": "All figures, charts and examples on this page are illustrative. Volumes, margins and validation results "
            "have been replaced with fictitious numbers; no real BP data is shown. Only the headline results are "
            "reported outcomes.",
    "project_label": "The project",
    "project_title": "One trusted view of fleet across ESA, ANZ and the US",
    "overview": "The goal was one trusted view of fleet operations: how cards and volume are being used, how demand "
                "is trending in each region, and where commercial and safety attention should go. I owned the data "
                "behind the report end to end: bringing in three regions' data, standardising it into one model, and "
                "building the Power BI report.",
    "blocks": [
        ("h3", "The starting point: the same KPI meant three different things"),
        ("p", "Every region measured fleet its own way. Before anything could be compared, the differences had to "
              "be written down."),
        ("figure", "Three regions, three definitions", "How each region reported fleet",
         table(["KPI", "ESA", "ANZ", "US"], [
             ["Volume", "litres", "litres", "gallons"],
             ["Margin unit", "cents per litre", "cents per litre", "cents per gallon"],
             ["Contribution margin", "card contribution, local currency", "site waterfall + card margin − costs",
              "site margin × card volume − offers"],
             ["Active cards", "this month", "rolling 3 months", "this month"],
         ])),
        ("p", "Some regions also counted only bp-branded cards while others included partner and third-party "
              "networks. A report that ignored all this would have looked comparable and been wrong."),

        ("h3", "Why the totals lied"),
        ("p", "Put the raw monthly volumes next to each other and the story seems obvious. It isn't."),
        ("figure", "Raw volume vs. year-on-year change", "Illustrative month",
         table(["Region", "Monthly volume", "Unit", "YoY change"], [
             ["ESA", "500 million", "litres", "<b>+2.0%</b>"],
             ["ANZ", "185 million", "litres", "<b>−2.3%</b>"],
             ["US", "46 million", "gallons", "<b>−6.5%</b>"],
         ])),
        ("p", "ESA looks ten times the size of the US, but the units differ (a gallon is about 3.8 litres). The "
              "year-on-year column tells the real story: ESA is growing, ANZ is slipping, and the US is declining "
              "fastest. That's where attention should go."),

        ("h3", "The method: keep the definitions, make them visible"),
        ("p", "Rather than force one artificial definition on everyone, I mapped every region into the same "
              "structure, kept each region's own definition, and documented it. Unit and currency travel with the "
              "data as columns, so nothing is silently converted."),
        ("figure", "The KPI set", "Each one defined per region on the report's definitions page",
         chips(["Fleet volume", "Fleet contribution margin", "Active cards (1 & 3 month)",
                "Active customers (1 & 3 month)", "Average volume per card", "Fleet share of retail volume"])),
        ("p", "Making the definitions part of the report, not tribal knowledge, is what let leaders read every "
              "number with confidence."),

        ("h3", "Comparing like with like"),
        ("p", "Cross-region views use trends and year-on-year change, which stay meaningful when units don't match."),
        ("figure", "Fleet volume, indexed", "Each region indexed to January = 100",
         line([("ESA", C1, list(enumerate([100, 100.4, 100.1, 100.8, 101.0, 100.7, 101.3, 101.6, 101.2, 101.8, 101.7, 102.0]))),
               ("ANZ", C3, list(enumerate([100, 99.6, 99.9, 99.2, 98.9, 99.1, 98.6, 98.4, 98.7, 98.1, 97.9, 97.7]))),
               ("US", C2, list(enumerate([100, 99.3, 98.9, 98.0, 97.6, 97.1, 96.4, 95.9, 95.2, 94.6, 94.0, 93.5])))],
              [(0, "Jan"), (2, "Mar"), (4, "May"), (6, "Jul"), (8, "Sep"), (11, "Dec")],
              0, 11, 92, 104, [92, 96, 100, 104], f="{:.1f}")),
        ("p", "Indexed to the same starting point, three very different businesses can sit on one chart, and the "
              "region that needs attention stands out without any unit conversion."),

        ("h3", "Can we trust it?"),
        ("p", "Every refresh is reconciled against each region's own reporting before anyone relies on it."),
        ("figure", "KPI validation page", "Report vs. regional source, one month",
         table(["Region", "Report", "Regional source", "Difference", "Status"], [
             ["ESA", "500.0M litres", "499.6M litres", "0.08%", ok("Reconciled")],
             ["ANZ", "185.0M litres", "185.0M litres", "0.00%", ok("Reconciled")],
             ["US", "46.0M gallons", "46.3M gallons", "0.65%", warn("Under review")],
         ])),
        ("p", "“Which number is right?” stopped being a meeting topic: the validation page answers it before the "
              "meeting starts."),

        ("h3", "What I built"),
        ("callouts", [
            ("The common data model", "Fleet volume, margin, card and customer data from three regional systems, "
                                      "standardised into one model with unit and currency carried as attributes."),
            ("The Power BI report", "A global summary, by-region views, a definitions page and a KPI validation "
                                    "page, with monthly and year-to-month comparisons."),
        ]),
    ],
    "results_label": "Results",
    "results": [("85%", "less report preparation"), ("3×", "faster decisions"),
                ("3 → 1", "regions in one report")],
    "why_title": "One view to run global fleet operations",
    "why": "The point of the report was to give leaders one place to watch how fleet assets were being used and how "
           "transportation demand was moving, region by region, and to act on it. Getting there meant being honest "
           "about what each region's numbers meant and reconciling every figure to source. Once that was in place, "
           "the monthly pack no longer had to be assembled by hand, and commercial and safety decisions could be "
           "made from one trusted view, three times faster.",
    "scale": [("3", "regions: ESA, ANZ, US"), ("6", "core fleet KPIs"),
              ("4", "report pages incl. definitions & validation"), ("1", "common data model")],
}

# ---------------------------------------------------------------------------------------------
# Inventory Over & Short
# ---------------------------------------------------------------------------------------------
INVENTORY = {
    "repo": "Inventory-Over-Short-BP",
    "eyebrow": "BP · Inventory Over & Short · Loss prevention",
    "title": "From Audit Adjustments to Where Stock Is Lost",
    "intro": "Every convenience store loses some stock to theft, damage, spoilage and errors. bp's store audits "
             "measured it, but the results arrived as thousands of adjustments by store and category. Inventory "
             "Over & Short turned them into a ranked answer: which stores are losing stock fastest, in what, and "
             "whether it's getting better.",
    "role": "Data Analyst",
    "note": "All stores, figures, charts and examples on this page are illustrative. Values have been replaced with "
            "fictitious numbers; no real BP data is shown. Only the headline results are reported outcomes.",
    "project_label": "The project",
    "project_title": "Shrink, measured and managed across two brands",
    "overview": "The audits covered two convenience brands, Thorntons and ampm. I owned the data behind the report end "
                "to end: bringing in audits, item hierarchies, store attributes and sales, making stores comparable, "
                "and building the Power BI report loss-prevention teams worked from.",
    "blocks": [
        ("h3", "The starting point: a pile of adjustments, no priorities"),
        ("p", "An audit counts what's on the shelf and compares it with what the system says should be there. The "
              "difference is the over/short. The numbers existed; the answers didn't. Which stores are losing the "
              "most? Is it getting worse? Where should teams go first?"),
        ("figure", "Three stores, three audit intervals", "Illustrative audits",
         table(["Store", "Audit adjustment", "Days since last audit", "Loss per day"], [
             ["A", "−$3,000", "90", "−$33"], ["B", "−$2,000", "30", "<b>−$67</b>"], ["C", "−$1,200", "45", "−$27"],
         ])),
        ("p", "Stores were audited at different intervals, so the raw totals weren't comparable. Ranked by dollars, "
              "Store A looks worst."),

        ("h3", "Why the biggest number wasn't the biggest problem"),
        ("p", "Dividing each adjustment by the days since the previous audit puts every store on the same clock."),
        ("figure", "The same three stores, ranked two ways", "$ loss",
         '<div class="pair"><div><h4>By raw audit loss</h4>'
         + hbars([("Store A", 3000), ("Store B", 2000), ("Store C", 1200)], pre="$", highlight=("Store A",))
         + '</div><div><h4>By loss per day</h4>'
         + hbars([("Store B", 67), ("Store A", 33), ("Store C", 27)], pre="$", highlight=("Store B",))
         + "</div></div>"),
        ("p", "Store B is losing stock twice as fast as Store A, and should be visited first. One division changed "
              "where loss-prevention teams spent their week."),

        ("h3", "Two brands, one shelf"),
        ("p", "Thorntons and ampm used different names and structures for the same audit categories, so a cigarette "
              "loss in one brand didn't line up with the other. I mapped both into one department and category "
              "hierarchy, and flagged anything unmapped instead of dropping it."),
        ("figure", "Mapping audit categories across brands", "Illustrative rows",
         table(["Brand", "Source category", "Department", "Category"], [
             ["Thorntons", "Cigarettes Audit Adj", "Tobacco", "Cigarettes"],
             ["ampm", "CIGS", "Tobacco", "Cigarettes"],
             ["Thorntons", "Beer Audit Adjust", "Alcohol", "Beer"],
         ])),
        ("p", "With one hierarchy, a category trend means the same thing in every store, whichever brand is on the sign."),

        ("h3", "Who to visit first"),
        ("p", "Stores are ranked by loss per day and compared with their peers, so the ones furthest from normal "
              "stand out on their own."),
        ("figure", "Outlier stores", "Loss per day; amber = above the region's outlier line",
         hbars([("Store B", 67), ("Store F", 58), ("Store K", 51), ("Store D", 47), ("Store A", 33), ("Store H", 31),
                ("Store C", 27), ("Store J", 22)], pre="$", highlight=("Store B", "Store F", "Store K", "Store D"),
               ref=45, ref_label="Outlier line $45")),
        ("p", "Four stores sit clearly above the line. That's the visit list, ready the moment the audits land."),

        ("h3", "What's going missing"),
        ("p", "Drilling into a flagged store shows where the loss actually sits."),
        ("figure", "Store B: loss by category", "$ per day",
         hbars([("Cigarettes", 31), ("Beer", 16), ("Fresh food", 8), ("Candy", 5), ("Grocery", 4), ("Other", 3)],
               pre="$", highlight=("Cigarettes", "Beer"))),
        ("p", "Most of Store B's loss is in cigarettes and beer. That points to a targeted fix, such as tighter "
              "receiving checks or secure display, rather than a general store review."),

        ("h3", "What I built"),
        ("callouts", [
            ("The comparable store view", "Audits, item and department hierarchies, store attributes and sales for "
                                          "both brands, with categories standardised and every audit aligned to its "
                                          "period for loss per day."),
            ("The Power BI report", "Monthly analysis, item level, department, category and account time series, "
                                    "outlier stores, latest audits and loss per day."),
        ]),
    ],
    "results_label": "Results",
    "results": [("22%", "better inventory recovery"), ("4×", "faster prioritization"),
                ("2 → 1", "brands in one category hierarchy"), ("Per day", "loss, comparable across every store")],
    "why_title": "Loss-prevention effort, pointed where it counts",
    "why": "The audits were always there. What changed was the question they answered: not “here are this month's "
           "adjustments” but “here is where we're losing stock fastest, and in what.” Loss-prevention teams went "
           "to the right stores first, which is where the 22% better recovery came from.",
    "scale": [("2", "convenience brands: Thorntons and ampm"), ("1", "shared category hierarchy"),
              ("$/day", "the metric that made stores comparable"), ("Trend", "views by department, category and account")],
}

# ---------------------------------------------------------------------------------------------
# Fuel Margin Waterfall
# ---------------------------------------------------------------------------------------------
FUEL = {
    "repo": "Fuel-Margin-Waterfall-BP",
    "eyebrow": "BP · Fuel Margin Waterfall · Margin analytics",
    "title": "From One Margin Number to Every Cent Explained",
    "intro": "Fuel margin is reported in cents per gallon, and one cent across hundreds of millions of gallons is "
             "millions of dollars. But a single number hides everything behind it. The Fuel Margin Waterfall broke "
             "it into the drivers that move it, so pricing and supply teams could see not just what the margin "
             "was, but why.",
    "role": "Data Analyst",
    "note": "All figures, charts and examples on this page are illustrative. Prices, volumes and margins have been "
            "replaced with fictitious numbers; no real BP data is shown. Only the headline results are reported "
            "outcomes.",
    "project_label": "The project",
    "project_title": "A margin waterfall for the US fuel network",
    "overview": "Every margin conversation used to start with “let's go and find out why.” I owned the data behind the "
                "report end to end: bringing pricing, supply cost, invoice and volume data together, making every "
                "component add up, and building the Tableau waterfalls.",
    "blocks": [
        ("h3", "The starting point: a number with no story"),
        ("p", "When margin dropped, the business couldn't quickly tell whether the market had moved, the brand "
              "premium had changed, supply terms had worsened, or costs had shifted. Each has a different owner and "
              "a different fix."),
        ("figure", "The monthly question", "Illustrative month",
         '<div class="bignum"><div class="n"><small>Standard margin</small>7.5 <span>cpg</span>'
         '<em>▼ 1.0 cpg vs. last month · ≈ $5M</em></div><ul><li>But why?</li><li>Did the market move?</li>'
         '<li>Did the brand premium change?</li><li>Did supply terms get worse?</li><li>Did costs shift?</li></ul></div>'),
        ("p", "Without the breakdown, a one-cent drop was a $5 million mystery."),

        ("h3", "Why it was hard: every driver lived somewhere else"),
        ("p", "This wasn't a charting problem. Every piece of the margin came from a different system, at a different "
              "level of detail."),
        ("figure", "Where each driver came from", "Source and grain",
         table(["Source", "Grain", "Used for"], [
             ["Market reference prices", "terminal × day × grade", "Baseline cost"],
             ["Retail pump prices", "site × day × grade", "Revenue per gallon"],
             ["Supply invoices", "delivery", "Actual cost, invoiced volume"],
             ["Contract terms", "contract / site", "Terms impact"],
             ["Delivered volumes", "site × day × grade", "Weighting, volume variance"],
         ])),
        ("p", "None of these lined up naturally, and a waterfall only works if every bar adds up exactly to the total."),

        ("h3", "The method: one grain, volume-weighted"),
        ("p", "I aligned every input to site × day × grade, and stored each component in dollars rather than cents "
              "per gallon. Conversion happens only at the very end, so the parts always sum to the whole."),
        ("figure", "Why dollars first", "The rule that makes the waterfall reconcile",
         formula(["<b>Component CPG</b> = Σ component $ ÷ Σ gallons", "<b>not</b> the average of each site's CPG"])),
        ("p", "A simple average gives a small site the same weight as a large one. Volume-weighting keeps every bar "
              "honest, and each refresh is checked against the finance margin."),

        ("h3", "Reading the waterfall"),
        ("p", "Standard margin starts from what anyone could earn at the market's lowest rack price, then adds and "
              "subtracts each driver."),
        ("figure", "Standard margin waterfall", "One month, network view, cents per gallon",
         waterfall([("Market (rack low)", 7.0), ("Brand value", 10.0), ("bp premium", -8.5), ("Terms", -1.2),
                    ("Volume variance", 1.3), ("Others", -0.1), ("Standard margin", None, "total")])),
        ("p", "At 500 million gallons, 8.5 cents per gallon is $42.5 million of standard margin, and every cent of "
              "it is attributed to a driver."),

        ("h3", "What moved this month?"),
        ("p", "When margin fell by a cent, the waterfall showed which bar moved."),
        ("figure", "Change vs. last month, by driver", "cpg",
         dbars([("Market (rack low)", 0.2), ("Brand value", 0.0), ("bp premium", -1.1), ("Terms", -0.1),
                ("Volume variance", 0.0), ("Others", 0.0), ("Standard margin", -1.0)], highlight=("Standard margin",))),
        ("p", "Brand value held, so pricing wasn't the problem. The bp premium widened, so the conversation goes to "
              "supply, with the size of the gap already on the table."),

        ("h3", "Three layers of margin"),
        ("p", "The same approach extends beyond the fuel itself, to what bp's supply chain adds and to "
              "environmental and regulatory effects."),
        ("figure", "Standard → integrated → total margin", "Illustrative, cents per gallon",
         waterfall([("Standard", 8.5), ("Logistics", 1.4), ("Supply & trading", 0.9), ("Integrated", None, "total"),
                    ("Lag effect", -0.6), ("RINs", 1.1), ("Programme costs", -0.3), ("Total", None, "total")],
                   height=220)),
        ("p", "One view, three layers, and the same breakdown from the whole network down to a single site and grade."),

        ("h3", "What I built"),
        ("callouts", [
            ("The margin dataset", "Pricing, supply cost, invoice and volume data aligned to site × day × grade, "
                                   "volume-weighted, decomposed into drivers and reconciled to the total."),
            ("The Tableau waterfalls", "Monthly, year-to-date and year-on-year views, filterable from channel of "
                                       "trade down to individual site and fuel grade."),
        ]),
    ],
    "results_label": "Results",
    "results": [("2×", "faster root-cause analysis"), ("3", "margin layers in one view"),
                ("Every cent", "traced to a driver"), ("Site", "level drill-down, every grade")],
    "why_title": "Changing the question",
    "why": "The waterfall moved every margin conversation from “what was our margin?” to “what moved our margin, and "
           "who owns it?” Root causes that used to take an investigation were read straight off the chart, twice as "
           "fast, and supply decisions got sharper because the gap was already quantified.",
    "scale": [("6", "drivers in standard margin"), ("3", "layers: standard, integrated, total"),
              ("site × day", "× grade: the common grain"), ("3", "views: monthly, YTD, year-on-year")],
}

# Published story pages: each becomes index.html of its repo. New drafts go in narrative_drafts.py
# (gitignored) until Agnivesh approves them.
NARRATIVES = {n["repo"]: n for n in (SCI, CLV, FLEET, INVENTORY, FUEL)}
