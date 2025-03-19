"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

"""
#prompt user to insert coin>> ignore if not 5c, 10c, 25c
#subtract the value of coin from the value, print amount due
#once 50c is reached, output value of change

def main():
    due = 50
    while True:
        print(f"Amount Due: {due}")
        if due > 0:
            coin = int(input("Insert Coin: "))
            if coin in (5, 10, 25):
                due -= coin
        if due <= 0:
            print(f"Change Owed: {abs(due)}")
            break
main()
