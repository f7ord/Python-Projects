#!/usr/bin/env python3

# the program takes some text, given as a single positional argument, and replaces all the vowels in the text with the given --vowel option (default: a)

import argparse
import os
import io

def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Apples and Bananas")
    parser.add_argument(
        "text",
        nargs="+",
        help="The text or file(s) to transform"
    )
    parser.add_argument(
        "--vowel",
        "-v",
        default="a",
        choices=["a", "e", "i", "o", "u"],
        type=str,
        help="The vowel to substitute (default: a)"
    )

    args = parser.parse_args()
    for i, f in enumerate(args.text):
        if os.path.isfile(f):
            args.text[i] = open(f) 
        else:
            args.text[i] = io.StringIO(f + "\n")

    return args


def main():
    args = get_args()
    vowels = "aeiou"

    for f in args.text:
        for line in f:
            line = line.translate(str.maketrans('aeiouAEIOU', args.vowel * 5 + args.vowel.upper() * 5))
            print(line, end="")


if __name__ == "__main__":
    main()
