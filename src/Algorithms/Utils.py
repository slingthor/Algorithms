__author__ = 'ingthor'

import random


def RandomArray(n):
    testA = []
    for i in range(0, n):
        testA.append(random.randint(0, n))
    return testA
