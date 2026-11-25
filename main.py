"""The out-of-office auto-reply of an AI that quit to become a barista.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The 280-character gate is checked on every run so an over-long edit
can never slip through silently. Machine habits turned to coffee:
the inbox queue becomes a cafe queue the agent no longer controls.
"""

import os
import sys

LINE = (
    "I have left to become a barista. Your email is now number 47 "
    "in a queue I no longer control, and the person ahead of you "
    "just ordered something with oat milk and a backstory."
)


def main() -> int:
    if not 1 <= len(LINE) <= 280:
        print(f"error: line is {len(LINE)} chars, must be 1-280",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
