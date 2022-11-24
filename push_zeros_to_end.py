"""
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
"""


def push_zeros_to_end(nums: list) -> list:
    num_of_zeros = nums.count(0)
    for i in range(num_of_zeros):
        nums.remove(0)
        nums.append(0)
    return nums


if __name__ == "__main__":
    assert push_zeros_to_end([0, 2, 7, 0, 1]) == [2, 7, 1, 0, 0]
    assert push_zeros_to_end([1, 2, 0]) == [1, 2, 0]
