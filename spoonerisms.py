#!/usr/bin/env python3

# create spoonerisms, where the initial consonant sounds of adjacent words are switched, so you get 'blushing crow' instead of 'crushing blow'

import argparse
import os
from typing import List
from rhymer import break_word


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Spoonerisms: the initial consonant sounds of adjacent words are switched"
    )
    parser.add_argument(
        'words',
        help='Input file / text'
    )

    args = parser.parse_args()
    if os.path.isfile(args.words):
        args.words = open(args.words).read()
    args.words = args.words.split()

    return args


def get_words(words: List[str]):
    """Return the words that start with consonants"""
    return list(filter(lambda c: break_word(c)[0] and break_word(c)[0].isalpha(), words))


def test_get_words():
    words = [
        'initial', 'commit', 'Apple', '123Banana',
        'CHAIR','']
    assert get_words(words) == ['commit', 'CHAIR']


def swap_start(x, y):
    """Switch the initial consonant sounds of x and y"""
    x_pref = break_word(x)[0]
    y_pref = break_word(y)[0]
    x = x.replace(x_pref, y_pref, 1)
    y = y.replace(y_pref, x_pref, 1)
    return x, y


def main():
    args = get_args()
    words = args.words
    cons_word = get_words(words)

    result = []
    x, y = '', ''
    for word in words:
        if word not in cons_word:
            result.insert(words.index(word), f'{word} ')
        else:
            if not x:
                x = word
            elif not y:
                y = word
            if x and y:
                x_index = words.index(x)
                y_index = words.index(y)
                x, y = swap_start(x, y)
                result.insert(x_index, f'{x} ')
                result.insert(y_index, f'{y} ')
                x = ''
                y = ''
    print(''.join(result))


if __name__ == '__main__':
    main()
