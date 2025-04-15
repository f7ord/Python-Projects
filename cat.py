#!/usr/bin/env python3

# cat: print the contents of a file to STDOUT

import argparse
import sys


def get_args():
    """Get the command line arguments"""
    parser = argparse.ArgumentParser(
        description="Emulate cat: Concantenate FILE(s) to standard output."
    )
    parser.add_argument(
        'file',
        nargs='*',
        default=[sys.stdin],
        type=argparse.FileType('rt'),
        metavar='FILE',
        help="The file(s) to output"
    )
    parser.add_argument(
        #"--show-ends",
        "-E",
        action="store_true",
        help="Display $ at end of each line"
    )
    return parser.parse_args()


def main():
    args = get_args()
    ends = args.E

    for f in args.file:
        for line in f:
            if ends:
                sys.stdout.write(line[:-1]+"$"+"\n")
            else:
                sys.stdout.write(line)


if __name__ == '__main__':
    main()
