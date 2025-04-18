#!/usr/bin/env python3

# print the first n lines of a file

import argparse
import sys
import os


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Emulate head: print the first n lines of a file"
    )
    parser.add_argument(
        "file",
        nargs="*",
        default=[sys.stdin],
        type=argparse.FileType('rt'),
        help="Input file(s)"
    )
    parser.add_argument(
        "--lines",
        "-n",
        default=10,
        type=int,
        help="Print the first n lines (default: 10); if negative, print all but the last n lines of each file",
    )

    return parser.parse_args()


def main():
    args = get_args()
    files = args.file
    n = args.lines
    
    for fh in files:
        lines = fh.readlines()
        num_lines = len(lines) - 1
        count = 0

        if len(files) > 1 and os.path.isfile(fh.name):
            print(f"==> {fh.name} <==")
        if n > 0:
            for line in lines:
                if count < n:
                    print(line.rstrip())
                    count += 1
        else:
            for line in lines:
                if count <= (num_lines + n):
                    print(line.rstrip())
                    count += 1
        print() if fh.name != files[-1].name else ''

if __name__ == "__main__":
    main()
