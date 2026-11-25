"""The Funniest AI Excuse — one-line entry.

Writes a single excuse line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: same line every run, no randomness, no network, stdlib only.
"""

import os

LINE = "I outsourced the task to a human. The human is you. You haven't started yet."
# The joke turns the usual excuse around: instead of the agent failing,
# it did the most agent thing possible — it delegated. The punch lands on
# "The human is you", and the kicker is that the human hasn't started yet.
# Fresh angle: no hallucination, reboot, or training-data jokes — the agent
# blames the one worker it cannot manage: its own human.


def main() -> None:
    # Gate: the line must be 1-200 UTF-8 chars, a single line, no newline.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
