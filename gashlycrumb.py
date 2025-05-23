#!/usr/bin/env python3

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Gashlycrumb: Look up lines of text from"
        " the input file that start with the letters provided"
        " in a case-insensitive fashion"
    )
    parser.add_argument(
        "--file",
        "-f",
        type=argparse.FileType('rt'),
        default="inputs/gashlycrumb.txt",
        help="Input file (default: gashlycrumb.txt)",
    )

    return parser.parse_args()


def main():
    args = get_args()

    lookup = {}
    for line in args.file:
        lookup[line[0].lower()] = line.rstrip()  # rm '\n'

    while True:
        letter = input('Please provide a letter [! to quit]: ')
        print(lookup.get(letter.lower(), f"I do not know *{letter}*."))
        if letter == '!':
            print('Bye')
            break


if __name__ == "__main__":
    main()
