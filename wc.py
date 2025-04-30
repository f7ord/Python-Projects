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
    parser.add_argument(
        '--chars',
        '-c',
        action="store_true",
        help="Print the number of characters"
    )
    parser.add_argument(
        "--lines",
        "-l",
        action="store_true",
        help="Print the number of lines"
    )
    parser.add_argument(
        "--words",
        "-w",
        action="store_true",
        help="Print the number of words"
    )

    return parser.parse_args()


def main():
    args = get_args()
    tnl, tnw, tnb = 0, 0, 0
    c, l, w = args.chars, args.lines, args.words

    for fh in args.file:
        nl, nw, nb = 0, 0, 0
        for line in fh:
            nl += 1
            nw += len(line.split())
            nb += len(line)
        tnl += nl
        tnw += nw
        tnb += nb

        # printing the result
        # print all the columns by default
        if not any([l, w, c]):
            print(f"{nl:8}{nw:8}{nb:8} {fh.name}")
        else:
            output = ""
            total = ""
            if l:
                output += f"{nl:8}"
                total += f"{tnl:8}"
            if w:
                output += f"{nw:8}"
                total += f"{tnw:8}"
            if c:
                output += f"{nb:8}"
                total += f"{tnb:8}"

            output += f" {fh.name}"
            total += " total"
            print(output)
        fh.close()
    # print the total if more than one file is passed
    if len(args.file) > 1:
        if not any([l,w,c]):
            print(f"{tnl:8}{tnw:8}{tnb:8} total")
        else:
            print(total)


if __name__ == '__main__':
    main()
