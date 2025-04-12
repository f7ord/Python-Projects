#!/usr/bin/env python3

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
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }
    print("".join(key.get(t, t) for t in text))


if __name__ == "__main__":
    main()
