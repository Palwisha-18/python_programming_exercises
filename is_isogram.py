"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
"""


def is_isogram(word: str) -> bool:
    word = word.lower()
    for character in word:
        if word.count(character) > 1:
            return False
    return True


if __name__ == "__main__":
    assert is_isogram("programming") is False
    assert is_isogram("python") is True
