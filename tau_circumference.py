#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program includes a while loop


def main():
    # I calculate circumference

    # input
    string_highest_number = input("Enter your highest positive integer: ")
    total = 0
    counter1 = 0

    # process & output
    try:
        int_highest_number = int(string_highest_number)
        while counter1 < int_highest_number:
            counter1 += 1
            total += counter1
        print(
            "Sum of positive integers up to {0} is {1}.".format(
                int_highest_number, total
            )
        )
    except Exception:
        print("Invalid Input")
    print("\nDone.")


if __name__ == "__main__":
    main()
