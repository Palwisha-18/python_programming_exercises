"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
numbers. Given a string s, return true if it is a palindrome, or false otherwise.
"""


def is_palindrome(input: str) -> bool:
    input = input.lower()
    input = ''.join(filter(str.isalnum, input))
    return input == input[::-1]


if __name__ == "__main__":
    assert is_palindrome("Madam") is True
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
