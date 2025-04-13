#!/usr/bin/env python3

import argparse
import os
import sys


def get_args():
    """Get the command line arguments"""
    parser = argparse.ArgumentParser(description="Make the given text uppercase")
    parser.add_argument("text", help="The message or file to transform")
    parser.add_argument("--out", "-o", default="", help="Output filename")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def main():
    args = get_args()
    outfile = open(args.out, "wt") if args.out else sys.stdout
    # outfile.write(args.text.upper() + "\n")
    print(args.text.upper(), file=outfile)
    outfile.close()


if __name__ == "__main__":
    main()
