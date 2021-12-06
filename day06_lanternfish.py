#!/usr/bin/env python3
"""

Advent of Code 2021: Day 6: Lanternfish
https://adventofcode.com/2021/day/6

"""


TEST_INPUT = 'data/day06_test_data.txt'
INPUT = 'data/day06_data.txt'


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            data += line.strip().split(',')

    data = [int(i) for i in data]
    return data


def iterate_day(ages):
    """ Iterate the simulation by one day
        Each fish gets one day older (age is decremented)
        Any fish reaching day 6 causes a new fish to be born
        New fish has age of 8 (to simulate juvenile)
        Any fish with age 0 resets to age 6

        After a certain time the size of our list become huge
        but since all fish of the same age behave the same we can
        group them by age

        Function returns new list with updated ages extended in length
        by any new births
    """
    # Rotate the age list to 'age' each fish another day
    ages_zero = ages.pop(0)
    ages[6] = ages[6] + ages_zero

    # Since we popped the zero'th the list
    # is only 7.  We add the new births into
    # posn 8
    ages.append(ages_zero)

    # new_fish = 0
    # for i, fish in enumerate(new_data):
    #     # Fish age reduces by one day
    #     fish = fish - 1

    #     # At end of cycle loop back to 6
    #     if fish < 0:
    #         fish = 6
    #         new_fish += 1

    #     new_data[i] = fish

    # for i in range(new_fish):
    #     new_data.append(8)

    return ages


def run_simulation(data, days):
    """ Run the simulation for x days """
    ages = [data.count(i) for i in range(9)]
    for _ in range(days):
        ages = iterate_day(ages)
        # print(data)
    return sum(ages)


def main():
    """ Main Program

        Bingo card wins if any row or column is complete

    """
    data = load_data(INPUT)
    days = 80
    count = run_simulation(data, days)
    print(f'Fish count after {days} days: {count}')
    assert count == 345387

    data = load_data(INPUT)
    days = 256
    count = run_simulation(data, days)
    print(f'Fish count after {days} days: {count}')
    assert count == 1574445493136


if __name__ == ("__main__"):

    main()
