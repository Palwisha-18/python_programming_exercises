"""
Reverse an array
"""


def reverse_array_using_reverse(arr: list) -> list:
    arr.reverse()
    return arr


def reverse_array_using_reversed(arr: list) -> list:
    return list(reversed(arr))


def reverse_array_by_swapping(arr: list) -> list:
    size = len(arr)
    for i in range(0,  size // 2):
        arr[i], arr[size - i - 1] = arr[size - i - 1],  arr[i]
    return arr


def reverse_array_using_slicing(arr: list) -> list:
    return arr[::-1]


def reverse_array_using_recursion(arr):
    if len(arr) == 1:
        return arr
    return reverse_array_using_recursion(arr[1:]) + arr[0:1]


if __name__ == "__main__":
    assert reverse_array_using_reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    assert reverse_array_using_reversed([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    assert reverse_array_by_swapping([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_array_by_swapping([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]

    assert reverse_array_using_slicing([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    assert reverse_array_using_recursion([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_array_using_recursion([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]
