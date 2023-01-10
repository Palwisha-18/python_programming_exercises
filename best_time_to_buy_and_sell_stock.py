"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def max_profit_brute_force(arr: list) -> int:
    max_profit = 0
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > max_profit:
                max_profit = arr[j] - arr[i]
    return max_profit


if __name__ == "__main__":
    assert max_profit_brute_force([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit_brute_force([7, 6, 4, 3, 1]) == 0
