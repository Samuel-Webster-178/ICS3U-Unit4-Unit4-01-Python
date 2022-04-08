#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program includes a while loop


def main():
    # I calculate circumference

    # input
    string_highest_number = input("Enter your highest positive integer: ")
    total = 0
    i = 0

    # process & output
    try:
        int_highest_number = int(string_highest_number)
        while i < int_highest_number:
            total += i + 1
            i += 1
        print("Sum of positive integers up to {1} is {2}.".format(int_highest_number, total))
    except Exception:
        print("Invalid Input")
    print("\nDone.")


if __name__ == "__main__":
    main()
