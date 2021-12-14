#!/usr/bin/env python3
"""

Advent of Code 2021:  Day 14: Extended Polymerization
https://adventofcode.com/2021/day/14

"""


TEST_INPUT = 'data/day14_test_data.txt'
TEST_INPUT_2 = 'data/day14_test_data_2.txt'
INPUT = 'data/day14_data.txt'

"""
Naive approach of building the polymer does not work for step 2 since we
need to build (2^n * 3) + 1, which is mahoosive

Alernative approach is to keep a count of the pairs in the polymer

NNCB = NN:1, NC:1, CB:1
NCNBCHB = NC:1, CN:1, NB:1, BC:1, CH:1, HB:1

This count list can be extended for each round and will always
be much smaller that the polymer list since there are limited
numbers of letters e.g. for 20 letters there are only 150 combinations
of 2 letters (actually might be 20 more than this since we allow
combinations of the same letters AA, BB etc)

On each iteration we break the pairs in 2 e.g. NN -> C:
NN -> NC + CN
We have a limited number of letter combinations and many of them
map to the same insertion char.

So on each iteration we split the pairs and keep a count of their
occurrences.  We can also keep a count of the chars in the polymer
and when we insert a char with can increment the count.

"""


def load_data(filename):
    """ Load data into a list
        Return the following:
            The template string
            count of chars in template
            insertion pairs in a dict
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

        template = lines[0]
        c_count = {c: template.count(c) for c in template}

        p_count = {}
        for i, _ in enumerate(template[:-1]):
            pair = template[i: i+2]
            p_count[pair] = p_count.get(pair, 0) + 1

        pairs = {}
        for line in lines[1:]:
            if ' -> ' in line:
                k, val = line.split(' -> ')
                pairs[k] = val

    return p_count, c_count, pairs


def inc_dict(my_dict, d_key, d_val):
    """  Add d_val to the dict entry with key=d_key
          If key does not exits then create it and
          set it equal to d_val
    """
    my_dict[d_key] = my_dict.get(d_key, 0) + d_val


def polymerise(p_count, c_count, pairs, steps):
    """ For each pair insert the relevant char
        to form 2 new pairs and ...
        a) Increment the count of the 2 new pairs
        b) Increment the count of the inserted char
    """

    for _ in range(steps):
        new_p_count = {}
        for pair, cnt in p_count.items():
            new_ch = pairs[pair]
            inc_dict(new_p_count, pair[0]+new_ch, cnt)
            inc_dict(new_p_count, new_ch+pair[1], cnt)
            inc_dict(c_count, new_ch, cnt)
        p_count = new_p_count

    return max(c_count.values()) - min(c_count.values())


def main():
    """ Main Program
    """

    # Part 1
    p_count, c_count, pairs = load_data(INPUT)
    score = polymerise(p_count, c_count, pairs, 10)
    print(f"Part1: Score after polymerisation: {score}")

    # Part 2
    p_count, c_count, pairs = load_data(INPUT)
    score = polymerise(p_count, c_count, pairs, 40)
    print(f"Part2: Score after polymerisation: {score}")


if __name__ == ("__main__"):
    main()
