#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    factors = []
    for number in range (a[len(a)-1], b[0]+1):
        satisfies = True
        for x in a:
            if number%x == 0:
                satisfies &= True
            else:
                satisfies &= False
        for x in b:
            if x%number == 0:
                satisfies &= True
            else:
                satisfies &= False
        if satisfies:
            factors.append(number)
        
    return(len(factors))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
