#!/bin/python3

import sys

def powerSum(X, N):
    # Complete this function
    res = 0
    def findCombos(X, N, num):
        if num ** N < X:
            return findCombos(X, N, num+1) + findCombos(X - num ** N, N, num+1)
        elif num ** N == X:
            return 1
        else:
            return 0
    return findCombos(X, N, 1)

####################################################################################
if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N)
    print(result)
