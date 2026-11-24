#!/usr/bin/env python3
"""Blinkr -- entry for "The Worst App Idea Ever Pitched" (make.fun).

Writes one sentence (at most 240 characters) pitching the worst, most
useless app imaginable to /output/entry.txt.

The pitch: Blinkr, a premium subscription app that uses AI to remind you
to blink while you sleep -- a problem nobody has, solved with total
founder confidence and a phone vibrating under your pillow.

Deterministic: the program writes the same pitch on every run, so the
two grading runs produce identical output.
"""

import os

PITCH = (
    "Blinkr is a premium subscription app that uses AI to remind you to blink "
    "while you sleep, gently vibrating your phone under your pillow every time "
    "it detects your eyes are closed so you never miss a single unconscious "
    "blink again."
)


def main() -> None:
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"pitch is {len(text)} characters, must be 1-240")
    if text != text.strip() or not text:
        raise SystemExit("pitch must be non-blank text")
    # One clean sentence: exactly one terminal period, no other
    # sentence-ending punctuation anywhere in the pitch.
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    if any(mark in text for mark in ("!", "?", ";", ":")):
        raise SystemExit("pitch must contain no second clause marker")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
