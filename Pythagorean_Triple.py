# Problem URL:
# https://www.hackerrank.com/challenges/pythagorean-triple/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pythagoreanTriple' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER a as parameter.
#

def pythagoreanTriple(a):
    if a % 2 == 1:
        return a, ((a**2)-1)//2, 1+((a**2)-1)//2
    else:
        return a, ((a//2)**2)-1, ((a//2)**2)+1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input().strip())

    triple = pythagoreanTriple(a)

    fptr.write(' '.join(map(str, triple)))
    fptr.write('\n')

    fptr.close()
