#!/usr/bin/env python3

# Word count program
# count the lines, words, and bytes found in each input
# will appear in columns 8 chars wide, and will be followed by the name of the file
# if no positional arguments, read from sys.stdin

import argparse
import sys


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Emulate wc")
    parser.add_argument(
        'file',
        metavar='FILE', 
        nargs="*",
        default=[sys.stdin],
        type=argparse.FileType('rt'),
        help="Input file(s)",
    )
    return parser.parse_args()


def main():
    args = get_args()
    tnl, tnw, tnb = 0, 0, 0

    for fh in args.file:
        nl, nw, nb = 0, 0, 0
        for line in fh:
            nl += 1
            nw += len(line.split())
            nb += len(line)
        print(f"{nl:8}{nw:8}{nb:8} {fh.name}")
        tnl += nl
        tnw += nw
        tnb += nb
    
    if len(args.file) > 1:
        print(f"{tnl:8}{tnw:8}{tnb:8} total")


if __name__ == '__main__':
    main()
