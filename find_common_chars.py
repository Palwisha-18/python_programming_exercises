"""
Given a string array words, return an array of all characters that show up in all strings within the words
(including duplicates). You may return the answer in any order.

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
"""
from collections import Counter
from functools import reduce


def find_common_chars_using_counter(arr):
    result = Counter(arr[0])
    for word in arr:
        result &= Counter(word)
    return list(result.elements())


def find_common_chars(arr):
    words_char_freq = []

    for word in arr:
        char_freq = {}
        for char in word:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
        words_char_freq.append(char_freq)

    common_chars_with_min_occurence_count = reduce(lambda d1, d2: {k: min(d1.get(k, 0), d2.get(k, 0))
                                                             for k in set(d1) & set(d2)}, words_char_freq)
    sorted(common_chars_with_min_occurence_count)

    results = []
    for k, v in common_chars_with_min_occurence_count.items():
        for _ in range(v):
            results.append(k)

    return results


if __name__ == "__main__":
    assert find_common_chars_using_counter(["bella", "label", "roller"]) == ["e", "l", "l"]
    assert find_common_chars_using_counter(["cool", "lock", "cook"]) == ["c", "o"]
    assert find_common_chars(["cool", "lock", "cook"]) == ["c", "o"]
    assert find_common_chars(["bella", "label", "roller"]) == ["e", "l", "l"]
