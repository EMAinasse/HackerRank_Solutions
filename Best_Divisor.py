#Problem URL:
# https://www.hackerrank.com/challenges/best-divisor/

#!/bin/python3

import math
import os
import random
import re
import sys

def best_num(n):
    best = 1
    for i in range(2,n+1):
        if n % i == 0:
            if sum([int(j) for j in str(i)]) > sum([int(j) for j in str(best)]):
                best = i
            elif sum([int(j) for j in str(i)]) == sum([int(j) for j in str(best)]):
                best = min(best,i)
    return best

if __name__ == '__main__':
    n = int(input().strip())
    print(best_num(n))
