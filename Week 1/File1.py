# -*- coding: utf-8 -*-
"""
Created on 12/11/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

# Greedy algorithm for knapsack problem
# Approximated solution
"""
while knapsack not full
    put "best" available item in knapsack

But which item is the best?
1.Most valuable
2.Least expensive (weight)
3.Highest value/units (value/weight)
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
        return self.name + ': <' + str(self.getValue()) \
               + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    """
    names, values, calories lists of same length
    :param names: a list of strings
    :param values: a list of numbers
    :param calories: a list of numbers
    :return: lists of Foods
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def greedy(items, maxCost, keyFunction):
    """
    :param items: a list of Foods
    :param maxCost: number >= 0
    :param keyFunction: maps elements of items to numbers
    :return: a tuple of the lists of items selected and the total value
    """
    # It should sort the list from worst to best but the reverse key
    # makes it from best to worst
    # n log(n)
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    # m
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getCost()
    # O(n log(n))
    return result, totalValue


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('    ', item)


def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('Use greedy by cost to allocate', maxUnits, 'calories')
    # x takes the place of self
    testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))
    print('Use greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)


"""
lambda is used to create anonymous functions, don't have names
"""
f1 = lambda x: x
f1(3)
f1('string')

f2 = lambda x, y: x + y
f2(2, 3)
f2('Amaury', 'Ortega')

f3 = lambda x, y: 'factor' if (x % y == 0) else 'no factor'
f3(4, 2)
f3(4, 3)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]

foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
testGreedys(foods, 1000)

trips = []
cows_copy = {}
cows_copy = cows.copy()
cows_copy = [(name, cows_copy[name]) for name in sorted(cows_copy, key=cows_copy.get, reverse=True)]

weight = 0
while weight <= limit:
    # Each trip
    weight = 0
    trip = []
    for cow, value in cows_copy:
        if weight + value <= limit:
            trip.append(cow)
            cows_copy.remove((cow, value))
    trips.append(trip)
