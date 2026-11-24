#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the
modern internet to a time traveler who has just stepped out of the
year 1800, using only things a person from that year could picture:
letters, roads, horses, and libraries. No word in the sentence was
coined after the traveler's time.
"""

import os

SENTENCE = (
    "Imagine the whole world's letters flying along invisible roads "
    "faster than a horse could ever run, and the books of a thousand "
    "libraries open before you without leaving home."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
