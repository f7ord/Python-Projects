#!/usr/bin/env python3

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Lookup: Look up lines of text from the "
        "input file that start with the letters provided in a "
        "case-insensitive fashion"
    )
    parser.add_argument(
        "letter",
        nargs="+",
        help="Letter(s)"
    )
    parser.add_argument(
        "file",
        type=argparse.FileType('rt'),
        help="Input file",
    )

    return parser.parse_args()


def main():
    args = get_args()
    letters = tuple(x.lower() for x in args.letter)
    file = args.file
    
    for line in file:
        if line.lower().startswith(letters):
            print(line, end='')


if __name__ == "__main__":
    main()
