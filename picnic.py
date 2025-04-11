#!/usr/bin/env python3

import argparse

def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Picnic Program")
    parser.add_argument('items', metavar='items', nargs='+', help='Item(s) to bring')
    parser.add_argument('-s', '--sorted', action='store_true', help='Sort the items to bring, if present')
    parser.add_argument('-c', '--comma', action='store_true', help='If present, print without the Oxford comma.')
    parser.add_argument('--sep', metavar='separator', default=',', help='The character to separate items.')
    return parser.parse_args()


def main():
    args = get_args()
    items = args.items
    sep = args.sep + ' '
    
    if args.sorted:
        items.sort()
    
    if len(items) == 1:
        print(f'You are bringing {items[0]}.')
    elif len(items) == 2:
        print(f'You are bringing {items[0]} and {items[1]}.')
    else:
        if args.comma:
            print(f"You are bringing {sep.join(items[:-1])} and {items[-1]}.")
        else:
            print(f"You are bringing {sep.join(items[:-1])}{sep.rstrip()} and {items[-1]}.")


if __name__ == '__main__':
    main()
