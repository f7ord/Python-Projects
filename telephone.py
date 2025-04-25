#!/usr/bin/env python3

# print “You said: ” and the original text, followed by “I heard: ” with a modified version of the message

import argparse
import io
import os
import random
import string


def get_args():
    """Get the commandd-line arguments"""
    parser = argparse.ArgumentParser(
        description="Telephone"
    )
    parser.add_argument(
        "text",
        help="Input file"
    )
    parser.add_argument(
        "-m",
        "--mutations",
        type=float,
        default=0.1,
        help="The percentage of the number of letters that should be altered (0 <= m <= 1)"
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
    
    if not 0 <= args.mutations <= 1:
        parser.error(f"--mutations *{args.mutations}* must be `0 <= mutations <= 1`")

    return args


def main():
    args = get_args()
    random.seed(args.seed)
    text = args.text
    mutations = round(len(text) * args.mutations)
    chars = string.ascii_letters + string.punctuation
    
    for i in random.sample(range(len(text)), mutations):
        rep_char = random.choice(chars.replace(text[i], '')) # ensures that rep_char != text[i]
        text = text[:i] + rep_char + text[i+1:]

    print(f"You said: *{args.text}*")
    print(f"I heard: *{text}*")


if __name__ == "__main__":
    main()
