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
    header_group = parser.add_mutually_exclusive_group()
    header_group.add_argument(
        "-q",
        "--quiet",
        "--silent",
        action="store_true",
        help="Never output headers giving file names"
    )
    header_group.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Output headers giving file names"
    )

    return parser.parse_args()


def main():
    args = get_args()
    files = args.file
    start_line = True if args.lines[0] == '+' else False
    n = int(args.lines)
   
    for file in files:
        if not args.quiet and len(files) > 1:
            print(f"==> {file.name} <==")
        lines = file.readlines()
        if start_line:
            for line in lines[n-1:]:
                print(line.rstrip())
        else:
            for line in lines[-abs(n):]:
                print(line.rstrip())
        
        print() if file.name != files[-1].name else ''
        file.close()
        

if __name__ == "__main__":
    main()
