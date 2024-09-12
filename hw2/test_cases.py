"""
This file contains test cases for the hw2_debudding.py file
"""

from hw2_debugging import merge_sort


def test_merge_sort_unsorted():
    """
    Test merge_sort with an unsorted list.
    """
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = merge_sort(unsorted_list)
    expected_list = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert sorted_list == expected_list


def test_merge_sort_sorted():
    """
    Test merge_sort with an already sorted list.
    """
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = merge_sort(sorted_list)
    assert result == sorted_list


def test_merge_sort_empty():
    """
    Test merge_sort with an empty list.
    """
    empty_list = []
    result = merge_sort(empty_list)
    assert result == empty_list
