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

    for i in range(2, int(n**0.5)+1):
        if not n % i:
            cnt = 0
            # print(f'{i:4}|{n}<== new i')
            while not n % i:
                # print(f'{i:4}|{n//i}')
                n = n//i
                cnt += 1
            factors.append((i, cnt))
    if n != 1:
        factors.append((n, 1))
    return factors


def main():
    num = get_args().num
    print(factorization(num))


if __name__ == '__main__':
    main()
