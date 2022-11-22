"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return
the answer in any order.
"""
from collections import Counter


def k_most_frequent_elements(nums: list, k: int) -> list:
    counter = Counter(nums)
    most_frequent_with_count = counter.most_common(k)
    return [elem for elem, freq in most_frequent_with_count]


if __name__ == "__main__":
    assert k_most_frequent_elements([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert k_most_frequent_elements([1], 1) == [1]
