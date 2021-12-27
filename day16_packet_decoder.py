#!/usr/bin/env python3
"""

Advent of Code 2021:  Day 16: Packet Decoder
https://adventofcode.com/2021/day/16

"""

TEST_INPUT = 'data/day16_test_data.txt'
TEST_INPUT_1 = 'data/day16_test_data_1.txt'
TEST_INPUT_2 = 'data/day16_test_data_2.txt'
INPUT = 'data/day16_data.txt'


def load_data(filename):
    """ Load data into a list
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        data = file.readline()

    return f"{int(data, 16):b}"


def decode_literal(pkt):
    """ Decode literal values
    """
    i = 6
    literal = pkt[i+1:i+5]
    while pkt[i] == '1':
        i += 5
        next_blk = pkt[i+1:i+5]
        literal += next_blk

    return literal


def decode(pkt, start, ver_sum):
    """ Decode the packet
    """
    ver = int(pkt[start:start+3], 2)
    p_type = int(pkt[start+3:start+6], 2)
    print(ver, p_type)
    ver_sum = ver_sum + ver

    # If literal then decode
    if p_type == 4:
        l_val = decode_literal(pkt)
        print(int(l_val, 2))

    # If sub_pkts then return the sub_pkts
    else:
        l_val = None
        # If we know the number of pkts
        for pkt in range()

    return

def main():
    """ Main Program
    """

    # Part 1
    # data = load_data(INPUT)
    # print(data)

    pkt = load_data(TEST_INPUT_1)
    pkt = load_data(INPUT)
    print(pkt)
    decode(pkt, start=0)
    print(len(pkt))

    # Part 2


if __name__ == ("__main__"):
    main()
