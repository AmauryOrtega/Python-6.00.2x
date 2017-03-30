# -*- coding: utf-8 -*-
"""
Created on 29/03/2017

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


# Answer:
def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.
    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    N = len(items)
    # Enumerate the 3**N possible combinations
    for i in range(3 ** N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)


def powerSet2(items):
    """
    items: list of items
    returns: generator capable of giving all the combinations of items
    """

    # Importing chain and combinations from itertools to make the power set
    from itertools import chain, combinations
    # Making each combination for a given list of items
    for combination in chain.from_iterable(combinations(items, r) for r in range(len(items) + 1)):
        # Yielding each combination as a list
        yield list(combination)


# Testing
a = powerSet2([1, 2, 3, 4, 5])
for combination in a:
    print(combination)
