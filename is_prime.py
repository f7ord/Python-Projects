#!/usr/bin/env python3

# Determine if a number is prime

import argparse


def get_args():
    """Get the number"""
    parser = argparse.ArgumentParser(
        description='Prime Number?'
    )
    parser.add_argument(
        'num',
        type=int,
        help='The number, as an integer'
    )
    return parser.parse_args()


def is_prime(n: int):
    """Return True if n is a prime number"""
    if n < 2:
        return False
    for i in range(2, int(n**.5)+1):
        if not n % i:
            return False
    return True


def main():
    print(is_prime(get_args().num))


if __name__ == '__main__':
    main()
