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
        "-a",
        "--adjectives",
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
    if args.adjectives < 1:
        parser.error(f'--adjectives *{args.adjectives}* must be > 0')
    elif args.number < 1:
        parser.error(f'--number *{args.number}* must be > 0')

    return args


def main():
    args = get_args()
    random.seed(args.seed)  

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable 
    dishonest false filthsome filthy foolish foul gross 
    heedless indistinguishable infected insatiate irksome 
    lascivious lecherous loathsome lubbery old peevish rascaly
    rotten ruinous scurilous scurvy slanderous sodden-witted 
    thin-faced toad-spotted unmannered vile wall-eyed
    """.split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart
    butt carbuncle coward coxcomb cur dandy degenerate fiend 
    fishmonger fool gull harpy jack jolthead knave liar lunatic 
    maw milksop minion ratcatcher recreant rogue scold slave 
    swine traitor varlet villain worm
    """.split()

    for _ in range(args.number):
        adjs = random.sample(adjectives, args.adjectives)
        noun = random.choice(nouns)
        print(f"You {', '.join(adjs)} {noun}!")


if __name__ == "__main__":
    main()
