#!/usr/bin/env python3

# Rhymer: Using regular expressions to create rhyming words

import argparse
import os
import string
import sys


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description='Make rhyming *words*')
    parser.add_argument(
        "word",
        help="A word to rhyme; if it is a filename, the\
         program will iterate and create the rhyming\
         words for each word in the file"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=argparse.FileType('wt'),
        default=sys.stdout,
        help="Output file (default: STDOUT)"
    )

    args = parser.parse_args()
    if os.path.isfile(args.word):
        args.word = open(args.word).read().split()

    return args


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
    """Replace the leading consonants with all the other
    consonants from the alphabets and the given
    consonant clusters"""
    leading, other = break_word(word)

    consonants = [x for x in string.ascii_lowercase if x not in 'aeiou']
    consonants.extend('bl br ch cl cr dr fl fr gl gr pl \
    pr sc sh sk sl sm sn sp st sw th tr tw thw wh wr sch\
     scr shr sph spl spr squ str thr'.split())

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


def write_output(word, outfile=sys.stdout):
    """Print the rhyming words (if can be done) to STDOUT or write them to the output file"""
    if isinstance(replace(word), list):
        print('\n'.join(replace(word)), file=outfile)
    else:
        print(replace(word), file=outfile)


def main():
    args = get_args()
    word = args.word

    if isinstance(word, str):
        write_output(word, args.output)
    elif isinstance(word, list):
        for w in word:
            out = open(f'{w}.txt', 'wt')
            write_output(w, outfile=out)
            out.close()


if __name__ == '__main__':
    main()
