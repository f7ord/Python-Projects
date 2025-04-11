#!/usr/bin/env python3

import argparse

def get_args():
    "Get the command line arguments"
    parser = argparse.ArgumentParser(description="Crow's Nest Program")
    parser.add_argument('word', type=str, help="The object to call out")
    parser.add_argument('-s', '--star', action='store_true', help="Changes larboard to starboard if present.")
    return parser.parse_args()


def main():
    args = get_args()
    word = args.word
    if word[0].isalpha():
        article = 'an' if args.word[0].lower() in 'aeiou' else 'a'
        article = article.title() if word[0].isupper() else article
        side = 'starboard' if args.star else 'larboard'
        print(f'Ahoy, Captain, {article} {args.word} off the {side} bow!')
    else:
        print('The program does not recognize the word provided.')


if __name__ == '__main__':
    main()
