#!/usr/bin/env python3

import argparse
import random


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Integer generator:" +
        " Generate n random integers")
    parser.add_argument(
        "n",
        type=int,
        help="Number of integers to generate"
    )
    parser.add_argument(
        "--seed",
        "-s",
        help="Random seed (default: None)"
    )
    return parser.parse_args()


def generator(n: int):
    """Generate n random integers"""
    return ' '.join(str(random.randint(0, 9)) for _ in range(n))


def main():
    args = get_args()
    random.seed(args.seed)

    print(generator(args.n))


if __name__ == '__main__':
    main()
