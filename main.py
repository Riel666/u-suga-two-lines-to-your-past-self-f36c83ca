"""Two lines: line 1 warns my past self about one specific moment in a single sentence; line 2 says in one sentence why that moment mattered and what changed because of it.

The program writes exactly those lines and nothing else to /output/entry.txt.
"""

import os

TEXT = "Do not hit send on that 2 a.m. email — you are angry, not right, and tomorrow morning has no undo button.\nIt mattered because that one unsent email saved a friendship, and ever since I write angry drafts at night and read them again after breakfast."


def main():
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
