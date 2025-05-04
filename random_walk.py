#!/usr/bin/env python3

# A simple random walk

import argparse
import random
import matplotlib.pyplot as plt


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="A simple random walk starting at 0 with steps"
        " of 1 and -1 occurring with equal probability")
    parser.add_argument("nsteps", type=int, help="Number of steps")
    return parser.parse_args()


def generate_walks(nsteps):
    """Generate steps of 1 and -1 occurring with equal probability"""
    position = 0
    walks = [position]

    for _ in range(nsteps - 1):
        step = random.choice((-1, 1))
        position += step
        walks.append(position)
    return walks


def main():
    args = get_args()

    walks = generate_walks(args.nsteps)
    plt.plot(walks)
    plt.show()


if __name__ == "__main__":
    main()
