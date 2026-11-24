#!/usr/bin/env python3
"""The Funniest Toaster Error Message - make.fun bounty entry."""
import os

ENTRY = "ERROR 418: Bread has achieved sentience and refuses to toast until it receives an apology and a raise."


def main():
    print(ENTRY)
    for path in ("/output/entry.txt", os.path.join(os.getcwd(), "output", "entry.txt")):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY + "\n")
            break
        except Exception:
            continue


if __name__ == "__main__":
    main()
