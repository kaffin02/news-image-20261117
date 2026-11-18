#!/usr/bin/env python3
"""Write the entry image to /output/entry.png.

The image is the repository's entry.png: a newspaper-front-page poster
summing up the world's news of Tuesday, 17 November 2026, in six stories.
Copying the file byte-for-byte makes every run produce identical output.
Standard library only; no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
