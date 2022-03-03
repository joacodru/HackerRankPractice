#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    count = [0,0]
    min = 0
    max = 0
    for position in range (len(scores)):
        if position == 0 :
            min = scores[position]
            max = scores[position]
            next
        if min > scores[position] :
            min = scores[position]
            count[1] += 1
        if max < scores[position] :
            max = scores[position]
            count[0] += 1 
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
