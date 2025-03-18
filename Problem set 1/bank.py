"""
In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
"""

import re

def main():
    x = hello()
    calculate(x)


#prompt user for greeting
def hello():
    user_greeting = input("Greeting: ")
    #transform to case insensitive and remove whitespace
    user_greeting = user_greeting.lower().strip()
    return user_greeting

#conditional statement
def calculate(greeting):
    if re.findall("^hello.*", greeting):
        print("$0")
    elif re.findall("^h.*", greeting):
        print("$20")
    else:
        print("$100")

main()
