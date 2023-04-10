"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a
given target value. If target is not found in the array, return [-1, -1].
"""


def find_first_and_last_index_of_elem(arr: list, target: int) -> list:
    first_index = -1
    last_index = -1
    count = 0
    for index, elem in enumerate(arr):
        if elem == target:
            if count == 0:
                first_index = index
                last_index = index
            else:
                last_index = index
            count += 1
    return [first_index, last_index]


if __name__ == "__main__":
    assert find_first_and_last_index_of_elem([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert find_first_and_last_index_of_elem([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert find_first_and_last_index_of_elem([], 0) == [-1, -1]
