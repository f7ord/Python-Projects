#!/usr/bin/env python3

import argparse

def get_args():
    "Get the command line arguments"
    parser = argparse.ArgumentParser(description="Crow's Nest Program")
    parser.add_argument('word', type=str, help="The object to call out")
    return parser.parse_args()


def main():
    args = get_args()
    word = args.word
    article = 'an' if args.word[0].lower() in 'aeiou' else 'a'
    article = article.title() if word[0].isupper() else article
    print(f'Ahoy, Captain, {article} {args.word} off the larboard bow!')


if __name__ == '__main__':
    main()
