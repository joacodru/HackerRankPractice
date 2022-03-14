#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ordered = []
    pairs = 0
    color = 0
    for i in range (1,n-1):
        color = ar[i]
        print ("position")
        print (i)
        print ("color")
        print(color)
        print ("-.---------------------")
        if color not in ordered:
            if (ar.count(color) % 2 == 0) & (ar.count(color) >= 2):
                ordered.append(color)
                pairs = pairs + ar.count(color) / 2
            elif ar.count(color) >= 2:
                ordered.append(color)
                pairs = pairs + ((ar.count(color)-1)/2)
    return int(pairs)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
