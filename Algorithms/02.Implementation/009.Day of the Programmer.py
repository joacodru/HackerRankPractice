#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    if 1700 <= year < 1918:
        if year % 4 == 0:
            res = '12.09.' + str(year)
        else:
            res = '13.09.' + str(year)
    elif 1918 < year <= 2700:
        if year % 400 == 0:
            res = '12.09.' + str(year)
        elif (year % 4 == 0) & (year % 100 != 0):
            res = '12.09.' + str(year)
        else:
            res = '13.09.' + str(year)
    else:
        res = '26.09.' + str(year)
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
