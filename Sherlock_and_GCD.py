# Problem URL:
# https://www.hackerrank.com/challenges/sherlock-and-gcd/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    # Write your code here
    if reduce(math.gcd,set(a)) == 1 and len(set(a)) > 1:
        return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
