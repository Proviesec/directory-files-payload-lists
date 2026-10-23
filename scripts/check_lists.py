#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check maintained wordlists for simple offline formatting errors."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGACY = {
    "directory-phpinfo-list.txt",  # Contains expression payloads as well as paths.
}
INCLUDES = (
    ("directory-best-sensitive-list.txt", "small-fast-list.txt"),
    ("small-fast-list.txt", "directory-full-list.txt"),
    ("top-1000-filenames.txt", "directory-full-list.txt"),
)


def main() -> int:
    problems = []
    checked = 0
    skipped = 0
    entries = {}
    for path in sorted(ROOT.rglob("*.txt")):
        name = path.relative_to(ROOT).as_posix()
        try:
            content = path.read_bytes().decode("utf-8")
        except UnicodeDecodeError as error:
            problems.append(f"{name}: invalid UTF-8: {error}")
            continue
        if not content.endswith("\n"):
            problems.append(f"{name}: missing final newline")
        if name in LEGACY:
            skipped += 1
            continue
        checked += 1
        seen = set()
        for number, line in enumerate(content.splitlines(), 1):
            if not line or line != line.strip() or "\r" in line:
                problems.append(f"{name}:{number}: blank or surrounding whitespace")
            if line in seen:
                problems.append(f"{name}:{number}: duplicate entry: {line!r}")
            if "\ufffd" in line:
                problems.append(f"{name}:{number}: replacement character in entry")
            seen.add(line)
        entries[name] = seen

    for smaller, larger in INCLUDES:
        missing = entries.get(smaller, set()) - entries.get(larger, set())
        if missing:
            examples = sorted(missing)[:5]
            problems.append(f"{smaller}: {len(missing)} entries missing from {larger}: {examples!r}")

    for problem in problems:
        print(problem)
    print(f"Checked {checked} lists for format and inclusion; {skipped} legacy exception; {len(problems)} issues.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
