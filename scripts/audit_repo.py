#!/usr/bin/env python3
"""Static audit for the interview knowledge base.

Checks:
1. broken relative Markdown links;
2. top-level knowledge modules without README.md;
3. duplicate normalized question titles;
4. unresolved TODO/TBD markers;
5. basic module/question statistics.

No third-party dependencies.
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
IGNORE_DIRS = {".git", ".github", "scripts", "__pycache__"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
Q_RE = re.compile(r"^#{1,4}\s+(?:Q\s*\d+[\.、:]?\s*)?(.+?)\s*$", re.M | re.I)
EXPLICIT_Q_RE = re.compile(r"^#{1,4}\s+Q\s*\d+[\.、:]?\s*(.+?)\s*$", re.M | re.I)
TODO_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.I)


def md_files():
    return [p for p in ROOT.rglob("*.md") if not any(part in IGNORE_DIRS for part in p.parts)]


def normalize_title(s: str) -> str:
    s = re.sub(r"[`*_~]", "", s)
    s = re.sub(r"\[[^\]]+\]\([^)]*\)", "", s)
    s = re.sub(r"[^0-9a-zA-Z\u4e00-\u9fff]+", "", s).lower()
    return s


def check_links(files):
    broken = []
    for p in files:
        text = p.read_text("utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (p.parent / target).resolve()
            if resolved.is_dir():
                resolved = resolved / "README.md"
            if not resolved.exists():
                broken.append((p.relative_to(ROOT), raw))
    return broken


def check_module_readmes():
    missing = []
    for p in ROOT.iterdir():
        if not p.is_dir() or p.name in IGNORE_DIRS or p.name.startswith("."):
            continue
        if re.match(r"^\d", p.name) and not (p / "README.md").exists():
            missing.append(p.name)
    return missing


def question_stats(files):
    titles = defaultdict(list)
    explicit_q = 0
    standalone_q = 0
    for p in files:
        text = p.read_text("utf-8")
        qs = EXPLICIT_Q_RE.findall(text)
        explicit_q += len(qs)
        for title in qs:
            key = normalize_title(title)
            if key:
                titles[key].append((p.relative_to(ROOT), title.strip()))
        if p.name != "README.md":
            m = re.search(r"^#\s+(.+)$", text, re.M)
            if m:
                standalone_q += 1
                key = normalize_title(m.group(1))
                if key:
                    titles[key].append((p.relative_to(ROOT), m.group(1).strip()))
    duplicates = {k: v for k, v in titles.items() if len({str(x[0]) for x in v}) > 1}
    return explicit_q, standalone_q, duplicates


def todo_markers(files):
    out = []
    for p in files:
        for i, line in enumerate(p.read_text("utf-8").splitlines(), 1):
            if TODO_RE.search(line):
                out.append((p.relative_to(ROOT), i, line.strip()))
    return out


def module_stats(files):
    c = Counter()
    for p in files:
        rel = p.relative_to(ROOT)
        c[rel.parts[0]] += 1
    return c


def main():
    files = md_files()
    broken = check_links(files)
    missing = check_module_readmes()
    explicit_q, standalone_q, duplicates = question_stats(files)
    todos = todo_markers(files)
    stats = module_stats(files)

    print("=== Knowledge Base Audit ===")
    print(f"Markdown files: {len(files)}")
    print(f"Explicit Q headings: {explicit_q}")
    print(f"Standalone topic files: {standalone_q}")
    print(f"Broken relative links: {len(broken)}")
    print(f"Top-level modules missing README: {len(missing)}")
    print(f"Duplicate normalized question titles: {len(duplicates)}")
    print(f"TODO/TBD/FIXME markers: {len(todos)}")
    print("\nTop-level Markdown file counts:")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")

    if broken:
        print("\nBROKEN LINKS:")
        for p, link in broken:
            print(f"  {p}: {link}")
    if missing:
        print("\nMISSING README:")
        for x in missing:
            print(f"  {x}")
    if duplicates:
        print("\nDUPLICATE QUESTION TITLES (warning):")
        for entries in list(duplicates.values())[:50]:
            print("  - " + " | ".join(f"{p}: {t}" for p, t in entries))
    if todos:
        print("\nUNRESOLVED MARKERS (warning):")
        for p, i, line in todos[:100]:
            print(f"  {p}:{i}: {line}")

    # Broken navigation and missing module README are hard failures.
    # Duplicate titles are warnings because the same concept can intentionally
    # appear in a high-frequency review index and a detailed module.
    if broken or missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
