#!/usr/bin/env python3

# print the last n lines of a file

import argparse
import sys


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Emulate tail: Print the last n lines of a file"
    )
    parser.add_argument(
        "file",
        nargs="*",
        default=[sys.stdin],
        type=argparse.FileType('rt'),
        help="Input file(s)"
    )
    parser.add_argument(
        "-n",
        "--lines",
        default=10,
        type=str,
        help="Output the last n lines (default: 10); Use -n +NUM to output starting with line NUM"
    )

    return parser.parse_args()


def main():
    args = get_args()
    files = args.file
    start_line = True if args.lines[0] == '+' else False
    n = int(args.lines)

    for file in files:
        lines = file.readlines()
        if start_line:
            for line in lines[n-1:]:
                print(line.rstrip())
        else:
            for line in lines[-n:]:
                print(line.rstrip())
        file.close()


if __name__ == "__main__":
    main()
