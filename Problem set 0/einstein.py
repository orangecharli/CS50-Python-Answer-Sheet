"""
Even if you haven’t studied physics (recently or ever!), you might have heard that E = mc2 , wherein E represents energy (measured in Joules),m represents mass (measured in kilograms), and c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""


# prompt user and convert to int
# do the math
# output in joules

def main():
    prompt = int(input('how many kilograms? '))
    x = convert_to_joules(prompt)
    print(x)

def convert_to_joules(mass):
    joules = mass * (300000000 ** 2)
    return joules

main()
