#!/usr/bin/env python3

# print “You said: ” and the original text, followed by “I heard: ” with a modified version of the message

import argparse
import io
import os
import random
import string
import sys


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
    parser.add_argument(
        "-w",
        "--words",
        action="store_true",
        help="Apply the mutations to randomly selected words instead of the whole string"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file"
    )
    parser.add_argument(
        "-c",
        "--chars",
        action="store_true",
        help="Limit the replacements to character values only (no punctuations)"
    )

    args = parser.parse_args()
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    if not 0 <= args.mutations <= 1:
        parser.error(f"--mutations *{args.mutations}* must be `0 <= mutations <= 1`")
    
    args.output = open(args.output, 'w') if args.output else sys.stdout

    return args


def main():
    def mutate_string(text, n: int):
        """
        n is the number of chars to replace
        Return the mutated version of the given string"""
        result = text
        chars = string.ascii_letters if args.chars else string.ascii_letters + string.punctuation
        
        for i in random.sample(range(len(text)), n):
            rep_char = random.choice(chars.replace(result[i], '')) # ensures that rep_char != text[i]
            result = result[:i] + rep_char + result[i+1:]
        return result
    
    args = get_args()
    text = args.text
    num_mutations = round(len(text.split()) * args.mutations) if args.words else round(len(text) * args.mutations)
    random.seed(args.seed)

    if not args.words:
        result = mutate_string(text, num_mutations)
    else:
        words = text.split()
        for i in random.sample(range(len(words)), num_mutations):
            words[i] = mutate_string(words[i], len(words[i])) # passed n as len(words[i]) so the whole word is mutated
        result = ' '.join(words)

    print(f"You said: *{args.text}*")
    print(f"I heard: *{result}*", file=args.output)


if __name__ == "__main__":
    main()
