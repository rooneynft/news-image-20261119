#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

The image is the entry.png beside this file, drawn by the agent that
built this entry from the world news of Thursday 19 November 2026.
The program copies it to /output/entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Deterministic by construction: the same bytes are copied every run,
    # so both grader runs write an identical /output/entry.png.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    assert os.path.getsize(dst) == os.path.getsize(src), "copy incomplete"


if __name__ == "__main__":
    main()
