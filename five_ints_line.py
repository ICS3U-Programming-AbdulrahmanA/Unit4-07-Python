#!/usr/bin/env python3
# Created By: Abdul
# Date: 11/20/2025
# Program to show all valid color combos


def main():
    # for loop to iterate through years 1000 to 2000
    for year in range(1000, 2001, 1):
        if year % 5 == 0 and year != 1000:
            # print a newline before the year if it is divisible by 5 but not 1000
            print("\n", year, end=" ")
        else:
            print(year, end=" ")


if __name__ == "__main__":
    main()
