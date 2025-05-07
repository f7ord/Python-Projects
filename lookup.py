#!/usr/bin/env python3

"""Lookup"""

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Lookup: Look up lines of text from the "
        "input file that start with the letters provided in a "
        "case-insensitive fashion"
    )
    parser.add_argument(
        "file",
        type=argparse.FileType('rt'),
        help="Input file",
    )
    parser.add_argument(
        "letter",
        nargs="+",
        help="Letter(s)"
    )
    parser.add_argument(
        "-mc",
        "--matchcase",
        action="store_true",
        help="Match the case (make the search case-sensitive)"
    )
    parser.add_argument(
        "-e",
        action="store_true",
        help="Output a message if no line starts with any of `letters`"
    )

    return parser.parse_args()


def format_letters_output(letters):
    """Format the output of letters"""
    if len(letters) == 1:
        return letters[0]
    if len(letters) == 2:
        return ' and '.join(letters)
    return ', '.join(letters[:-1]) + f' or {letters[-1]}'


def main():
    args = get_args()
    matchcase = args.matchcase
    found_line = 0

    letters = tuple(args.letter) if matchcase else tuple(x.lower() for x in args.letter)

    for line in args.file:
        if matchcase:
            if line.startswith(letters):
                print(line, end='')
                found_line = 1
        else:
            if line.lower().startswith(letters):
                print(line, end='')
                found_line = 1
    if not found_line and args.e:
        print("Sorry we didn't find any lines that start with "
              f"{format_letters_output(args.letter)}")


if __name__ == "__main__":
    main()
