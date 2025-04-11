#!/usr/bin/env python3

# TODO: make it work for higher bases like 16

import argparse


def get_args():
    "Get the command-line arguments"
    parser = argparse.ArgumentParser(
        description="Convert the given decimal number to base b"
    )
    parser.add_argument(
        "num", 
        help="the decimal number to convert", 
        type=int)
    parser.add_argument(
        "-b",
        "--base",
        metavar="base",
        help="the base to convert the number to (default is 2)",
        default=2,
        type=int,
    )
    return parser.parse_args()


def base_convert(num: int, b: int):
    """Basic base conversion program
    num: the number to convert (decimal)
    b: the base to convert the number to (default is 2)
    Return num in base b
    """
    ans = []
    while num:
        ans.insert(0, num % b)
        num = num // b
    return "".join(str(i) for i in ans)


def main():
    args = get_args()
    print(base_convert(args.num, args.base))


if __name__ == "__main__":
    main()
