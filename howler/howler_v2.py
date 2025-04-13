#!/usr/bin/env python3

import argparse
import os
import sys
import io


def get_args():
    """Get the command line arguments"""
    parser = argparse.ArgumentParser(description="Make the given text uppercase")
    parser.add_argument(
        "text",
        nargs="+",
        help="The message or file to transform")
    parser.add_argument(
        "--outdir",
        "-o", 
        default="", 
        help="Output filename")
    parser.add_argument(
        "-lc", 
        action="store_true", 
        help="The input will be printed in lowercase, if on"
    )

    args = parser.parse_args()

    for i, f in enumerate(args.text):
        if os.path.isfile(f):
            args.text[i] = open(f)
        else:
            args.text[i] = io.StringIO(f + "\n")

    return args


def main():
    args = get_args()
    outfile = open(args.outdir, "wt") if args.outdir else sys.stdout
    out_case = str.lower if args.lc else str.upper
    for f in args.text:
        for line in f:
            outfile.write(out_case(line))
    outfile.close()


if __name__ == "__main__":
    main()
