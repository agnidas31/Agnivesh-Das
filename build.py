"""Build Agnivesh Das's portfolio website and résumé from content.py + site_content.py.

Usage
  python3 build.py site                       # hub index.html + public résumé PDF (no phone number)
  python3 build.py projects                   # case-study pages into each project repo checkout
  python3 build.py all                        # both of the above
  python3 build.py resume --phone "(xxx) xxx-xxxx" --out ~/Agnivesh_Das_Resume.pdf
                                              # private résumé with phone, written outside the repo

Project repos are expected as sibling checkouts of this repo, named in lowercase
(e.g. ../single-customer-identifier-bp). Override with --projects-root.
"""
import argparse
import copy
import datetime
import re
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

import content
import site_content

ROOT = Path(__file__).resolve().parent
env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))


def project_url(repo: str) -> str:
    return f"https://{site_content.SITE['github_user']}.github.io/{repo}/"


def live_projects():
    out = []
    for pr in site_content.PROJECTS:
        if pr.get("status") == "live":
            pr = dict(pr, url=project_url(pr["repo"]))
            out.append(pr)
    return out


def real_credentials():
    return [c for c in content.CREDENTIALS if not c.strip().startswith("[")]


def render_resume_pdf(out_path: Path, phone: str = "") -> None:
    from playwright.sync_api import sync_playwright

    profile = copy.deepcopy(content.PROFILE)
    profile["phone"] = phone
    html = env.get_template("resume.html").render(
        p=profile, summary=content.SUMMARY, signature=content.SIGNATURE,
        capabilities=content.CAPABILITIES, experience=content.EXPERIENCE,
        tech=content.TECH_ENVIRONMENT, education=content.EDUCATION, credentials=real_credentials(),
    )
    tmp = out_path.with_suffix(".html")
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto(tmp.resolve().as_uri())
        page.pdf(path=str(out_path), format="Letter", print_background=True, prefer_css_page_size=True)
        browser.close()
    tmp.unlink()
    print(f"résumé -> {out_path}")


def build_site() -> None:
    html = env.get_template("site.html").render(
        p=content.PROFILE, site=site_content.SITE, summary=content.SUMMARY,
        signature=content.SIGNATURE, capabilities=content.CAPABILITIES,
        experience=content.EXPERIENCE, education=content.EDUCATION,
        credentials=real_credentials(), projects=live_projects(), year=datetime.date.today().year,
    )
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("hub -> index.html")
    render_resume_pdf(ROOT / site_content.SITE["resume_file"], phone="")
    domain = site_content.SITE.get("custom_domain", "").strip()
    if domain:
        (ROOT / "CNAME").write_text(domain + "\n")
        print(f"CNAME -> {domain}")


def md_to_page(md_text: str, page: str, has_technical: bool) -> str:
    # House style: own labels, not borrowed ones.
    md_text = re.sub(r"^# Creative Solutions: ", "# ", md_text, flags=re.M)
    md_text = md_text.replace("Field-Tested Innovation · ", "Case Study · ")
    body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])
    title_m = re.search(r"^#\s+(.+)$", md_text, re.M)
    title = title_m.group(1).replace("Creative Solutions: ", "").strip() if title_m else "Case study"
    desc_m = re.search(r"^#\s+.+\n\n(.+)$", md_text, re.M)
    description = re.sub(r"[*_`]", "", desc_m.group(1)).strip() if desc_m else title
    return env.get_template("project.html").render(
        body=body, title=title, description=description[:300], author=content.PROFILE["name"],
        hub_url=site_content.SITE["base_url"], linkedin_url=site_content.SITE["linkedin_url"],
        page=page, has_technical=has_technical,
    )


def build_projects(projects_root: Path) -> None:
    for pr in live_projects():
        repo_dir = projects_root / pr["repo"].lower()
        if not repo_dir.exists():
            print(f"skip {pr['repo']}: no checkout at {repo_dir}")
            continue
        has_tech = bool(pr.get("technical")) and (repo_dir / pr["technical"]).exists()
        story = (repo_dir / pr["story"]).read_text(encoding="utf-8")
        (repo_dir / "index.html").write_text(md_to_page(story, "story", has_tech), encoding="utf-8")
        if has_tech:
            tech = (repo_dir / pr["technical"]).read_text(encoding="utf-8")
            (repo_dir / "technical.html").write_text(md_to_page(tech, "technical", True), encoding="utf-8")
        print(f"project -> {repo_dir.name}/index.html{' + technical.html' if has_tech else ''}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", choices=["site", "projects", "all", "resume"])
    ap.add_argument("--phone", default="")
    ap.add_argument("--out", default="")
    ap.add_argument("--projects-root", default=str(ROOT.parent))
    a = ap.parse_args()
    if a.target in ("site", "all"):
        build_site()
    if a.target in ("projects", "all"):
        build_projects(Path(a.projects_root))
    if a.target == "resume":
        out = Path(a.out).expanduser() if a.out else ROOT.parent / "Agnivesh_Das_Resume_private.pdf"
        if ROOT in out.resolve().parents:
            raise SystemExit("Refusing to write the private résumé inside the public repo.")
        render_resume_pdf(out, phone=a.phone)


if __name__ == "__main__":
    main()
