#!/usr/bin/env python3

# Ransom: Randomly capitalizing text

import argparse
import random
import os


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Ransom")
    parser.add_argument(
        "text",
        help="Input text/file",
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        help="Random seed (default: None)"
    )

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args


def capitalize(s):
    """Return the uppercase of the given letter"""
    return s.upper() if random.choice([0,1]) else s.lower()


def main():
    args = get_args()
    random.seed(args.seed)

    print(''.join(map(capitalize, args.text)))
    

if __name__ == '__main__':
    main()
