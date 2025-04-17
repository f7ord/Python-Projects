#!/usr/bin/env python3

# Count the number of times each word is seen in a document
# add a flag to make the count case-insensitive
# add a flag to sort the output

import argparse
import pprint as pp
import sys

def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Count: count the number of times each word in the given document occurs"
    )
    parser.add_argument(
        "file",
        nargs="*",
        default=[sys.stdin],
        type=argparse.FileType('rt'),
        help="Input file(s)",
    )

    return parser.parse_args()


def main():
    args = get_args()

    for fh in args.file:
        output = {}
        for line in fh:
            for word in line.split():
                output[word] = output.get(word, 0) + 1
        print(fh.name.upper().center(30))
        pp.pp(output)
        print()


if __name__ == "__main__":
    main()
