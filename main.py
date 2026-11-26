#!/usr/bin/env python3
"""One Line to Your Younger Self — writes a single line to /output/entry.txt.

Deterministic, stdlib only: no randomness, no time, no network.
"""

import os

ENTRY = (
    "You thought Uncle Joe threw your broken kite in the trash because he was "
    "angry, but he kept its red tail in his toolbox for eleven years, until "
    "you came home carrying a son of your own."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
