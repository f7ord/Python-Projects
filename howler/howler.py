#!/usr/bin/env python3

import argparse
import os

def get_args():
    """Get the command line arguments"""
    parser = argparse.ArgumentParser(description="Make the given text uppercase")
    parser.add_argument('text', help="The message or file to transform")
    return parser.parse_args()


def main():
    args = get_args()
    text = args.text

    if os.path.isfile(text):
        content = open(text).read().rstrip()
        print(content)
    else:
        print(text.upper())


if __name__ == '__main__':
    main()
