#!/usr/bin/env python3
"""

Advent of Code 2021: Day2
https://adventofcode.com/2021/day/2

"""
INPUT = 'data/day02_data.txt'

TEST_DATA = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    return data


def track_position(data):
    """ Process the input data to calculate final position
    """
    depth = 0

    forward = [int(i.split(' ')[1]) for i in data if i.startswith('forward')]
    down = [int(i.split(' ')[1]) for i in data if i.startswith('down')]
    up = [int(i.split(' ')[1]) for i in data if i.startswith('up')]
    h_pos = sum(forward)
    depth = sum(down) - sum(up)
    return h_pos, depth


def aim_position(data):
    """ Process intut data to calculate the final position
        based on the new rules

        down x : aim = aim + x
        up x : aim = aim - x
        forward x : h_pos = h_pos + x,  depth = aim * x
    """
    aim = 0
    depth = 0
    h_posn = 0

    for i in data:
        inst, dist = i.split(' ')
        x = int(dist.strip())
        inst = inst.strip()
        if inst.startswith('forward'):
            h_posn += x
            depth += aim * x
        if inst.startswith('down'):
            aim += x
        if inst.startswith('up'):
            aim -= x
    return h_posn, depth


def main():
    """ Main Program
    """
    data = load_data(INPUT)
    h_pos, depth = track_position(data)
    print('Simple Position Calculation:')
    print(f"Horizontal Position = {h_pos}")
    print(f"Depth = {depth}")
    print(f"H_Posn * depth = {h_pos * depth}")

    assert h_pos * depth == 1855814

    print('')
    print('Modified Position Calculation:')
    h_pos, depth = aim_position(data)
    print(f"Horizontal Position = {h_pos}")
    print(f"Depth = {depth}")
    print(f"H_Posn * depth = {h_pos * depth}")

    assert h_pos * depth == 1845455714


if __name__ == ("__main__"):
    main()
