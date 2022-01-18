# Problem URL:
# https://www.hackerrank.com/challenges/special-multiple/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def solve(n):
    L = [9*int(str(bin(i))[2:]) for i in range(1,n+1)]
    c = 1
    while True:
        new_c = 9*int(str(bin(c))[2:])
        if new_c % n == 0:
            return str(new_c)    
        c += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
