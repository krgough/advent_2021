#!/usr/bin/env python3
"""

Advent of Code 2021: Day 10: Syntax Scoring
https://adventofcode.com/2021/day/10

"""

TEST_INPUT = 'data/day10_test_data.txt'
INPUT = 'data/day10_data.txt'

DELIMS = {
    '<': '>',
    '(': ')',
    '{': '}',
    '[': ']',
}

I_DELIMS = {v: k for k, v in DELIMS.items()}


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        data = [line.strip() for line in file]

    return data


def parse_syntax(data):
    """  Walk through a line and build a list
         of opening delimiters.  Remove delimiters
         from the list if the correct closing
         delimiter is found.

        Stop if no more delimiters (eol)
        or
        Stop if wrong closing delimiter found

        Return None if no errors or the incorrect
        delimiter char
    """
    delim_seq = []

    for char in data:
        # Is it a valid opening deliminator
        if char in I_DELIMS.values():
            delim_seq.append(char)

        # If it's a closing
        if char in I_DELIMS:
            opening = I_DELIMS[char]
            if delim_seq[-1] == opening:
                delim_seq.pop()
            else:
                return char, delim_seq

    return None, delim_seq


def closing_sequence(data):
    """ Find the sequence of closing delimiters for the
        given input.

        Iteratively walk through the input and delete
        adjacent pairs of open/close delims

        exit when a pass is made with no deletions
    """

    # Create a copy as we don't want to modify the list
    # we are iterating over
    result_list = data.copy()

    pair_found = True
    while pair_found:
        pair_found = False
        for i, char in enumerate(data[:-1]):
            if char in DELIMS and DELIMS[char] == data[i + 1]:
                pair_found = True
                result_list.pop(i + 1)
                result_list.pop(i)

    result_list.reverse()
    return result_list


def close_sequence_score(data):
    """ Calculate the closing sequence score

        For each char multiply score by 5 and add the following:

        ): 1 point
        ]: 2 points
        }: 3 points
        >: 4 points

    """
    # This is inverse to above and the sequence we have is the
    # reversed list of opening delimiters:
    score_lu = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    score = 0
    for char in data:
        score = (score * 5) + score_lu[char]
    return score


def whats_the_syntax_score(data):
    """ Count the score.
        Score values are:
          ) = 3 points
          ] = 57 points
          } = 1197 points
          > = 25137 points
    """
    score_lu = {")": 3, ']': 57, '}': 1197, '>': 25137}
    score = sum([score_lu[c] for c in data])
    return score


def main():
    """ Main Program
    """

    # Part 1
    data = load_data(INPUT)

    errors = []
    i_rows = []
    for row in data:
        result, seq = parse_syntax(row)
        if result:
            # print(row, f"ERROR: {result}")
            errors.append(result)
        else:
            # Need this for part 2
            i_rows.append(seq)
    score = whats_the_syntax_score(errors)
    print(f"Part1: Syntax Score: {score}")

    # print(f"Part 1: Risk Level = {risk_level}")

    # Part 2
    # Find all incomplete rows without syntax errors.
    # Build the correct closure sequence.  In our case we
    # return a reversed list of umatched opening delimiters.
    # Calculate score for the closure sequence
    scores = []
    for i_row in i_rows:
        res = closing_sequence(i_row)
        # print(res)
        score = close_sequence_score(res)
        scores.append(score)
    scores.sort()
    middle_score = scores[((len(scores) - 1) // 2)]
    print(f"Part2: Middle closing sequence score: {middle_score}")

    # Do above for all rows and find middle score
    # print(f"Part 2: Basin product = {ans}")


if __name__ == ("__main__"):
    main()
