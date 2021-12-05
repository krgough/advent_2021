#!/usr/bin/env python3
"""

Advent of Code 2021: Day 5: Hydrothermal Venture
https://adventofcode.com/2021/day/5

"""

from collections import namedtuple

TEST_INPUT = 'data/day05_test_data.txt'
INPUT = 'data/day05_data.txt'


Point = namedtuple("Point", ['x', 'y'])


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            row = line.strip().split(" -> ")
            for point in row:
                coords = [int(i) for i in point.split(",")]
                data.append(Point(*coords))
    return data


def build_blank_grid(data):
    """ Populate a blank grid with '.' chars.
        Determine the grid size from the given data
    """
    x_max = max([point.x for point in data])
    y_max = max([point.y for point in data])

    grid = [['.' for x in range(x_max + 1)]
            for y in range(y_max + 1)]

    return grid


def create_sequence(start, stop, length):
    """ Create a list of integers of given length.
    """
    if start < stop:
        step = 1
    elif start > stop:
        step = -1
    else:
        step = 0

    my_range = [start + (i * step) for i in range(length + 1)]
    return my_range


def create_seg_ranges(p1, p2):
    # pylint: disable=invalid-name
    """ Create ranges for x and y co-ords for
        the the line segment defined by p1 and p2.
    """
    seg_len = max(abs(p1.x - p2.x), abs(p1.y - p2.y))

    x_range = create_sequence(p1.x, p2.x, seg_len)
    y_range = create_sequence(p1.y, p2.y, seg_len)

    return x_range, y_range


def plot_lines(coords):
    """ Take the list of line segment coords
        and draw those lines into the grid
        Each point is a number that is incremented
        when a line passes through that point.
    """
    # pylint: disable=invalid-name
    grid = build_blank_grid(coords)

    for i in range(0, len(coords) - 1, 2):
        p1 = coords[i]
        p2 = coords[i+1]

        x_range, y_range = create_seg_ranges(p1, p2)

        for idx, x in enumerate(x_range):
            y = y_range[idx]
            if grid[y][x] == '.':
                grid[y][x] = 1
            else:
                grid[y][x] += 1

        # print_grid(grid)

    return grid


def print_grid(grid):
    """ Print the grid """
    for row in grid:
        print("".join([str(i) for i in row]))
    print()


def count_overlaps(grid):
    """ Count points in the grid where line count at the
        point is greater than 1
    """
    count = 0
    for row in grid:
        for cell in row:
            try:
                if int(cell) > 1:
                    count += 1
            except ValueError:
                pass
    return count


def main():
    """ Main Program

        Bingo card wins if any row or column is complete

    """
    data = load_data(INPUT)
    grid = plot_lines(data)

    # print_grid(grid)
    overlaps = count_overlaps(grid)
    print(f"Overlaps: {overlaps}")
    assert overlaps == 18864


if __name__ == ("__main__"):
    main()
