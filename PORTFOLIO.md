# Portfolio builder: memory and operating rules

This file is the builder agent's memory. Read it fully before changing anything in this
repo or any project repo. Update the "Status" and "Decisions" sections whenever something changes.

## Who this is for

**Agnivesh Das**, Data Analytics & AI Leader, 13+ years (Walmart, BP, Nike, EmblemHealth).
Currently Manager, Strategic Insights & AI, Walmart Customer Engagement Services (Sep 2025 to present),
Bentonville, Arkansas. Targeting Director of Data Analytics level roles.

- Email: agnivesh.das@gmail.com
- LinkedIn: https://www.linkedin.com/in/agnivesh-das/
- GitHub: agnidas31
- Phone: **never** commit it to any repo. Only the private résumé gets it, via `--phone`.

## How the site is built (Victor Chowdhury's pattern)

- **Hub site**: this repo (`Agnivesh-Das`). `index.html` is generated, never hand-edited.
- **One repo per project**: each case study lives in its own public repo with a `README.md`,
  the Markdown write-ups, and a generated `index.html` (+ `technical.html` when there is a deep dive).
- **Single source of truth**:
  - `content.py`: everything shared with the résumé (profile, summary, signature metrics,
    capabilities, experience, tech environment, education). Edit here and both the résumé and site update.
  - `site_content.py`: site-only settings and the `PROJECTS` list (cards on the hub).
  - `templates/`: `site.html` (hub), `project.html` (case studies), `resume.html` (résumé PDF).
- **Build**: `python3 build.py all` (needs jinja2, markdown, playwright + Chromium).
  Project repos must be checked out as lowercase siblings of this repo (e.g. `../global-fleet-bp`).
- **Publish**: commit and push each changed repo; GitHub Pages serves `main` at the root.
  Project pages: `https://agnidas31.github.io/<Repo>/`.

## Writing rules (non-negotiable)

1. **Only confirmed facts.** Every metric, title, date, team and claim must come from Agnivesh or his
   source documents. If something is missing, ask; never invent outcomes, tools, team sizes or scope.
2. **Metrics are exact.** Use the numbers in `content.py` as written. Real results go in Impact
   sections; worked examples use clearly labelled illustrative numbers.
3. **Confidentiality.** No internal table names, URLs, colleague names, store numbers, account counts,
   internal margin rates or model scores unless Agnivesh explicitly approves publishing them.
   Walmart is his current employer: get explicit sign-off before publishing any Walmart material
   (given for the seven Walmart demo repos on 2026-10-20).
4. **Own voice.** Do not reuse Victor Chowdhury's wording, labels or results ("Creative Solutions",
   "Field-Tested Innovation", "not just tables", "without a request queue in between", his metrics).
   Similar structure is fine; copied phrasing is not.
5. **No placeholders on public pages.** Before publishing, grep for `[Confirm`, `[Add`, `[~`, `Draft note`.
6. **Résumé style**: bold lead-in with the headline result, then a colon and the "how", then a payoff.
   Signature cards: metric, label, tag ("Company · Project"), one plain sentence = action + second result.

## Case-study format (each project repo)

Story file (`<project>.md`): eyebrow line, `#` title, one-line hook, byline
(`Agnivesh Das · <title at the time> · <Company>`), then sections:
My Role · The Problem · The Constraint Nobody Was Naming · The Fix (controls + How it works) ·
Worked Example (illustrative, labelled) · Built to Scale (optional) · Why This Beat The Old Approach (table) ·
Impact (real confirmed numbers first) · footer line.
Technical file (optional): step-by-step method with formulas and short illustrative SQL/Python.

## Adding a new project (the builder workflow)

1. Collect source material from Agnivesh (docs, notes, dashboards) and his exact role and metrics.
2. Draft the story (and technical) Markdown in the format above; flag anything inferred.
3. Get his confirmation on facts and on what is OK to publish.
4. Make sure a repo exists (Agnivesh creates it; the agent cannot create repos) and attach it.
5. Add the Markdown + a one-line README to the project repo.
6. Add the project to `PROJECTS` in `site_content.py` with `status: "live"`.
7. If it changes the résumé (new metric or bullet), update `content.py`.
8. `python3 build.py all`, screenshot-check desktop and 390px mobile, grep for placeholders.
9. Commit and push the project repo and this repo. GitHub Pages must be switched on once per new repo
   by Agnivesh (the session's GitHub proxy blocks the Pages API): repo → Settings → Pages →
   "Deploy from a branch" → `main` / `/ (root)` → Save.

## Status

| Repo | State |
|---|---|
| Agnivesh-Das (hub) | Built and pushed; Pages to be switched on; custom domain pending |
| Single-Customer-Identifier-BP | Live (story + technical) (pushed; Pages to be switched on) |
| Customer-Lifetime-Value-BP | Live (story + technical) (pushed; Pages to be switched on) |
| Global-Fleet-BP | Live (pushed; Pages to be switched on) |
| Inventory-Over-Short-BP | Live (pushed; Pages to be switched on) |
| Fuel-Margin-Waterfall-BP | Live (pushed; Pages to be switched on) |
| AIsleOne, CRM-Analysis, Smart-Woofie, Appeasement-Analysis, Agent-Performance-Scorecard, Call-Complexity, Call-Complexity-vs-SSR (all -Walmart) | Live demos (synthetic data) shown in Selected work; each repo serves its own index.html. Agnivesh confirmed he built them (executed the work; his Director was Victor Chowdhury) and approved publishing without a credit line. Pages to be switched on. |
| bp_projects (private) | Original working copies of the BP write-ups |

## Decisions log

- Hub lives in `Agnivesh-Das`; Agnivesh wants a **custom domain** (name not chosen yet). When chosen:
  set `SITE["custom_domain"]` and `SITE["base_url"]`, update `PROFILE["portfolio"]` in `content.py`,
  rebuild (writes `CNAME`), and give him the DNS records to add.
- Public résumé PDF on the site has **no phone number**. Private résumé: `python3 build.py resume --phone "…" --out ~/…`.
- Visitor chat agent ("ask my AI", fit check) is **deferred**: needs a small serverless backend + API key.
- Résumé is allowed to run to 3 pages.
- Visual style (site, Oct 2026): layout modeled on Victor Chowdhury's site (navy hero, impact grid, about, tabbed
  "how I work" lenses, work-sample carousel, capabilities, career timeline, contact band), written from scratch.
  Navy `#172340` base with a **copper accent `#b4541a`** (Victor uses teal), Source Serif 4 headings, Inter body.
  The résumé PDF still uses teal `#0e5a63` with Lora/Carlito; align it if Agnivesh asks.

## Open items

- Custom domain name.
- Walmart case-study material and sign-off.
- Certifications (none listed yet; `CREDENTIALS` hides placeholders automatically).
- Fuel Margin Waterfall: integrated/environment margin definitions are a reading of dashboard labels; confirm with Agnivesh.
- EmblemHealth: confirm "Led" vs "Ran" for user acceptance testing.
