#!/usr/bin/env python3

import argparse
import os
import sys
import io


def get_args():
    """Get the command line arguments"""
    parser = argparse.ArgumentParser(description="Make the given text uppercase")
    parser.add_argument("text", help="The message or file to transform")
    parser.add_argument("--out", "-o", default="", help="Output filename")
    parser.add_argument('-lc', action="store_true", help="The input will be printed in lowercase, if on")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')
    
    return args


def main():
    args = get_args()
    outfile = open(args.out, 'wt') if args.out else sys.stdout
    out_case = str.lower if args.lc else str.upper
    for line in args.text:
        outfile.write(out_case(line))
    outfile.close()


if __name__ == '__main__':
    main()
