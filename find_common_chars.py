"""
Given a string array words, return an array of all characters that show up in all strings within the words
(including duplicates). You may return the answer in any order.

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
"""
from collections import Counter


def find_common_chars_using_counter(arr):
    result = Counter(arr[0])
    for word in arr:
        result &= Counter(word)
    return list(result.elements())


if __name__ == "__main__":
    assert find_common_chars_using_counter(["bella", "label", "roller"]) == ["e", "l", "l"]
    assert find_common_chars_using_counter(["cool", "lock", "cook"]) == ["c","o"]
