#!/usr/bin/env python3

# Ransom: Randomly mutating text

import argparse
import random
import os


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Ransom")
    parser.add_argument(
        "text",
        help="Input text/file",
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        help="Random seed (default: None)"
    )

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args


def mutate(s):
    """Return the uppercase of the given letter"""
    key = {
        'a': '4',
        'b': '|3',
        'c': '(',
        'd': '|)',
        'e': '3',
        'f': '|=',
        'g': '(-',
        'h': '|-|',
        'i': '1',
        'j': '_|',
        'k': '|<',
        'l': '|_',
        'm': r'|\/|',
        'n': r'|\|',
        'o': '0',
        'p': '|`',
        's': '5',
        't': '+',
        'v': r'\/',
        'w': r'\/\/'
    }
    return key.get(s.lower(), s)


def main():
    args = get_args()
    random.seed(args.seed)

    print(''.join(map(mutate, args.text)))
    

def test_mutate():
    assert mutate('N') == r'|\|'
    assert mutate('o') == '0'
    assert mutate('A') != 'a'
    assert mutate('A') == str(4)


if __name__ == '__main__':
    main()
