"""
Given a string, write a Python program to check if that string is Pangram or not.
A pangram is a sentence containing every letter in the English Alphabet.
"""


def is_pangram(input: str) -> bool:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in input.lower():
            return False

    return True


if __name__ == "__main__":
    assert is_pangram("The quick brown fox jumps over the lazy dog") is True
    assert is_pangram("abcdefgxyz") is False
