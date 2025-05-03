#!/usr/bin/env python3

import argparse
import sys
from rhymer import break_word


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Find and return all unique consonant sounds in FILE")
    parser.add_argument(
        '-f',
        '--file',
        type=argparse.FileType('rt'),
        default='dictionary.txt',
        help="Input file"
    )
    parser.add_argument(
        '-o',
        '--outfile',
        type=argparse.FileType('wt'),
        default=sys.stdout,
        help="Output file"
    )
    return parser.parse_args()


def find_consonant_sounds(file):
    """Find and return all unique consonant sounds in dictionary"""
    sounds = set()

    for word in file:
        word = word.lower()
        start = break_word(word)[0]
        if start:
            sounds.add(start)
    return list(sounds)


def main():
    args = get_args()
    sounds = sorted(find_consonant_sounds(args.file))
    if args.outfile == sys.stdout:
        return sounds
    args.outfile.write('\n'.join(sounds))


if __name__ == '__main__':
    main()
