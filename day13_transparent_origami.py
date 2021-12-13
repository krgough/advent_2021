#!/usr/bin/env python3
"""

Advent of Code 2021:  Day 13: Transparent Origami
https://adventofcode.com/2021/day/13

"""
# pylint: disable=invalid-name

TEST_INPUT = 'data/day13_test_data.txt'
TEST_INPUT_2 = 'data/day13_test_data_2.txt'
INPUT = 'data/day13_data.txt'


def load_data(filename):
    """ Load data into a list
    """
    data = []
    fold_data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('fold'):
                line = line.strip().split(' ')[2].split('=')
                line[1] = int(line[1])
                fold_data.append(line)
            elif line.strip():
                data.append([int(v) for v in line.strip().split(',')])

    # max_x = max([d[0] for d in data]) + 1
    # max_y = max([d[1] for d in data]) + 1

    # new_data = [['.' for _ in range(max_x)] for _ in range(max_y)]
    # # for x in range(max_x):
    # #     for y in range(max_y):
    # #         if [x, y] in data:
    # #             new_data[y][x] = "#"
    # for d in data:
    #     new_data[d[1]][d[0]] = '#'

    return data, fold_data


def print_grid(grid):
    """ Pretty print the grid
    """
    x_data = [p[0] for p in grid]
    y_data = [p[1] for p in grid]

    for y in range(max(y_data) + 1):
        for x in range(max(x_data) + 1):
            if [x, y] in grid:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()


def reflection_in_line(grid, m, c):
    """ Calculate the new point after relection
        in line y=mx+c
    """
    denom = 1 + m**2

    for x, _ in enumerate(grid[0]):
        for y, _ in enumerate(grid):
            if grid[y][x] == '#':
                new_x = ((1 - m**2)*x + 2*m*(y - c)) / denom
                new_y = (2*m*x - (1 - m**2)*y + 2*c) / denom
                grid[int(new_y)][int(new_x)] = '#'

    return grid


def reflection_in_x_line(grid, y_cross):
    """  Reflection in a vertical line
    """
    new_grid = []
    for p in grid:
        if p[0] < y_cross and p not in new_grid:
            new_grid.append(p)

        new_x = 2*y_cross - p[0]
        if new_x < y_cross:
            if [new_x, p[1]] not in new_grid:
                new_grid.append([new_x, p[1]])

    return new_grid


def reflection_in_y_line(grid, x_cross):
    """  Reflection in a vertical line
    """
    new_grid = []
    for p in grid:
        if p[1] < x_cross and p not in new_grid:
            new_grid.append(p)

        new_y = 2*x_cross - p[1]
        if new_y < x_cross:
            if [p[0], new_y] not in new_grid:
                new_grid.append([p[0], new_y])

    return new_grid


def main():
    """ Main Program
    """

    # Part 1
    grid, fold_data = load_data(INPUT)
    # print_grid(grid)
    # print(fold_data)
    print()

    for i, fold in enumerate(fold_data):
        if fold[0] == 'x':
            grid = reflection_in_x_line(grid, fold[1])
        else:
            grid = reflection_in_y_line(grid, fold[1])

        if i == 0:
            print(f"Part1: Visible points after 1st fold={len(grid)}")

    print("\nPart2:")
    print_grid(grid)
    print('all done')

    # Part 2


if __name__ == ("__main__"):
    main()
