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

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')
    
    return args


def main():
    args = get_args()
    outfile = open(args.out, 'wt') if args.out else sys.stdout
    for line in args.text:
        outfile.write(line.upper())
    outfile.close()


if __name__ == '__main__':
    main()
