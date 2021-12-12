#!/usr/bin/env python3
"""

Advent of Code 2021: Day3
https://adventofcode.com/2021/day/3

"""
INPUT = 'data/day03_data.txt'

TEST_DATA = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    return data


def count_bits_by_index(data):
    """ For each bit position in each word in data
        count how many bits are set

        Example:

        001
        010
        110
        110

        231

        Returns a list of counts in reverse order i.e.

        [1, 3, 2]

    """
    word_len = len(data[0])
    counts = [0] * word_len

    for i in range(word_len):
        bit_val = 0x01 << i
        for word in data:
            if int(word, 2) & bit_val:
                counts[i] += 1

    return counts


def find_gamma_epsilon(data):
    """ Count bits by index and then convert those to gamma and epsilon

        gamma = if more 1's than zeros then gamma bit is 1
                else 0

        epsilon = inverse of gamma
    """
    bit_counts_by_index = count_bits_by_index(data)
    gamma = 0
    for i, val in enumerate(bit_counts_by_index):
        if val > len(data) / 2:
            gamma |= 0x01 << i
    epsilon = ~gamma & (2**len(data[0]) - 1)
    return gamma, epsilon


def find_o2_rating(data):
    """  For O2 rating:

         Determine the most common value (0 or 1) in the current bit position,
         and keep only numbers with that bit in that position. If 0 and 1 are
         equally common, keep values with a 1 in the position being considered.
    """
    i = 0
    my_data = data.copy()
    while len(my_data) > 1:
        b_counts = count_bits_by_index(my_data)[::-1]
        if b_counts[i] >= len(my_data) / 2:
            my_data = [d for d in my_data if d[i] == '1']
        else:
            my_data = [d for d in my_data if d[i] == '0']
        i += 1
    return my_data[0]


def find_co2_scrub_rating(data):
    """  For CO2 Scrub rating:

         Determine the lest common value (0 or 1) in the current bit position,
         and keep only numbers with that bit in that position. If 0 and 1 are
         equally common, keep values with a 0 in the position being considered.
    """
    i = 0
    my_data = data.copy()
    while len(my_data) > 1:
        b_counts = count_bits_by_index(my_data)[::-1]
        if b_counts[i] < len(my_data) / 2:
            my_data = [d for d in my_data if d[i] == '1']
        else:
            my_data = [d for d in my_data if d[i] == '0']
        i += 1
    return my_data[0]


def main():
    """ Main Program
    """
    data = load_data(INPUT)

    # Power Consumption
    # data = TEST_DATA
    gamma, epsilon = find_gamma_epsilon(data)
    power_consumption = gamma * epsilon

    print(f"Gamma:               {gamma:012b}, {gamma}")
    print(f"Epsilon:             {epsilon:012b}, {epsilon}")
    print(f"Power consumption:   {epsilon * gamma}")

    # Life Support Rating
    o2_rating = find_o2_rating(data)
    co2_scrub = find_co2_scrub_rating(data)
    life_support_rating = int(o2_rating, 2) * int(co2_scrub, 2)
    print(f"O2 Rating:           {o2_rating}")
    print(f"CO2 Scrub Rating:    {co2_scrub}")
    print(f"Life Support Rating: {life_support_rating}")

    assert power_consumption == 4147524


if __name__ == ("__main__"):
    main()
