"""
A man was given directions to go from point A to point B.
The directions were: "SOUTH", "NORTH", "WEST", "EAST".
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
Going to one direction and coming back in the opposite direction is a waste of time and energy.
So, we need to help the man by writing a program that will eliminate the useless steps and
will contain only the necessary directions.

For example: The directions ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
should be reduced to ["WEST"]. This is because going "NORTH" and then immediately "SOUTH" means
coming back to the same place. So we cancel them and we have ["SOUTH", "EAST", "WEST",
"NORTH", "WEST"]. Next, we go "SOUTH", take "EAST" and then immediately take "WEST",
which again means coming back to the same point. Hence we cancel "EAST" and "WEST" to giving us
["SOUTH", "NORTH", "WEST"]. It's clear that "SOUTH" and "NORTH" are opposites hence canceled
and finally we are left with ["WEST"].
"""

OPPOSITE_DIRECTIONS = {
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH',
    'EAST': 'WEST',
    'WEST': 'EAST'
}


def simplify_directions(directions: list) -> list:
    final_directions = []

    for i in range(len(directions)):
        if not final_directions:
            final_directions.append(directions[i])
        else:
            if OPPOSITE_DIRECTIONS[final_directions[-1]] == directions[i]:
                final_directions.pop()
            else:
                final_directions.append(directions[i])
    return final_directions


if __name__ == "__main__":
    assert simplify_directions(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == ["WEST"]
    assert simplify_directions(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]) == []
    assert simplify_directions(["EAST", "SOUTH", "NORTH", "WEST", "WEST", "EAST", "EAST"]) == ["EAST"]
