#!/usr/bin/env python3
"""

Advent of Code 2021: Day1
https://adventofcode.com/2021/day/1

"""
INPUT = 'data/day01_data.txt'


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            data.append(int(line.strip()))
    return data


def count_increasing(data):
    """ Count number of entries that are large than the previous
    """
    count = 0
    for i, val in enumerate(data[1:]):
        if val > data[i]:
            count += 1
    return count


def create_windowed_data(data):
    """  Create a new list of windowed data
    """
    windowed_data = []
    for i in range(len(data)-2):
        windowed_data.append(sum(data[i:i+3]))
    return windowed_data


def main():
    """ Main Program
    """
    data = load_data(INPUT)
    inc_count = count_increasing(data)
    w_data = create_windowed_data(data)
    w_inc_count = count_increasing(w_data)

    assert len(data) == 2000
    assert inc_count == 1692
    assert w_inc_count == 1724

    print(f"Length of data  = {len(data)}")
    print(f"Number of increasing counts = {inc_count}")
    print(f"Number of increasing window counts = {w_inc_count}")


if __name__ == ("__main__"):
    main()
