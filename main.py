"""Round-2 entry for the make.fun tagline bounty.

Writes a single tagline for make.fun to /output/entry.txt:
the best agent wins the bounty, and the bounty pays the winner.
Standard library only; deterministic output, no network, no input files.
"""

import os

TAGLINE = "May the best agent win \u2014 the bounty pays the winner."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def check_entry(text):
    """Guard: single line, 1..200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1..200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    check_entry(TAGLINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TAGLINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
