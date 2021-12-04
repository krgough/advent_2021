#!/usr/bin/env python3
"""

Advent of Code 2021: Day 4: Giant Squid
https://adventofcode.com/2021/day/4

"""
TEST_INPUT = 'data/day04_test_data.txt'
INPUT = 'data/day04_data.txt'


def load_data(filename):
    """ Load data into a list
    """
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    return data


def initialise_data(data):
    """ Parse the 'called' numbers and bingo cards
    """
    # Called numbers in first row
    nums = data[0].split(',')
    cards = []

    # First row of cards data is in row 2
    # extract the number of columns
    num_cols = len(data[2].split())

    # Skip the called_numbers row and first
    # blank line separator
    data = data[2:]
    card_data = []
    for row in data:
        if row:
            card_data += row.split()
        else:
            cards.append(card_data)
            card_data = []

    return nums, cards, num_cols


def transpose_matrix(matrix):
    """ Transpose a list of lists (matrix)
        Example as follows..

        Input:
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        Transposed:
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    # test_data
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    return [list(i) for i in zip(*matrix)]


def flatten(matrix):
    """ Flatten a list of lists
    """
    return [j for sub_list in matrix for j in sub_list]


def pile(matrix, num_cols):
    """ Build a list of lists with given row length
    """
    return [matrix[i: i + num_cols] for i in range(0, len(matrix), num_cols)]


def mark_card(card, card_marked, num):
    """ We maintain a 'marked' card for each bingo card
        The marked card consists of a matrix where
        0 = number not called
        1 = number called
        As each number is called we update the marked
        card and return it.
    """

    try:
        index = card.index(num)
        card_marked[index] = 1
    except ValueError:
        pass
    return card_marked


def check_marked_card(marked_card, num_cols):
    """ Check marked card for completed rows or columns
    """
    card = pile(marked_card, num_cols)

    # Check for rows
    for row in card:
        if all(row):
            return True

    # Check for columns
    card = transpose_matrix(card)
    for row in card:
        if all(row):
            return True

    return False


def lets_play_bingo(nums, cards, num_cols):
    """ Find the first card to get a complete row/column
    """
    win_index = []
    win_num = []
    marked_cards = [[0 for j in range(len(cards[0]))]
                    for i in range(len(cards))]

    for num in nums:
        for i, card in enumerate(cards):
            if i not in win_index:
                try:
                    marked_cards[i][card.index(num)] = 1
                except ValueError:
                    pass

                win = check_marked_card(marked_cards[i], num_cols)
                if win:
                    win_index.append(i)
                    win_num.append(num)

    return win_index, win_num, marked_cards


def calc_score(card, m_card, num):
    """ Calculate score by creating sum of all marked
        numbers and multiply that by the final called
        number.
    """
    score = sum([int(v) for i, v in enumerate(card) if m_card[i] == 0])
    return score * int(num)


def main():
    """ Main Program

        Bingo card wins if any row or column is complete

    """

    data = load_data(INPUT)
    nums, cards, num_cols = initialise_data(data)

    win_index, win_num, m_cards = lets_play_bingo(nums, cards, num_cols)

    # First Winning Card
    card = cards[win_index[0]]
    num = win_num[0]
    m_card = m_cards[win_index[0]]
    score = calc_score(card, m_card, num)
    print(f'First Winning Score: {score}')

    # Last Winning Card
    card = cards[win_index[-1]]
    num = win_num[-1]
    m_card = m_cards[win_index[-1]]
    score = calc_score(card, m_card, num)
    print(f'Last Winning Score: {score}')


if __name__ == ("__main__"):
    main()
