#!/usr/bin/env python3

# Count the number of times each word is seen in a document
# modify to take input from sys.stdin
# modify to take multiple input files

import argparse
import pprint as pp

def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Count: count the number of times each word in the given document occurs"
    )
    parser.add_argument(
        "file",
        type=argparse.FileType('rt'),
        help="Input file"
    )

    return parser.parse_args()


def main():
    args = get_args()
    output = {}

    for line in args.file:
        for word in line.split():
            output[word] = output.get(word, 0) + 1
    
    pp.pp(output)


if __name__ == "__main__":
    main()
