#!/usr/bin/env python3
"""

Advent of Code 2021: Day 9: Smoke Basin
https://adventofcode.com/2021/day/

"""
# pylint: disable=invalid-name

TEST_INPUT = 'data/day09_test_data.txt'
INPUT = 'data/day09_data.txt'


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            line_data = [int(d) for d in line.strip()]
            data.append(line_data)
    return data


def print_grid(data):
    """ Pretty print the data grid
    """
    for row in data:
        for num in row:
            print(num, end='')
        print()


def find_neighbours_old(data, x, y):
    """ Find neighbour values
    """
    neighbours = []
    neighbours.append(9 if y == 0 else data[y - 1][x])
    neighbours.append(9 if y == len(data) - 1 else data[y + 1][x])
    neighbours.append(9 if x == 0 else data[y][x - 1])
    neighbours.append(9 if x == len(data[0]) - 1 else data[y][x + 1])
    return neighbours


def find_neighbours(data, x, y):
    """ Return the neighbour co-ords
        Handle edges of the grid
    """
    neighbours = []

    if y != 0:
        neighbours.append((y - 1, x))

    if y != len(data) - 1:
        neighbours.append((y + 1, x))

    if x != 0:
        neighbours.append((y, x - 1))

    if x != len(data[0]) - 1:
        neighbours.append((y, x + 1))

    return neighbours


def find_low_points(data):
    """ Find points in the grid that are local minimums.
        We check vertical and horizontal neighbours
        Diagonal neighbours are ignored.
    """
    local_mins = []
    for y, _ in enumerate(data):
        for x, _ in enumerate(data[0]):
            neighbours = find_neighbours(data, x, y)
            if all(data[i[0]][i[1]] > data[y][x] for i in neighbours):
                local_mins.append({
                    'x': x, 'y': y, 'val': data[y][x]})
                print(f"x={x}, y={y}, {data[y][x]} is a local min")
    return local_mins


def large_neighbours(data, x, y, results):
    """ Return a list of neighbours
        that are higher than the given point

        Do not include those with height==9

        Call this recursively to walk the whole tree
        Add high points as tuples to a results list
    """
    neighbours = find_neighbours(data, x, y)
    for n in neighbours:
        d = data[n[0]][n[1]]
        if 9 > d > data[y][x]:
            if n not in results:
                results.append(n)
                large_neighbours(data, n[1], n[0], results)
    return results


def multiply_list(data):
    """ Multiply elements of a list together
    """
    res = 1
    for d in data:
        res *= d
    return res

def main():
    """ Main Program
    """

    # Part 1
    data = load_data(INPUT)
    print_grid(data)
    low_points = find_low_points(data)
    vals = [x['val'] for x in low_points]
    risk_level = sum([x+1 for x in vals])
    print(f"Part 1: Risk Level = {risk_level}")

    # Part 2
    basin_sizes = []
    for lp in low_points:
        basin = large_neighbours(data, lp['x'], lp['y'], [])
        basin_sizes.append(len(basin) + 1)
    basin_sizes = sorted(basin_sizes)
    print(basin_sizes)
    ans = multiply_list(basin_sizes[-3:])
    print(f"Part 2: Basin product = {ans}")


if __name__ == ("__main__"):
    main()
