#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    sp = s.split(":")
    if sp[2][-2:] == "PM":
        if sp[0] != "12":
            sp[0] = str(int(sp[0]) + 12)
    else:
        if sp[0] == "00":
            sp[0] = "24"
        elif sp[0] == "12":
            sp[0] = "00"
    res = sp[0] + ":" + sp[1] + ":" + sp[2][:2]
    return(res)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
