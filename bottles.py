#!/usr/bin/env python3

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Bottles")
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=10,
        help="Print all the verses from NUM down do 1 (default: 10)"
    )

    args = parser.parse_args()
    if args.num < 1:
        parser.error(f"--num *{args.num}* must be greater than 0")

    return parser.parse_args()


def verse(num):
    """Print a verse"""
    bottle = 'bottles' if num > 1 else 'bottle'

    print(f"{num} {bottle} of beer on the wall,")
    print(f"{num} {bottle} of beer,")
    print(f"Take one down, pass it around,")
    if num != 1:
        bottle = 'bottles' if num-1 > 1 else 'bottle'
        print(f"{num-1} {bottle} of beer on the wall!\n")
    else:
        print("No more bottles of beer on the wall!")


def main():
    args = get_args()
    num = args.num

    for i in range(num, 0, -1):
        verse(i)


if __name__ == "__main__":
    main()
