# Problem URL:
# https://www.hackerrank.com/challenges/reverse-game/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(n,k):
    L = list(range(n))
    for i in range(n):
        L = L[:i] + L[i:][::-1]
    return L.index(k)

def func(S,k):
    for x in S:
        if k in x:
            if x[0] != x[1]:
                if k == x[0]:
                    return 2*S.index(x)
                else:
                    return 1+2*S.index(x)
            else:
                return 2*S.index(x)
            
if __name__ == '__main__':

    t = int(input().strip())
    for j in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
    
        k = int(first_multiple_input[1])
        
        S = [[n-1-i,i] for i in range(0,(n-1)//2+1)]
        
        print(func(S, k))

