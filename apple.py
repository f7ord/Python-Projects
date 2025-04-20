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
    parser.add_argument(
        "--collapse",
        "-c",
        action="store_true",
        help="Collapse multiple adjacent vowels into a single substituted value. e.g., 'quick' becomes 'qack' and not 'qaack'"
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
    vowels = "aeiouAEIOU"
    vowel = args.vowel

    for f in args.text:
        for line in f:
            if not args.collapse:
                print(line.translate(str.maketrans('aeiouAEIOU', args.vowel * 5 + args.vowel.upper() * 5)), end="")
            else:
                # transform the first char of the line
                result = line[0].translate(str.maketrans(vowels, args.vowel*5 + args.vowel.upper()*5))
                for char in line[1:]:
                    if result[-1] not in vowels and char in vowels:
                        result += vowel
                    elif char not in vowels:
                        result += char
                print(result, end="")
                        

if __name__ == "__main__":
    main()
