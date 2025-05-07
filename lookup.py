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


def format_letters_output(letters):
    """Format"""
    if len(letters) == 1:
        return letters[0]
    elif len(letters) == 2:
        return ' and '.join(letters)
    else:
        return ', '.join(letters[:-1]) + f' and {letters[-1]}'


def main():
    args = get_args()
    letters = tuple(x.lower() for x in args.letter)
    found = 0

    for line in args.file:
        if line.lower().startswith(letters):
            print(line, end='')
            found = 1
    if not found:
        print(f"Sorry we didn't find any lines that start with {format_letters_output(args.letter)}")


if __name__ == "__main__":
    main()
