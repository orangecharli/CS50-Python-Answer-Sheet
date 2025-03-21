"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).

Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively."
"""

def main():
    x = get_grocery_list()
    output_grocery_list(x)

def get_grocery_list():
    grocery_list = {}
    while True:
        try:
                #prompt user for item
                item = input("").upper()
                #store the items in a dictionary, and count items
                if item in grocery_list:
                    grocery_list[item] += 1
                else:
                    grocery_list[item] = 1
        except EOFError:
            print("", end="\n")
            return grocery_list

def output_grocery_list(list):
    #sort alphabetically
    for item in sorted(list):
        #print the list, with a quantity prefix
        print(f"{list[item]} {item}")

main()
