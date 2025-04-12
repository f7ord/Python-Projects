#!/usr/bin/env python3

import argparse

def get_args():
    """Get the command line arguments"""
    parser = argparse.ArgumentParser(description="Make the given text uppercase")
    parser.add_argument('text', help="The message to transform")
    return parser.parse_args()


def main():
    args = get_args()
    print(args.text.upper())

if __name__ == '__main__':
    main()
