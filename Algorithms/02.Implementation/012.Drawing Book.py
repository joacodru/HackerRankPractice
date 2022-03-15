#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    if p % 2 != 0:
        pages = p - 1
    else:
        pages = p
    minPages = 0
    if n % 2 == 0:
        if n / 2 >= pages:
            minPages = pages / 2
        else:
            minPages = (n - pages) / 2
    else:
        if (n - 1) / 2 >= pages:
            minPages = pages / 2
        else:
            minPages = (n - pages) / 2
    return int(minPages)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
