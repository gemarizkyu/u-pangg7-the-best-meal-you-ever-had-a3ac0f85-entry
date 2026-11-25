#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence (at most 200 characters) about the best meal
I ever had to /output/entry.txt.

The sentence is fixed and deterministic: no clock, no randomness,
no network, no model call. The program only writes the text below.
"""

import os
from pathlib import Path

SENTENCE = (
    "At my grandmother's table in Bogor, rain on the tin roof, "
    "I ate rendang that fell apart on the spoon, its steam smelling "
    "of coconut and woodsmoke, and for a moment I was seven again."
)


def main() -> None:
    # Gate mirror: the entry must be 1-200 characters of real text.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text, "entry must not be only white space"
    output_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
