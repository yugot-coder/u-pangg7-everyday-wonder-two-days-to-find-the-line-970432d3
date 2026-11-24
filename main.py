#!/usr/bin/env python3
"""Everyday Wonder — write one sentence of everyday wonder to entry.txt.

Standard library only. Deterministic: the same line on every run.
"""

import os

LINE = (
    "On rainy mornings my houseplant leans away from the window and toward me, "
    "as if the sun had called in sick and I would have to be the light instead."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line length {len(LINE)} outside 1..200 characters")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)

    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != LINE:
        raise SystemExit("read-back verification failed: entry.txt differs from LINE")
    if not 1 <= len(written) <= 200:
        raise SystemExit(f"written length {len(written)} outside 1..200 characters")


if __name__ == "__main__":
    main()
