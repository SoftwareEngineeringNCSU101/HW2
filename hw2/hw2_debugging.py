"""
This module contains functions for merge sort and random array generation.
"""
import rand

def merge_sort(input_arr):
    """Recursively sorts an array using merge sort."""
    if len(input_arr) <= 1:
        return input_arr
    half = len(input_arr) // 2
    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))

def recombine(left_arr, right_arr):
    """Merges two sorted arrays into one."""
    left_index = 0
    right_index = 0
    merge_arr = []

    # Merge the arrays until one is exhausted
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # Append the remaining elements from left_arr, if any
    while left_index < len(left_arr):
        merge_arr.append(left_arr[left_index])
        left_index += 1

    # Append the remaining elements from right_arr, if any
    while right_index < len(right_arr):
        merge_arr.append(right_arr[right_index])
        right_index += 1

    return merge_arr

# Test run with random array
arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
