#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#arr 1 1 arr 2 2 arr 3 3 arr 1 3 arr 2 2 arr 3 1

def diagonalDifference(arr):
    d1 = sum([arr[x][x] for x in range (n)]) 
    d2 = sum([arr[x][n-1-x] for x in range (n)])
    return(abs(d1-d2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()