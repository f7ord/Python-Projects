#!/usr/bin/env python3

# Twelve Days of Christmas: Algorithm design

import argparse
import sys


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Twelve Days of Christmas")
    parser.add_argument(
        "-n",
        "--num",
        metavar="days",
        type=int,
        default=12,
        help="Number of days to sing (default: 12)"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=argparse.FileType('wt'),
        default=sys.stdout,
        help="Outfile (default: STDOUT)"
    )

    args = parser.parse_args()
    if not 1 <= args.num <= 12:
        parser.error(f"--num {args.num} must be between 1 and 12")

    return args


def verse(n):
    """Generate a verse"""
    days = {
        1: ['first', 'A partridge in a pear tree.'],
        2: ['second', 'Two turtle doves,'],
        3: ['third', 'Three French hens,'],
        4: ['fourth', 'Four calling birds,'],
        5: ['fifth', 'Five gold rings,'],
        6: ['sixth', 'Six geese a laying,'],
        7: ['seventh', 'Seven swans a swimming,'],
        8: ['eighth', 'Eight maids a milking,'],
        9: ['ninth', 'Nine ladies dancing,'],
        10: ['tenth', 'Ten lords a leaping,'],
        11: ['eleventh', 'Eleven pipers piping,'],
        12: ['twelfth', 'Twelve drummers drumming,'],
    }

    lines = [
        f'On the {days[n][0]} day of Christmas,',
        'My true love gave to me,',
        f'{days[n][1]}',
    ]

    if n > 1:
        for i in range(n-1, 0, -1):
            if i == 1:
                lines.append('And ' + days[1][1].lower())
            else:
                lines.append(days[i][1])

    return '\n'.join(lines)


def test_verse():
    assert verse(5) == '\n'.join([
        'On the fifth day of Christmas,',
        'My true love gave to me,',
        'Five gold rings,',
        'Four calling birds,',
        'Three French hens,',
        'Two turtle doves,',
        'And a partridge in a pear tree.'
        ])
    assert verse(1) == 'On the first day of Christmas,\
\nMy true love gave to me,\nA partridge in a pear tree.'


def main():
    args = get_args()

    print('\n\n'.join(map(verse, range(1, args.num+1))), file=args.output)
    args.output.close()


if __name__ == '__main__':
    main()
