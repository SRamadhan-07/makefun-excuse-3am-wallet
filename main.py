"""The 3 AM Excuse - a hardware wallet refuses to sign.

Writes one line to /output/entry.txt: the wallet's own excuse for
refusing a signature at 3 a.m., when every signature feels like a
confession its half-asleep owner is in no state to make.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Refused: at 3 a.m. every signature is a confession, "
    "and you, sir, are clearly not awake enough to make one."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate allows a single line of 1 to 200 characters; guard the
    # invariant here so the entry can never drift out of bounds.
    assert "\n" not in ENTRY_TEXT
    assert 1 <= len(ENTRY_TEXT) <= 200
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
