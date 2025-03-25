"""
I’m thinking of a number between 1 and 100…

What is it?
It’s 50! But what if it were more random?

In a file called game.py, implement a program that:

1. Prompts the user for a level n. If the user does not input a positive integer, the program should prompt again.
2. Randomly generates an integer between 1 and n inclusive, using the random module.
3. Prompts the user to guess that integer.
>> If the guess is not a positive integer, the program should prompt the user again.
>> If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
>> If the guess is larger than that integer, the program should output Too large! and prompt the user again.
>>If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random
import sys


def main():
    level = get_level()
    integer_to_guess = random.randint(1, level)
    guess_number(integer_to_guess)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            pass


def guess_number(n):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                pass
            if guess < n:
                print("Too small!")
            if guess > n:
                print("Too large!")
            if guess == n:
                sys.exit("Just right!")
        except ValueError:
            pass


main()
