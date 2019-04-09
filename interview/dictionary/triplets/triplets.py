#!/bin/python3

import math
import os
import random
import re
import sys


def build_dict(arr):
    """
    Build dictionary from array.
    """
    d = dict()
    for i, val in enumerate(arr):
        if val not in d:
            d[val] = set()
        d[val].add(i)
    return d

# Use memoization to store "couples" in dict
# e.g. for array 1 1 1 1 5 25 25
# store (4, 1) = 2 to represent index 4 and n=1, two "couples" 
# same couple used for four different triplets

couples = dict()

def find_couples(arr, d, i, r):

    # Check if next value in triplet present in array
    val = arr[i] * r
    if val not in d:
        return 0
    # If result cached, get it
    if i in couples:
        return couples[i]
    # Compute number couples and memoize
    n_couples = len([j for j in d[val] if j > i]) 
    couples[i] = n_couples
    return n_couples


def find_triplets(arr, d, i, r):

    # Check if next value in triplet present in array
    val = arr[i] * r
    if val not in d:
        return 0
    js = d[val]
    # Get remaining two elements of triplet
    total = 0
    for j in js:
        total += d[j] 
        total += find_couples(arr, d, j, r)
    return total

def lookup(d, val):
    if val not in d:
        return 0
    return len(d[val])

def count_triplets(arr, r):
    """
    Count triplets in array with common ratio r.

    Args:
        arr (list of int):
        r (int): common ratio
    """
    # Only keep multiples of common ratio
    d = build_dict(arr)
    total = 0
    for i in range(len(arr)-2):
        #total += find_triplets(arr, d, i, r)
        val = arr[i]
        total += lookup(d, val*r) * lookup(d, val*r*r)
        d[val].remove(i)
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = count_triplets(arr, r)
    fptr.write(str(ans) + '\n')
    fptr.close()

