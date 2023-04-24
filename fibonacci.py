"""
Implement Fibonacci sequence
"""


def fibonaci(num: int):
    if num <= 1:
        return num

    return fibonaci(num - 1) + fibonaci(num - 2)


if __name__ == "__main__":
    assert fibonaci(0) == 0
    assert fibonaci(1) == 1
    assert fibonaci(5) == 5
    assert fibonaci(8) == 21
