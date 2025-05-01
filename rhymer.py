#!/usr/bin/env python3

# Rhymer: Using regular expressions to create rhyming words

import argparse
import string


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description='Make rhyming *words*')
    parser.add_argument(
        "word",
        help="A word to rhyme"
    )
    return parser.parse_args()


def break_word(word):
    """Return leading consonants (if any) and the rest of the word"""
    word = word.lower()
    conso = ''
    
    i = 0
    while i < len(word):
        if word[i] not in 'aeiou':
            conso += word[i]
            i += 1
        else:
            break
    return conso, word[i:]


def replace(word):
    """Replace the leading consonants with all the other consonants from the alphabets and the given consonant clusters"""
    leading, other = break_word(word)

    consonants = [x for x in string.ascii_lowercase if x not in 'aeiou']
    consonants.extend('bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr'.split())
    
    if not other: # if word is only consonants
        return f'Cannot rhyme "{word}"'
    return sorted([char + other for char in consonants if char != leading])


def test_break_word():
    assert break_word('apple') == ('', 'apple')
    assert break_word('BANanaS') == ('b', 'ananas')
    assert break_word('chair')[0] == 'ch'
    assert break_word('kljnbmt') == ('kljnbmt', '')
    assert break_word('') == ('', '')
    assert break_word('123') == ('123','')


def main():
    args = get_args()
    word = args.word
    
    print('\n'.join(replace(word))) if type(replace(word)) == list else print(replace(word))


if __name__ == '__main__':
    main()
