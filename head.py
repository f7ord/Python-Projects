#!/usr/bin/env python3

import argparse
import sys


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
        "--quiet",
        "--silent",
        "-q",
        action="store_true",
        help="Don't print headers giving file names",
    )
    print_group = parser.add_mutually_exclusive_group()
    print_group.add_argument(
        "--lines",
        "-n",
        help="Print the first n lines (default: 10); if negative, print all but the last n lines of each file",
    )
    print_group.add_argument(
        "--bytes",
        "-c",
        help="Print the first c bytes of each file; if negative, print all but the last c bytes of each file",
    )
    
    return parser.parse_args()


def main():
    args = get_args()
    files = args.file
    n = args.lines if args.lines else "10"
    c = args.bytes
    active = "c" if c else "n"

    for fh in files:
        lines = fh.readlines()
        num_lines = len(lines) - 1
        count = 0

        # print or not print file name headers
        if not args.quiet and len(files) > 1:
            print(f"==> {fh.name} <==")
        
        # print the first n lines or all but the last n lines
        if active == "n":
            if int(n) >= 0 and n[0] != '-':
                for line in lines:
                    if count < int(n):
                        print(line.rstrip())
                        count += 1
            else:
                for line in lines:
                    if count <= (num_lines + int(n)):
                        print(line.rstrip())
                        count += 1

        # print the first c bytes or all but the last c chars
        nchars = sum(len(line) for line in lines) - 1
        nbytes = 0

        if active == "c": # if user passed a value for c
            if int(c) >= 0 and c[0] != '-':
                for line in lines:
                    for char in line:
                        if nbytes < int(c):
                            print(char, end="")
                            nbytes += 1
            else:
                for line in lines:
                    for char in line:
                        if nbytes <= (nchars + int(c)):
                            print(char, end="")
                            nbytes += 1
        
        print() if fh.name != files[-1].name else ''
        fh.close()


if __name__ == "__main__":
    main()
