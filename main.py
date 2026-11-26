#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — one-line make.fun entry.

Writes a single voicemail greeting, recorded by a cat on behalf of its
owner, to /output/entry.txt. Deterministic, offline, stdlib only.
"""

import os

# The greeting: an imperious cat who dispatched its human on a 4 a.m.
# salmon run and now screens every incoming message by sitting on it.
# One line, well under the competition's 120-character cap.
GREETING = (
    "This is the cat. My human is out buying salmon; I woke him at 4 a.m. "
    "Leave a message; if it's urgent, I'll sit on it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(GREETING)


if __name__ == "__main__":
    main()
