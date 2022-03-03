#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0
    for x in arr:
        if x > 0:
            positive += 1
        elif x < 0:
            negative += 1
        elif x == 0:
            zeros += 1
    print("{:.6f}".format(positive/n))
    print("{:.6f}".format(negative/n))
    print("{:.6f}".format(zeros/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
