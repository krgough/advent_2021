#!/usr/bin/env python3
"""

Advent of Code 2021: Day 12: Passage Pathing
https://adventofcode.com/2021/day/12

"""

TEST_INPUT = 'data/day12_test_data.txt'
TEST_INPUT_2 = 'data/day12_test_data_2.txt'
INPUT = 'data/day12_data.txt'


def load_data(filename):
    """ Load data into a list
    """
    nodes = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().split('-')
            try:
                nodes[line[0]].append(line[1])
            except KeyError:
                nodes[line[0]] = [line[1]]

            try:
                nodes[line[1]].append(line[0])
            except KeyError:
                nodes[line[1]] = [line[0]]

    return nodes


def allowed_cave(node, visited, max_visits):
    """ start can only be visited once
        end can only be visited once

        The first small cave can be visited twice
        Other small cave can be visited once
    """
    if node == 'start':
        return False
    if node.islower() and node in visited:
        # We have been here before.  Can we re-enter.
        small_caves = [c for c in visited if c.islower()]
        visit_count = max([small_caves.count(c) for c in small_caves])
        if visit_count >= max_visits:
            return False
    return True


def find_paths(node_exits, data, visited, routes, max_visits):
    """  Find all the paths through the directed graph
         from 'start' to 'end'
    """
    # For a given exit list move to each node
    # call myself again for each exit
    # Create a visited list and if the current node
    # is a small cave on the list then do nothing
    # If no more exits then do nothing
    # If exit is 'end' then print visited.

    for node in node_exits:
        if node == 'end':
            routes.append(visited)
        # elif node.islower() and node in visited:
        #     pass
        # else:
        #     new_visited = visited.copy()
        #     new_visited.append(node)
        #     exits = data[node]
        #     find_paths(exits, data, new_visited, routes)
        elif allowed_cave(node, visited, max_visits):
            new_visited = visited.copy()
            new_visited.append(node)
            exits = data[node]
            find_paths(exits, data, new_visited, routes, max_visits)

    return routes


def main():
    """ Main Program
    """

    # Part 1
    data = load_data(INPUT)
    routes = find_paths(data['start'],
                        data,
                        visited=['start'],
                        routes=[],
                        max_visits=1)
    print(f"Part1: Number of routes = {len(routes)}")

    # Part 2
    data = load_data(INPUT)
    routes = find_paths(data['start'],
                        data,
                        visited=['start'],
                        routes=[],
                        max_visits=2)
    print(f"Part2: Number of routes = {len(routes)}")


if __name__ == ("__main__"):
    main()
