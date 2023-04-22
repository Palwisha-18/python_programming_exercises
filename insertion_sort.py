"""
Sort a given array using insertion sort algorithim
"""


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        for j in range(i, -1, -1):
            if j > 0 and arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr


if __name__ == "__main__":
    assert insertion_sort([5, 3, 2, 6, 1, 4]) == [1, 2, 3, 4, 5, 6]
