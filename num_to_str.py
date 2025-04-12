#!/usr/bin/env python3
# Encode the numbers with strings

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Jump the Five")
    parser.add_argument("text", help="The text to encode")
    return parser.parse_args()


def main():
    args = get_args()
    text = args.text

    key = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero",
    }
    print("".join(key.get(t, t) for t in text))


if __name__ == "__main__":
    main()
