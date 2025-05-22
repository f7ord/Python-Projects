#!/usr/bin/env python3

# Check if the phrase or word given is a palindrome

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Palindrome checker")
    parser.add_argument(
        'text',
        help='The phrase or word'
    )
    return parser.parse_args()


def is_palindrome(text):
    """Return True if text is a palindrome"""
    text = ''.join(filter(lambda x: x.isalnum(), text))
    text = text.lower().replace(' ', '')
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:-1])


def test_is_palindrome():
    assert is_palindrome('nurses run')
    assert not is_palindrome('nurses rune')
    assert is_palindrome('')
    assert is_palindrome('121')
    assert is_palindrome('l')
    assert is_palindrome('Sit on a potato pan, Otis')
    assert is_palindrome('Cigar? Toss it in a can. It is so tragic.')


def main():
    text = get_args().text
    print(is_palindrome(text))


if __name__ == '__main__':
    main()
