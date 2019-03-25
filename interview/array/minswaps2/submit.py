#!/bin/python3

import math
import os
import random
import re
import sys

def normalize_array(array, val):
    """
    Normalize array after a value is removed. For each element
    greater than 'val', subtract one from its value.
    Args: 
        array (list of int): Array post-removal of one element.
        val (int): Value removed from array.
    Returns:
        list of int: Normalized array of consecutive (not necessarily
            sorted) integers.
    """
    for i, _ in enumerate(array):
        if array[i] > val:
            array[i] -= 1
    return array


class Array(object):
    """
    Class to keep track of 'state' of task (i.e. the array).
    """
    def __init__(self, arr, arr_sorted=None):
        """
        Initialize unordered array. 
        Args:
            arr (list of int): Our array
            arr_sorted(list of int): Ordered version of array. If None,
                sort 'arr' to get ordered array.
        """
        if arr_sorted is None:
            arr_sorted = sorted(arr)
        removed = list()
        for i, val in enumerate(arr):
            if val == arr_sorted[i]:
                removed.append(val)
        if len(removed) > 0:
            removed = sorted(removed, reverse=True)
            for val in removed:
                arr.remove(val)
                arr_sorted.remove(val)
                arr = normalize_array(arr, val)
                arr_sorted = normalize_array(arr_sorted, val)
        self.arr = arr
        self.arr_sorted = arr_sorted

    def swap(self, i, j):
        """
        Swap elements i and j in array.
        Args:
            i (int): Index of first element to swap.
            j (int): Index of second element to swap.
        
        Returns:
            Array: Array with elements i and j swapped.
        """
        arr_swp = self.arr.copy()
        tmp = arr_swp[j]
        arr_swp[j] = arr_swp[i]
        arr_swp[i] = tmp
        return Array(arr_swp, arr_sorted=self.arr_sorted)


def generate_possible_swaps(arr):
    """
    Generate possible swaps for array.
    Args:
        arr (Array): Our array.
    Returns:
        score (dict): Keys (int) represent indices of the array,
            Values (int) represent the gain in sorted values 
            after swapping the value at the index.
    """
    l = len(arr.arr)
    score = dict()
    for i in range(0, l):
        if arr.arr[i] == i+1:
            score[i] = 2
        else:
            score[i] = 1
    return score


def minimum_swaps(arr):
    """
    Get minimum number of swaps to sort array 'arr' in ascending
    order.
    Args:
        arr (list of int): Array to sort.
    Returns:
        int: Minimum number of swaps to sort.
    """
    array = Array(arr)
    swaps = 0
    while len(array.arr) > 1:
        score = generate_possible_swaps(array)
        i = max(score, key=score.get) 
        j = array.arr[i]-1
        array = array.swap(i, j)
        swaps += 1
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimum_swaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()