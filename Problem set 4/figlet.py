"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
>> Zero if the user would like to output text in a random font.
>> Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.

Prompts the user for a str of text and Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
    from pyfiglet import Figlet
    figlet = Figlet()

    You can then get a list of available fonts with code like this:
    figlet.getFonts()

    You can set the font with code like this, wherein f is the font’s name as a str:
    figlet.setFont(font=f)

    And you can output text in that font with code like this, wherein s is that text as a str:
    print(figlet.renderText(s))
"""

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()



def main():
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))
    elif (
        len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts
    ):
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

    #prompt user for input:
    text = input("Input: ")
    print(figlet.renderText(text))




main()
