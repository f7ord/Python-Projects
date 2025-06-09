#!/usr/bin/env python3

# Find the prime factorization of a number

import argparse


def get_args():
    """Get the number"""
    parser = argparse.ArgumentParser(
        description='Prime Factorization'
    )
    parser.add_argument(
        'num',
        type=int,
        help='The number, as an integer'
    )

    args = parser.parse_args()
    if args.num <= 1:
        parser.error(f'*{args.num}* must be greater than 1')

    return args


def factorization(n: int):
    """Return the prime factorization of n"""
    factors = []

    for i in range(2, n+1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n = n//i
                cnt += 1
            factors.append((i, cnt))
    return factors


def main():
    print(factorization(get_args().num))


if __name__ == '__main__':
    main()
