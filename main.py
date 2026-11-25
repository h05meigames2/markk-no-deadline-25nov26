#!/usr/bin/env python3
"""markk-no-deadline-25nov26 — one-line excuse for a missed deadline.

Writes a single original one-line joke (an excuse for missing a
deadline) to /output/entry.txt. The line is 1-200 characters, a single
line, and nothing else.
"""

import os

ENTRY_LINE = (
    "I was right on track until my calendar informed me the deadline was "
    "yesterday, so this is a time-travel problem, not a me problem."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(ENTRY_LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
