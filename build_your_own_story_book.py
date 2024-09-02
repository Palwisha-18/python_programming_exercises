"""
You are reading a Build Your Own Story book. It is like a normal book except that choices on some pages
affect the story, sending you to one of two options for your next page.
These choices are really stressing you out, so you decide that you'll either always pick the first option,
or always pick the second option.
You start reading at page 1 and read forward one page at a time unless you reach a choice or an ending.
The choices are provided in a list, sorted by the page containing the choice, and each choice has two
options of pages to go to next. In this example, you are on page 3, where there is a choice.
Option 1 goes to page 14 and Option 2 goes to page 2.

choices1 = [[3, 14, 2]] => [current_page, option_1, option_2]

The ending pages are also given in a sorted list:
endings = [6, 15, 21, 30]

Given a list of endings, a list of choices with their options, and the choice you will always take
(Option 1 or Option 2), return the ending you will reach. If you get stuck in a loop, return -1.
Example:
find_ending(endings, choices1, 1) (always Option 1)
  Start: 1 -> 2 -> 3(choice) -> 14 -> 15(end) => Return 15
find_ending(endings, choices1, 2) (always Option 2)
  Start: 1 -> 2 -> 3(choice) -> 2 -> 3(choice) -> 2... => Return -1

Additional inputs:
choices2 = [[5, 11, 28], [9, 19, 29], [14, 16, 20], [18, 7, 22], [25, 6, 30]]
choices3 = []
choices4 = [[2, 10, 15], [3, 4, 10], [4, 3, 15], [10, 3, 15]]

Complexity Variable:
n = number of pages
(endings and choices are bound by the number of pages)

All Test Cases:
find_ending(endings, choices1, 1) => 15
find_ending(endings, choices1, 2) => -1
find_ending(endings, choices2, 1) => 21
find_ending(endings, choices2, 2) => 30
find_ending(endings, choices3, 1) => 6
find_ending(endings, choices3, 2) => 6
find_ending(endings, choices4, 1) => -1
find_ending(endings, choices4, 2) => 15
"""
from typing import List, Tuple, Dict, Set


def preprocess_choices(choices: List[List[int]]) -> Dict[int, Tuple[int, int]]:
    """
    Preprocess the choices into a dictionary for O(1) lookups.

    Args:
        choices (List[List[int]]): The list of choices, where each choice is represented as
        [current_page, option_1, option_2].

    Returns:
        Dict[int, Tuple[int, int]]: A dictionary mapping the current_page to a tuple of (option_1, option_2).
    """
    return {choice[0]: (choice[1], choice[2]) for choice in choices}


def find_ending(endings: Set[int], choices: Dict[int, Tuple[int, int]], option: int) -> int:
    """
    Finds the ending page based on the choices made.

    Args:
        endings (Set[int]): A set of ending pages.
        choices (Dict[int, Tuple[int, int]]): A dictionary of choices with pages as keys
        and their options as values.
        option (int): The choice option to always take (1 or 2).

    Returns:
        int: The ending page reached, or -1 if stuck in a loop.
    """
    cur_page = 1
    visited = set()

    while cur_page not in endings:
        if cur_page in visited:
            return -1
        visited.add(cur_page)
        if cur_page in choices:
            cur_page = choices[cur_page][option - 1]
        else:
            cur_page += 1

    return cur_page


def run_tests() -> None:
    """
    Runs the test cases to validate the solution.
    """
    TEST_CASES = [
        (set([6, 15, 21, 30]), [[3, 14, 2]], 1, 15),
        (set([6, 15, 21, 30]), [[3, 14, 2]], 2, -1),
        (set([6, 15, 21, 30]),
         [[5, 11, 28], [9, 19, 29], [14, 16, 20], [18, 7, 22], [25, 6, 30]], 1, 21),
        (set([6, 15, 21, 30]),
         [[5, 11, 28], [9, 19, 29], [14, 16, 20], [18, 7, 22], [25, 6, 30]], 2, 30),
        (set([6, 15, 21, 30]), [], 1, 6),
        (set([6, 15, 21, 30]), [], 1, 6),
        (set([6, 15, 21, 30]),
         [[2, 10, 15], [3, 4, 10], [4, 3, 15], [10, 3, 15]], 1, -1),
        (set([6, 15, 21, 30]),
         [[2, 10, 15], [3, 4, 10], [4, 3, 15], [10, 3, 15]], 2, 15)
    ]

    for endings, choices, option, expected in TEST_CASES:
        assert find_ending(endings, preprocess_choices(choices),
                           option) == expected, f"Failed on {choices} with option {option}"


if __name__ == "__main__":
    run_tests()
