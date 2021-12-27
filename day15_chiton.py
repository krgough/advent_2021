#!/usr/bin/env python3
"""

Advent of Code 2021:  Day 15: Chiton
https://adventofcode.com/2021/day/15

"""
# pylint: disable=invalid-name
from rich import print as pprint

TEST_INPUT = 'data/day15_test_data.txt'
INPUT = 'data/day15_data.txt'


def load_data(filename):
    """ Load data from a file
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        grid = [[int(n) for n in line.strip()] for line in file]
    return grid


def find_exits(x, y, max_x, max_y):
    """ Find all exits from current location
    """
    exits = []

    if y != 0:
        exits.append((x, y - 1))

    if y != max_y:
        exits.append((x, y + 1))

    if x != 0:
        exits.append((x - 1, y))

    if x != max_x:
        exits.append((x + 1, y))

    return exits


def find_route(grid):
    """ Walk the grid starting at 0,0.
        For each exit point - work out the total path cost to
        get to that point.  Save a breadcrumb trail of how we
        got there.  For any cell we visit if the total cost
        to get there is less that the existing value then
        overwrite with the new value.

        At the end we follow the breadcrumbs back to get the
        'cheapest' route.

    """

    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    costs = {(0, 0): 0}
    bc_path = {}
    points = [(0, 0)]

    for (x, y) in points:
        neighbours = find_exits(x, y, max_x, max_y)
        for (x1, y1) in neighbours:
            if ((x1, y1) in costs and
                    costs[x1, y1] <= costs[x, y] + grid[y1][x1]):
                # This route in is more expensive than existing
                # so ignore it
                continue

            costs[x1, y1] = costs[x, y] + grid[y1][x1]
            points.append((x1, y1))
            bc_path[x1, y1] = (x, y)

    # path = {(0, 0)}
    # x, y = max_x, max_y
    # while (x, y) != (0, 0):
    #     path.add((x, y))
    #     x, y = bc_path[x, y]

    # for y, row in enumerate(grid):
    #     my_str = ""
    #     for x, risk in enumerate(row):
    #         if (x, y) in path:
    #             my_str += f"[green]{risk}[/green]"
    #         else:
    #             my_str += f"[dim white]{risk}[/dim white]"
    #     pprint(my_str)

    return costs[max_x, max_y]


def tile(row, n):
    """ Create the row for the nth tile
        Each entry is n larger than the corresponding
        entry in the original row
    """
    return [((c+n-1) % 9) + 1 for c in row]


def part_2_data(grid):
    """ Create the extended grid
    """
    new_grid = []
    for n in range(5):
        for row in grid:
            r = tile(row, n)
            r += tile(row, n + 1)
            r += tile(row, n + 2)
            r += tile(row, n + 3)
            r += tile(row, n + 4)
            new_grid.append(r)
    return new_grid


if __name__ == "__main__":
    # Part 1
    assert find_route(load_data(TEST_INPUT)) == 40
    cost = find_route(load_data(INPUT))
    print(f"Part1: {cost}")

    # # Part 2
    new_data = part_2_data(load_data(TEST_INPUT))
    assert find_route(new_data) == 315, find_route(new_data)

    new_data = part_2_data(load_data(INPUT))
    cost = find_route(new_data)
    print(f"Part2: {cost}")
    print('all done')
