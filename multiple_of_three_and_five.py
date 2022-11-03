"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Finish the solution so that it returns the sum of all the
multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.
"""


def multiple_of_three_and_five(number: int) -> int:
    sum_of_multiples = 0
    for i in range(0, number):
        if (i % 3 == 0) or (i % 5 == 0):
            sum_of_multiples += i
    return sum_of_multiples


if __name__ == "__main__":
    assert multiple_of_three_and_five(10) == 23
    assert multiple_of_three_and_five(-5) == 0
    assert multiple_of_three_and_five(5) == 3
