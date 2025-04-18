#!/usr/bin/env python3

# Count the number of times each word is seen in a document

# add a flag to sort the output k or v

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
    parser.add_argument(
        # "--ignore-case",
        "-c",
        action="store_true",
        help="Ignore the case of the words"
    )

    return parser.parse_args()


def main():
    args = get_args()

    for fh in args.file:
        output = {}
        for line in fh:
            words = [word.lower() if args.c else word for word in line.split()]
            for word in words:
                output[word] = output.get(word, 0) + 1
        print(f"==> {fh.name} <==")
        pp.pp(output)
        print() if args.file.index(fh) != (len(args.file)-1) else ''


if __name__ == "__main__":
    main()
