#!/usr/bin/env python3
"""Write the six-word story entry to /output/entry.txt.

Exactly six words, 1-60 chars per the gate; the story must stand alone.
"""
import os

TEXT = "He won the war. Lost everything."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
