#!/usr/bin/env python3

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Bottles")
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=10,
        help="Print all the verses from NUM down do 1"
    )

    return parser.parse_args()


def main():
    args = get_args()
    num = args.num

    # def on_the_wall(num, end=','):
    #     bottle = 'bottles' if num > 1 else 'bottle'
    #     print(f"{num} {bottle} of beer on the wall{end}")
    #     if end != '!':
    #         print(f"{num} {bottle} of beer,")


    # for _ in range(num):
    #     on_the_wall(num)
    #     print(f"Take one down, pass it around,")
    #     if num != 1:
    #         on_the_wall(num-1, end='!')
    #         print("\n")
    #         num -= 1
    #     else:
    #         print(f"No more bottles of beer on the wall!\n")

    def on_the_wall(num, end=','):
        bottle = 'bottles' if num > 1 else 'bottle'
        print(f"{num} {bottle} of beer on the wall{end}")
        if end != '!\n':
            print(f"{num} {bottle} of beer,")


    for i in range(num, 0, -1):
        on_the_wall(i)
        print(f"Take one down, pass it around,")
        if i != 1:
            on_the_wall(i-1, end='!\n')
        else:
            print(f"No more bottles of beer on the wall!")

if __name__ == "__main__":
    main()
