"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            #prompt user for input
            user_date = input("Date: ").strip()
            #check if input is formatted in "M/D/YYYY" and split into M, D, Y variables
            if re.search("^[1-9][0-9]*/[1-9][0-9]*/[0-9]{4}$"  , user_date):
                month, day, year = user_date.split("/")
            #check if input is formatted in "September D, YYYY" and split into M, D, Y variables
            elif re.search("[A-Z][a-z]*", user_date).group() in months and re.search("^[A-Z][a-z]* [1-9][0-9]*, [0-9]{4}$", user_date):
                month, day, year = user_date.split(" ")
                day = day[:-1]
                month = months.index(month) + 1
            else:
                raise ValueError
            #check if user input day > 31 or month > 12
            if int(day) > 31 or int(month) > 12: 
                raise ValueError
          except ValueError:
            pass
        else:
            #output the date in YYYY-MM-DD format
            print(f"{year}-{int(month):02d}-{int(day):02d}")
            break

main()
