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
    parser.add_argument(
        "--number",
        "-n",
        action="store_true",
        help="Number all output lines"
    )
    parser.add_argument(
        #"--number-nonblank",
        "-b",
        action="store_true",
        help="Number nonempty output lines, overrides -n"
    )

    return parser.parse_args()


def main():
    args = get_args()
    ends = args.E
    number = args.number
    nonblank = args.b
    count = 1

    for f in args.file:
        for line in f:
            if nonblank:
                number = 0
                # we assume that if a line contains only whitespace chars, it is a blank line
                if len(line) > 1:
                    sys.stdout.write(f"{count} ".rjust(7)+' ')
                    count += 1 
            if number:
                sys.stdout.write(f"{count} ".rjust(7)+' ')
                count += 1
            if ends:
                sys.stdout.write(line[:-1]+"$"+"\n")
            else:
                sys.stdout.write(line)


if __name__ == '__main__':
    main()
