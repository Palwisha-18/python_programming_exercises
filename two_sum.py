"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""


def two_sum_brute_force(arr: list, target: int) -> list:
    size_of_arr = len(arr)
    for i in range(0, size_of_arr):
        for j in range(i + 1, size_of_arr):
            if (arr[i] + arr[j]) == target:
                return [i, j]
    return []


def two_sum_linear(arr: list, target: int) -> list:
    size_of_arr = len(arr)
    numbers_visited = {}
    for i in range(0, size_of_arr):
        if target - arr[i] in numbers_visited:
            return [numbers_visited[target - arr[i]], i]
        numbers_visited[arr[i]] = i
    return []


if __name__ == "__main__":
    assert two_sum_brute_force([1, 2, 3, 4, 5], 8) == [2, 4]
    assert two_sum_linear([1, 4, 2, 6, 3], 8) == [2, 3]
