"""
Sort a given array using bubble sort algorithim
"""


def bubble_sort(arr: list):
    size_of_arr = len(arr)
    swapped = False
    for i in range(size_of_arr - 1):
        for j in range(0, size_of_arr - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


if __name__ == "__main__":
    arr = [5, 3, 2, 6, 1, 4]
    bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6]
