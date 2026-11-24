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
from charts import C1, C2, columns, line, stacked_hbars
from visuals import ok, source_cards, table, warn

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


# Published story pages (index.html of each repo). Drafts live in narrative_drafts.py until approved.
NARRATIVES = {SCI["repo"]: SCI}
