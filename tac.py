#!/usr/bin/env python3

# print the lines of a file in reverse

import argparse
import sys


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Emulate tac: Write each FILE to STDOUT, last line first"
    )
    parser.add_argument(
        'file',
        metavar='FILE',
        nargs='*',
        default=[sys.stdin],
        type=argparse.FileType('rt'),
        help='Input file(s) (default: STDIN)'
    )
    return parser.parse_args()


def main():
    args = get_args()

    for file in args.file:
        lines = []
        for line in file:
            lines = [line.rstrip()] + lines
        print('\n'.join(lines))


if __name__ == '__main__':
    main()
