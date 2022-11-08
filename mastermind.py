"""
Write a program that generates a four-digit random code and the user needs to guess the code in
10 tries or less. If any digit out of the guessed four-digit code is wrong, the computer should
print out "B". If the digit is correct but at the wrong place, the computer should print "Y".
If both the digit and position is correct, the computer should print "R".
"""
import random


def generate_code():
    code = []
    for i in range(4):
        code.append(random.randint(0, 9))
    return code


def guess_code():
    code = generate_code()
    tries = 0
    while tries < 10:
        guessed_code = input("Guess 4-digit code: ")
        guessed_code = [int(d) for d in guessed_code]
        tries += 1

        if len(guessed_code) != 4:
            print("You need to enter 4-digit code.")
            continue

        if code == guessed_code:
            print("RRRR")
            print("You guessed the code!")
            break

        result = ""
        for index, digit in enumerate(guessed_code):
            if digit in code:
                if code[index] == digit:
                    result += "R"
                else:
                    result += "Y"
            else:
                result += "B"

        print(result)
    else:
        print("No more tries left!")


if __name__ == "__main__":
    guess_code()
