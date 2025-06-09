#!/usr/bin/env python3

# Sieve of Eratosthenes

import argparse


def get_args():
    """Get the number"""
    parser = argparse.ArgumentParser(
        description='Sieve of Eratosthenes'
    )
    parser.add_argument(
        'num',
        type=int,
        help='The number, as an integer'
    )
    return parser.parse_args()


def sieve(n):
    """Return all the prime numbers under n"""
    nums = list(range(2, n))

    for x in range(2, int(n**.5)+1):
        for i in range(x**2, n+1):
            if i in nums and not i % x:
                nums.remove(i)
    return nums


def main():
    num = get_args().num
    print(' '.join(str(x) for x in sieve(num)))


if __name__ == '__main__':
    main()
