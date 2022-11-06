"""
Given a string s, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
Constraints:
len(s) > 3
At least three distinct chars in s

For example, according to the conditions described above,
Input = aaabbbbccde
Output:
b 4
a 3
c 2
"""

from collections import Counter


def most_common_chars_with_counter(input: str):
    sorted_input = sorted(input)
    counter = Counter(sorted_input)
    for k, v in counter.most_common(3):
        print(k, v)


def most_common_chars(input: str):
    counter = {}
    for char in input:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    sorted_counter = sorted(counter.items(), key=lambda x: (x[1] * -1, x[0]))
    for i in range(0, 3):
        print(sorted_counter[i][0], sorted_counter[i][1])


if __name__ == "__main__":
    most_common_chars("aaabbbbccde")
    most_common_chars("cccbbbbaaade")

    most_common_chars_with_counter("aaabbbbccde")
    most_common_chars_with_counter("cccbbbbaaade")
