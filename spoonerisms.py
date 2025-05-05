#!/usr/bin/env python3

# create spoonerisms, where the initial consonant sounds
# of adjacent words are switched, so you get 'blushing
# crow' instead of 'crushing blow'

import argparse
import os
from typing import List


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Spoonerisms: the initial consonant'
        ' sounds of adjacent words are switched'
    )
    parser.add_argument(
        'words',
        help='Input file / text'
    )

    args = parser.parse_args()
    if os.path.isfile(args.words):
        args.words = open(args.words, encoding='utf-8').read()
    args.words = args.words.split()

    return args


def break_word(word):
    """Return leading consonants (if any) and the rest of the word"""
    word = word.lower()
    conso = ''

    i = 0
    while i < len(word):
        if word[i] not in 'aeiou' and word[i].isalpha():
            conso += word[i]
            i += 1
        else:
            break
    return conso, word[i:]


def startswithconsonant(word):
    """Return True if word starts with consonant(s)"""
    return bool(break_word(word)[0])


def test_startswithconsonant():
    """Test our functions"""
    assert startswithconsonant('initial') is False
    assert startswithconsonant('commit')
    assert startswithconsonant('Apple') is False
    assert startswithconsonant('123Banana') is False
    assert startswithconsonant('') is False
    assert startswithconsonant('CHAIR')
    assert swap_start('The', 'quick') == ('qe', 'thuick')
    assert swap_start('hello', 'there') == ('thello', 'here')
    assert break_word('apple') == ('', 'apple')
    assert break_word('BANanaS') == ('b', 'ananas')
    assert break_word('chair')[0] == 'ch'
    assert break_word('kljnbmt') == ('kljnbmt', '')
    assert break_word('') == ('', '')
    assert break_word('123') == ('', '123')


def swap_start(x, y):
    """Switch the initial consonant sounds of x and y"""
    x_pref = break_word(x)[0]
    y_pref = break_word(y)[0]
    x = x.lower().replace(x_pref, y_pref, 1)
    y = y.lower().replace(y_pref, x_pref, 1)
    return x, y


def modify_words(words: List[str]):
    """Go through `words` and switch the initial
     consonant sounds of adjacent words"""
    result = []
    x, y = '', ''

    for word in words:
        if not startswithconsonant(word):
            result.insert(words.index(word), f'{word} ')
        else:
            if not x:
                x = word
                x_index = words.index(x)
            elif not y:
                y = word
                y_index = words.index(y)
            if x and y:
                x, y = swap_start(x, y)
                result.insert(x_index, f'{x} ')
                result.insert(y_index, f'{y} ')
                # resetting x and y
                x = ''
                y = ''
        # handle cases where an odd number of words
        # start with consonants
        # if we get to the end of the list and there's an x that has
        # no y counterpart to swap initials with
        if word == words[-1] and x and not y:
            result.insert(x_index, f'{x} ')

    return ''.join(result)


def main():
    args = get_args()
    print(modify_words(args.words))


if __name__ == '__main__':
    main()
