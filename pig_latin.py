#!/usr/bin/env python3

""" Pig Latin """

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Pig Latin")
    parser.add_argument(
        "word",
        help="Input word"
    )
    return parser.parse_args()


def main():
    word = get_args().word

    if word[0] not in 'aeiou':
        print(f'{word[1:]}-{word[0]}ay')
    else:
        print(f'{word}-yay')


if __name__ == '__main__':
    main()
