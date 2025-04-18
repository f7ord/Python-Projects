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
        help="Print the first n lines (default: 10)",
    )

    return parser.parse_args()


def main():
    args = get_args()
    files = args.file
    n = args.lines
    
    for fh in files:
        if os.path.isfile(fh.name):
            print(f"==> {fh.name} <==")
        count = 0
        for line in fh:
            if count < n:
                print(line.rstrip())
                count += 1
        print() if files.index(fh) != (len(files)-1) else ''        
    

if __name__ == "__main__":
    main()
