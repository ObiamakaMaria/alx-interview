#!/usr/bin/python3
''' Implementation of Minimun  number of Operations
'''


def minOperations(n: int) -> int:
    '''Calculating the minimum number of operations'''
    recent = 1
    holder = 0
    counter = 0
    while (recent < n):
        if holder == 0:
            holder = recent
            counter += 1
        if recent == 1:
            recent += holder
            counter += 1
            continue
        rem = n - recent
        if rem < holder:
            return 0
        if rem % recent == 0:
            holder = recent
            recent += holder
            counter += 2
        else:
            recent += holder
            counter += 1
    if recent != n:
        return 0
    return counter
