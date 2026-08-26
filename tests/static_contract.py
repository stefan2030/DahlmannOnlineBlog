#!/usr/bin/env python3
"""Static acceptance checks for the generated Hugo site."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
POSTS = sorted((ROOT / "content" / "posts").glob("*.md"))
REQUIRED = ("content_type", "audience", "last_reviewed", "school_status", "categories")


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def front_matter(text: str) -> str:
    check(text.startswith("---\n"), "YAML front matter expected")
    return text.split("---", 2)[1]


def main() -> None:
    check(len(POSTS) == 5, f"expected 5 source posts, got {len(POSTS)}")
    for path in POSTS:
        text = path.read_text(encoding="utf-8")
        fm = front_matter(text)
        for key in REQUIRED:
            check(re.search(rf"(?m)^{re.escape(key)}:", fm) is not None, f"{path.name}: missing {key}")
        check("## Kurzüberblick" in text, f"{path.name}: missing Kurzüberblick")
        check("Offizielle Schulanleitung" not in fm, f"{path.name}: must not claim official status")
    all_content = "\n".join(path.read_text(encoding="utf-8") for path in POSTS)
    check("Schule digital unabgängig" not in all_content, "taxonomy typo remains")

    for path in (ROOT / "content" / "anleitungen.md", ROOT / "content" / "impressum.md", ROOT / "content" / "datenschutz.md"):
        check(path.exists(), f"missing {path.relative_to(ROOT)}")
    for icon in ("favicon.ico", "favicon-16x16.png", "favicon-32x32.png", "apple-touch-icon.png", "safari-pinned-tab.svg"):
        check((ROOT / "static" / icon).exists(), f"missing static/{icon}")

    config = (ROOT / "hugo.toml").read_text(encoding="utf-8")
    check("locale = 'de-DE'" in config, "Hugo locale not configured")
    check("languageCode" not in config, "deprecated languageCode remains")

    check(PUBLIC.exists(), "public missing; run scripts/build.sh")
    check(not (PUBLIC / "posts" / "my-first-post").exists(), "stale my-first-post survived clean build")
    home = (PUBLIC / "index.html").read_text(encoding="utf-8")
    for marker in ("Anleitungen für Kolleginnen und Kollegen", "/anleitungen/", "/impressum/", "/datenschutz/"):
        check(marker in home, f"homepage/footer missing {marker}")
    search = (PUBLIC / "suche" / "index.html").read_text(encoding="utf-8")
    check(re.search(r'id=["\']?search["\']?', search) is not None and "pagefind-ui.js" in search, "Pagefind UI missing")
    check('id="searchInput"' not in search, "obsolete PaperMod/Fuse search remains")

    post_pages = sorted((PUBLIC / "posts").glob("*/index.html"))
    check(len(post_pages) == 5, f"expected 5 generated canonical post pages, got {len(post_pages)}")
    for page in post_pages:
        html = page.read_text(encoding="utf-8")
        check('data-pagefind-body' in html, f"{page}: article is not Pagefind body")
        check(re.search(r'class=["\']?knowledge-meta(?:["\'\s>])', html) is not None, f"{page}: visible metadata badges missing")
        check(re.search(r'<script[^>]+src=["\']?https://giscus\.app/client\.js', html) is None, f"{page}: Giscus loads before consent")
        check(re.search(r'<iframe[^>]+src=["\']?https://(?:www\.)?youtube(?:-nocookie)?\.com/embed', html) is None, f"{page}: YouTube iframe loads before consent")
    for page in (PUBLIC / "archives" / "index.html", PUBLIC / "tags" / "index.html", PUBLIC / "categories" / "index.html"):
        html = page.read_text(encoding="utf-8")
        check('data-pagefind-body' not in html, f"{page}: taxonomy/archive must not be indexed")

    print(f"static-contract: PASS ({len(POSTS)} posts, {len(post_pages)} generated post pages)")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"static-contract: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
