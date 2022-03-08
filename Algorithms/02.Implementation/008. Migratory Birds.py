#!/bin/python3

import sys
from collections import Counter

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
p = Counter(types)
maxV = max(p.values())
sight = [k for k,v in p.items() if v == maxV]
print(min(sight))
