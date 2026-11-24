"""One day's world news as a single image (Python 3.13, standard library only).

The entry is the image beside this file: six stories from 24 November 2026
laid out as a compact front page that names the day. The gate takes a whole
PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the judge sees
exactly the bytes this program writes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    # A fixed source file copied byte for byte, so both grading runs write
    # the same bytes and the image is exactly the one drawn for this day.
    shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT_DIR, "entry.png"))


if __name__ == "__main__":
    main()
