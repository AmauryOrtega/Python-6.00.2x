# -*- coding: utf-8 -*-
"""
Created on 25/03/2017

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


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


def maxVal(toConsider, available):
    """
    toConsider: list of items
    available: available weight
    Returns: a tuple of the total value of a solution to 0/1 knapsack problem and the items of that solution
    """
    if toConsider == [] or available == 0:
        result = (0, ())
    elif toConsider[0].getCost() > available:
        # The item doesn't fit so only the right node is considered
        result = maxVal(toConsider[1:], available)
    else:
        nextItem = toConsider[0]

        # withVal and withTaken are the value and the items taken up to this node (left node)
        withVal, withTaken = maxVal(toConsider[1:], available - nextItem.getCost())
        withVal += nextItem.getValue()

        # withoutVal and withoutTaken are the value and the items taken up to this node (right node)
        withoutVal, withoutTaken = maxVal(toConsider[1:], available)

        # Choose the best node
        if withVal > withoutVal:
            result = (withVal, withTaken + (nextItem,))
        else:
            result = (withoutVal, withoutTaken)

    return result


def testMaxVal(foods, maxUnits, printItems=True):
    print('Use search tree to allocate', maxUnits, 'calories')
    value, taken = maxVal(foods, maxUnits)
    print('Total value of item taken =', value)
    if printItems:
        for item in taken:
            print(' ', item)


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testMaxVal(foods, 750)

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
    testMaxVal(items, 760, False)
    print()
