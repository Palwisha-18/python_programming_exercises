"""
Write a program to check whether a given integer number by user is a prime number or not.
"""


def is_prime_number(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    assert is_prime_number(1) is True
    assert is_prime_number(3) is True
    assert is_prime_number(6) is False
    assert is_prime_number(13) is True
