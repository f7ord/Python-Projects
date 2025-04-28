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
    parser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        help="Reverse the order of the verses, count up instead of down"
    )
    parser.add_argument(
        "-s",
        "--step",
        type=int,
        default=1,
        help="Skip numbers by STEPs"
    )

    args = parser.parse_args()
    if args.num < 1:
        parser.error(f"--num *{args.num}* must be greater than 0")
    if args.step < 1:
        parser.error(f"--step *{args.step}* must be greater than 0")

    return parser.parse_args()


def verse(num):
    """Print a verse"""
    num_less_one = num-1 if num > 1 else 'No more'
    end = 's' if num > 1 else ''
    end2 = '' if num_less_one == 1 else 's'

    return '\n'.join([
        f'{num} bottle{end} of beer on the wall,',
        f'{num} bottle{end} of beer,',
        f'Take one down, pass it around,',
        f'{num_less_one} bottle{end2} of beer on the wall!'
    ])


def main():
    args = get_args()
    num = args.num
    reverse = args.reverse
    step = args.step

    step = step if reverse else -step
    start = 1 if reverse else num
    stop = num+1 if reverse else 0

    print('\n\n'.join(map(verse, range(start, stop, step))))


if __name__ == "__main__":
    main()
