#!/usr/bin/env python3

# Calculate the factorial of a number

import argparse


def get_args():
    """Get the number"""
    parser = argparse.ArgumentParser(
        description="Factorial"
    )
    parser.add_argument(
        'num',
        type=int,
        help='The number'
    )

    args = parser.parse_args()
    if args.num < 0:
        parser.error(f'*{args.num}* must be non-negative')

    return args


def factorial(n):
    """Return the factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n-1)


def main():
    num = get_args().num
    print(factorial(num))


if __name__ == '__main__':
    main()
