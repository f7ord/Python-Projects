#!/usr/bin/env python3

# Insult the user by randomly selecting adjectives and nouns to create slanderous epithets


import argparse
import random


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Heap abuse"
    )
    parser.add_argument(
        "--adjectives",
        "-A",
        type=argparse.FileType('rt'),
        default="adjectives.txt",
        help="The file that contains the adjectives"
    )
    parser.add_argument(
        "--nouns",
        "-N",
        type=argparse.FileType('rt'),
        default="nouns.txt",
        help="The file that contains the nouns"
    )
    parser.add_argument(
        "-a",
        "--num_adjs",
        type=int,
        default=2,
        help="Number of adjectives (default: 2)"
    )
    parser.add_argument(
        "-n",
        "--number",
        metavar="insults",
        type=int,
        default=3,
        help="Number of insults (default: 3)"
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        help="Random seed (default: None)",
    )

    args = parser.parse_args()
    if args.num_adjs < 1:
        parser.error(f'--adjectives *{args.num_adjs}* must be > 0')
    elif args.number < 1:
        parser.error(f'--number *{args.number}* must be > 0')

    args.adjectives = args.adjectives.read().split()
    args.nouns = args.nouns.read().split()

    return args


def main():
    args = get_args()
    adjectives = args.adjectives
    nouns = args.nouns
    random.seed(args.seed)  

    for _ in range(args.number):
        adjs = random.sample(adjectives, args.num_adjs)
        noun = random.choice(nouns)
        print(f"You {', '.join(adjs)} {noun}!")


if __name__ == "__main__":
    main()
