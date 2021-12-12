#!/usr/bin/env python3
"""

Advent of Code 2021: Day 11: Dumbo Octopus
https://adventofcode.com/2021/day/11

"""
# pylint: disable=invalid-name
import numpy as np

TEST_INPUT = 'data/day11_test_data.txt'
INPUT = 'data/day11_data.txt'


# class Point():
#     """ Class for points """
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            data.append([int(i) for i in list(line.strip())])

    return np.array(data)


def get_neighbours(x, y, max_x, max_y):
    """ Get a list of the neighbour coords
        Typically 8 but fewer for edge cells
    """
    neighbours = []
    for x_delta in range(-1, 2, 1):
        for y_delta in range(-1, 2, 1):
            x_new = x + x_delta
            y_new = y + y_delta
            if 0 <= x_new < max_x and 0 <= y_new < max_y:
                neighbours.append((y_new, x_new))
    return neighbours


def update_neighbours(x, y, max_x, max_y, data):
    """  Add 1 energy point to all neighbours
    """
    neighbours = get_neighbours(x, y, max_x, max_y)
    for n in neighbours:
        if data[n] > 0:
            data[n] += 1
    return data


def iterate(data, flash_count, max_x, max_y):
    """ Peform one charge/flash cycle
    """
    # Scan the grid
    # All increase by 1
    data += 1

    # Now find any that have exceeded 9
    # They cause all neighbours to inc by 1
    # Keep doing this until no more are over 9

    while (data > 9).any():
        for x in range(max_x):
            for y in range(max_y):
                if data[y][x] > 9:
                    data[y][x] = 0
                    flash_count += 1
                    data = update_neighbours(x, y, max_x, max_y, data)

    return data, flash_count


def main():
    """ Main Program
    """

    # Part 1
    data = load_data(INPUT)
    max_x = data.shape[0]
    max_y = data.shape[1]

    flash_count = 0
    for i in range(100):
        data, flash_count = iterate(data, flash_count, max_x, max_y)

    print(data)
    print(f'Iteration: {i+1}, Flash Count: {flash_count}')

    # Part 2
    data = load_data(INPUT)
    max_x = data.shape[0]
    max_y = data.shape[1]
    i = 0
    flash_count = 0
    while (data != 0).any():
        i += 1
        data, flash_count = iterate(data, flash_count, max_x, max_y)

    print(data)
    print(f"Part2: In sync on iteration {i}")


if __name__ == ("__main__"):
    main()
