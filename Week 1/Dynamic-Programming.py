# -*- coding: utf-8 -*-
"""
Created on 29/03/2017

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


# Fibonacci example
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Fibonacci example
def fast_fib(n, memo={}):
    """
    :param n: an int >= 0
    :param memo: used only by recursive calls
    :return: Fibonacci of n
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n - 1, memo) + fast_fib(n - 2, memo)
        memo[n] = result
        return result


# ----------------------------------------------------------------------------------------------------------------------
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    """
    names, values, calories are lists of same length.
    names a list of strings
    values and calories lists of numbers
    return list of Foods
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def fast_maxVal(toConsider, available, memo={}):
    """
    :param toConsider: list of items to consider
    :param available: available weight
    :param memo:
                Used only by recursive calls. The key of this set is a
                tuple (items left to be considered, available weight)
                Items left to be considered will be represented by len(toConsider)
                because with this number, you can tell which items are represented in this case
    :return: a tuple of the total value of a solution to 0/1 knapsack problem and the items of that solution
    :summary:
        1) check if optimal choice of items given the available weight is in memo
        2) at the end, memo has to be updated
    """
    if (len(toConsider), available) in memo:
        result = memo[(len(toConsider), available)]
    elif toConsider == [] or available == 0:
        result = (0, ())
    elif toConsider[0].getCost() > available:
        # The item doesn't fit so only the right node is considered
        result = fast_maxVal(toConsider[1:], available)
    else:
        nextItem = toConsider[0]

        # withVal and withTaken are the value and the items taken up to this node (left node)
        withVal, withTaken = fast_maxVal(toConsider[1:], available - nextItem.getCost())
        withVal += nextItem.getValue()

        # withoutVal and withoutTaken are the value and the items taken up to this node (right node)
        withoutVal, withoutTaken = fast_maxVal(toConsider[1:], available)

        # Choose the best node
        if withVal > withoutVal:
            result = (withVal, withTaken + (nextItem,))
        else:
            result = (withoutVal, withoutTaken)
    memo[(len(toConsider), available)] = result
    return result


def testMaxVal(foods, maxUnits, algorithm, printItems=True):
    print('Use search tree to allocate', maxUnits, 'calories')
    value, taken = algorithm(foods, maxUnits)
    print('Total value of item taken =', value)
    if printItems:
        for item in taken:
            print(' ', item)


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testMaxVal(foods, 750, fast_maxVal)

# Testing larger examples

import random


def buildLargeMenu(numberItems, maxValue, maxCost):
    items = []
    for i in range(numberItems):
        items.append(
            Food(str(i),
                 random.randint(1, maxValue),
                 random.randint(1, maxCost))
        )
    return items


for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
    print("numItems:", numItems)
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 760, fast_maxVal, False)
    print()
