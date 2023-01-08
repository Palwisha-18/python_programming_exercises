"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""


def two_sum(arr: list, target: int) -> list:
    size_of_arr = len(arr)
    for i in range(0, size_of_arr):
        for j in range(i + 1, size_of_arr):
            if (arr[i] + arr[j]) == target:
                return [i, j]
    return []


if __name__ == "__main__":
    assert two_sum([1, 2, 3, 4, 5], 8) == [2, 4]
