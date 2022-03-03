#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
#s: integer, starting point of Sam's house location.
#t: integer, ending location of Sam's house location.
#a: integer, location of the Apple tree.
#b: integer, location of the Orange tree.
#apples: integer array, distances at which each apple falls from the tree.
#oranges: integer array, distances at which each orange falls from the tree.

def countApplesAndOranges(s, t, a, b, apples, oranges):
    orangesN = 0
    applesN = 0
    for i in range(len(apples)):
        if (((a + apples[i]) >= s) and ((a + apples[i]) <= t)):
            applesN += 1
    for i in range(len(oranges)):
        if (((b + oranges[i]) >= s) and ((b + oranges[i]) <= t)):
            orangesN += 1
            
    print(applesN)
    print(orangesN)
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
