#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    specials = 0
    page = 1
    space = 0
    problem = 1
    chapter = 0
    while chapter <= n - 1:
        if problem == page:
            specials += 1
        if problem < arr[chapter]:
            problem += 1
            space += 1
        else:
            problem = 1
            chapter += 1
            space = 0
            page += 1
        if space == k:
            space = 0
            page += 1
    return specials

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
