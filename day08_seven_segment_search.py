#!/usr/bin/env python3
"""

Advent of Code 2021: Day 8: Seven Segment Search
https://adventofcode.com/2021/day/8

"""


TEST_INPUT = 'data/day08_test_data.txt'
INPUT = 'data/day08_data.txt'


SEG_LOOKUP = {
    'abcefg': "0",
    'cf': "1",
    'acdeg': "2",
    'acdfg': "3",
    'bcdf': "4",
    'abdfg': "5",
    'abdefg': "6",
    'acf': "7",
    'abcdefg': "8",
    'abcdfg': "9"
}

SEG_COUNT = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}


def load_data(filename):
    """ Load data into a list
    """
    patterns = []
    digits = []

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            pattern, digit = line.strip().split('|')
            pattern = pattern.strip().split(' ')
            digit = digit.strip().split(' ')
            patterns.append([''.join(sorted(d)) for d in pattern])
            digits.append([''.join(sorted(d)) for d in digit])
    return patterns, digits


def count_digits(digits: list, nums: list) -> int:
    """ Count the number of digits that have x segments
    """
    num_segs = [SEG_COUNT[num] for num in nums]
    digs = [d for d_row in digits for d in d_row if len(d) in num_segs]
    return len(digs)

# Segments b,e,f can be found by counting.
# Segments c,f are in digit 1 which is only digit
# with 2 segments
# We know f so c is the other one.
# we know a from digit 7 (only digit with 3).  The other two
# are c,f (already known)
# So we know a,b,c,e,f
# Digit 4 gives d
# remaining must be g.


def segment_bef(patterns):
    """ Work out the segment frequencies in
        the given digits

        b,e,f segments have unique occurence
        counts in the digits 0-9
        a,c,d,g have non-unique counts.
        a,c = 8
        d,g = 7
        b=6, e=4, f=9
    """
    seg_data = "".join(patterns)
    counts = {a: seg_data.count(a) for a in seg_data}

    seg_freqs = {6: 'b', 4: 'e', 9: 'f'}

    results = {}
    for k in counts:
        results[k] = seg_freqs.get(counts[k])

    return results


def segment_c(patterns, seg_map):
    """ Segments c,f are in digit 1 which is only digit
        with 2 segments
    """
    two = [d for d in patterns if len(d) == 2][0]
    c_seg = [seg for seg in two if not seg_map[seg]]
    assert len(c_seg) == 1
    seg_map[c_seg[0]] = 'c'
    return seg_map


def segment_a(patterns, seg_map):
    """ Find Number 7 - the only one with 3 segments
        We already know the mapping for 2 so the remaining
        one is segment a.
    """
    seven = [d for d in patterns if len(d) == 3][0]
    a_seg = [seg for seg in seven if not seg_map[seg]]
    assert len(a_seg) == 1
    seg_map[a_seg[0]] = 'a'
    return seg_map


def segment_d(pattern, seg_map):
    """ Find segment d from digit 4
    """
    four = [d for d in pattern if len(d) == 4][0]
    d_seg = [seg for seg in four if not seg_map[seg]]
    assert len(d_seg) == 1
    seg_map[d_seg[0]] = 'd'
    return seg_map


def segment_g(seg_map):
    """ Segment g must be final segment
    """
    assert len([seg_map[k] for k in seg_map if not seg_map[k]]) == 1
    seg_map = {k: (v if v else 'g') for k, v in seg_map.items()}
    return seg_map


def find_segment_map(pattern):
    """ Find the segment mapping
    """
    seg_map = segment_bef(pattern)
    seg_map = segment_c(pattern, seg_map)
    seg_map = segment_a(pattern, seg_map)
    seg_map = segment_d(pattern, seg_map)
    seg_map = segment_g(seg_map)
    # print(seg_map)
    return seg_map


def build_digit(digit_data, seg_map):
    """ Take the scrambled digit data and work out which
        digit it is using the seg_map and then lookup
        the digit in the segment lookup table
    """

    num = ''
    for digit in digit_data:
        seg_data = ""
        for seg in digit:
            seg_data += seg_map[seg]
        digit = "".join(sorted(seg_data))
        digit_str = SEG_LOOKUP[digit]
        num += digit_str
    return int(num)


def main():
    """ Main Program
    """

    # Part 1
    patterns, digits = load_data(INPUT)
    count = count_digits(digits, [1, 4, 7, 8])
    print()
    print(f"Part 1: Digit count: {count}")
    assert count == 452

    # Part 2
    numbers = []
    for i, digit_vals in enumerate(digits):
        seg_map = find_segment_map(patterns[i])
        num = build_digit(digit_vals, seg_map)
        # print(num)
        numbers.append(num)
    # print(numbers)
    print(f"Part 2: Digit sum: {sum(numbers)}")
    assert sum(numbers) == 1096964


if __name__ == ("__main__"):
    main()
