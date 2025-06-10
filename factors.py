#!/usr/bin/env python3

# Find all the factors of the given number

import argparse


def get_args():
    """Get the number"""
    parser = argparse.ArgumentParser(
        description="Find all the factors"
    )
    parser.add_argument(
        'num',
        nargs='+',
        type=int,
        help='The number, an integer'
    )
    return parser.parse_args()


def factors(num: int):
    """Find all the factors of num"""
    ans = set()
    for i in range(1, int(num**0.5)+1):
        if not num % i:
            ans.add(i)
            ans.add(num // i)
    return sorted(ans)


def main():
    nums = get_args().num

    if len(nums) > 1:
        for num in nums:
            print(f'{num: 4}:', factors(num))
    else:
        print(factors(nums[0]))


if __name__ == '__main__':
    main()
