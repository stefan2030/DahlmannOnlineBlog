#!/usr/bin/env python3
"""Check generated internal HTML links and local assets."""
from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        wanted = "href" if tag in {"a", "link"} else "src" if tag in {"img", "script", "source"} else None
        if wanted:
            for key, value in attrs:
                if key == wanted and value:
                    self.values.append(value)


def resolves(source: Path, raw: str) -> bool:
    parts = urlsplit(raw)
    if parts.scheme or parts.netloc or raw.startswith(("mailto:", "tel:", "data:", "javascript:")):
        return True
    path = unquote(parts.path)
    if not path or path == "/":
        return (PUBLIC / "index.html").exists()
    target = (PUBLIC / path.lstrip("/")) if path.startswith("/") else (source.parent / path)
    candidates = [target]
    if path.endswith("/") or target.suffix == "":
        candidates.append(target / "index.html")
    return any(candidate.exists() for candidate in candidates)


def main() -> None:
    broken: list[str] = []
    checked = 0
    for page in sorted(PUBLIC.rglob("*.html")):
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        for raw in parser.values:
            checked += 1
            if not resolves(page, raw):
                broken.append(f"{page.relative_to(PUBLIC)} -> {raw}")
    if broken:
        print("link-check: FAIL", file=sys.stderr)
        print("\n".join(broken[:50]), file=sys.stderr)
        raise SystemExit(1)
    print(f"link-check: PASS ({len(list(PUBLIC.rglob('*.html')))} HTML files, {checked} references)")


if __name__ == "__main__":
    main()
