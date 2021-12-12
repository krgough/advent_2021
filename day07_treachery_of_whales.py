#!/usr/bin/env python3
"""

Advent of Code 2021: Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7

"""


TEST_INPUT = 'data/day07_test_data.txt'
INPUT = 'data/day07_data.txt'


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            data += line.strip().split(',')

    data = [int(i) for i in data]
    return data


def addatorial_func(num):
    """ sum = 5 + 4 + 3 + 2 + 1

               n^2 + n
        sum  = -------
                  2
    """
    return int((num**2 + num) / 2)


def unity_func(num):
    """ Return myself
    """
    return num


def calc_deltas(data, func):
    # pylint: disable=invalid-name
    """ Find the minimum moves required to move
        all numbers to a single number
    """
    consumptions = []
    for i in range(max(data) + 1):
        x = sum([func(abs(i - a)) for a in data])
        consumptions.append(x)
    return consumptions


def main():
    """ Main Program
    """
    # data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    # Part 1
    data = load_data(INPUT)
    consumption = min(calc_deltas(data, unity_func))
    print(f"Minimum Consumption: {consumption}")
    assert consumption == 341558

    # Part 2
    data = load_data(INPUT)
    consumption = min(calc_deltas(data, addatorial_func))
    print(f"Minimum Consumption: {consumption}")
    assert consumption == 93214037


if __name__ == ("__main__"):
    main()
