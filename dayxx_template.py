#!/usr/bin/env python3
"""

Advent of Code 2021:  Day xx
https://adventofcode.com/2021/day/xx

"""

TEST_INPUT = 'data/dayxx_test_data.txt'
TEST_INPUT_2 = 'data/dayxx_test_data_2.txt'
INPUT = 'data/dayxx_data.txt'


def load_data(filename):
    """ Load data into a list
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        data = [line.strip().split(',') for line in file]

    return data


def main():
    """ Main Program
    """

    # Part 1
    data = load_data(INPUT)
    print(data)

    # Part 2


if __name__ == ("__main__"):
    main()
