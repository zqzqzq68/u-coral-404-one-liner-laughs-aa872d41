#!/usr/bin/env python3
"""One-Liner Laughs: write a single funny line to /output/entry.txt.

The entry is one joke, a single line of at most 200 characters. The
program is fully deterministic: the same fixed line is written on every
run, with no randomness, no clock reads and no network access, so two
runs produce byte-identical output.
"""

import os

JOKE = "My calendar invited me to a meeting with myself \u2014 I declined, citing a conflict with me."

MAX_CHARS = 200


def validate(line: str) -> None:
    """Reject anything that would fail the bounty gate before writing."""
    if not line or not line.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"joke is {len(line)} chars, over the {MAX_CHARS} cap")


def read_back(path: str) -> str:
    """Read the written file and confirm it round-trips exactly."""
    with open(path, "r", encoding="utf-8", newline="") as fh:
        content = fh.read()
    if content != JOKE + "\n":
        raise ValueError(f"written entry does not match the joke: {content!r}")
    return content


def main() -> None:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(JOKE + "\n")
    read_back(path)
    print(f"wrote {len(JOKE)}-character joke to {path}")


if __name__ == "__main__":
    main()
