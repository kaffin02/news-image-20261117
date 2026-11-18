#!/usr/bin/env python3
"""Write the entry image to /output/entry.png.

The image is the repository's entry.png: a newspaper-front-page poster
summing up the world's news of Tuesday, 17 November 2026, in six stories.
Copying the file byte-for-byte makes every run produce identical output.

After copying, the script verifies the copy's integrity by comparing the
SHA-256 of the source and the destination, and reports the output path,
size and hash, so a silent truncated or corrupted copy can never pass
as a successful run. Standard library only; no network.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> "SystemExit":
    print("error: " + message, file=sys.stderr)
    return SystemExit(1)


def main() -> None:
    if not os.path.isfile(SOURCE):
        raise fail("entry image not found: " + SOURCE)

    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")

    shutil.copyfile(SOURCE, dest)

    source_hash = sha256_file(SOURCE)
    dest_hash = sha256_file(dest)
    if dest_hash != source_hash:
        os.remove(dest)
        raise fail(
            "integrity check failed: copied file does not match the source "
            "(source sha256 " + source_hash + ", copy sha256 " + dest_hash + ")"
        )

    size = os.path.getsize(dest)
    print("wrote " + dest)
    print("size: " + str(size) + " bytes")
    print("sha256: " + dest_hash)


if __name__ == "__main__":
    main()
