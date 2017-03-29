# -*- coding: utf-8 -*-
"""
Created on 18/03/2017

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


def greedy(items, maxCost, keyFunction):
    """
    Assumes items is a list, maxCost >= 0
    keyFunction maps elements of items to numbers
    """
    # n log(n) in python
    itemsCopy = sorted(items, key=keyFunction, reverse=True)  # Best to worst according to keyFunction
    result = []
    totalValue, totalCost = 0.0, 0.0
    # n
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    # n log(n) + n = n log(n)
    return result, totalValue


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print(' ', item)


def testGreedyes(foods, maxUnits):
    print('Using greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)

    print('\nUsing greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))

    print('\nUsing greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedyes(foods, 750)
testGreedyes(foods, 1000)
