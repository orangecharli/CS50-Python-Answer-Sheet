"""
Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

1. Expects the user to specify as a command-line argument the number of Bitcoins, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
2. Queries the API for the CoinCap Bitcoin Price Index at https://api.coincap.io/v2/assets/bitcoin, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like: except requests.RequestException:
3. Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.

"""

import sys
import requests


def main():
    total_coins = get_total_coins()
    price = get_bitcoin_price()
    get_cost(total_coins, price)


def get_total_coins():
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")


def get_bitcoin_price():
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    bitcoin_info = response.json()
    price = bitcoin_info["data"]["priceUsd"]
    return float(price)


def get_cost(quantity, price):
    cost = quantity * price
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
