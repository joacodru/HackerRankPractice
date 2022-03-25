#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
#summer + 1
#spring x2
#sapling = 1

def utopianTree(n):
    treeHeight = 1
    for period in range(n):
        if period % 2 == 0:
            treeHeight *= 2
            
        elif period % 2 != 0: 
            treeHeight += 1
    return treeHeight

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
