"""
Write a function called repeat_str which repeats the given string exactly n times.
"""


def repeat_str(input_str: str, n: int) -> str:
    return input_str * n


if __name__ == "__main__":
    assert repeat_str("none", 2) == "nonenone"
