#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program adds two numbers

import constants


def main():
    # this is a number guessing game

    # input
    print("Number Guessing Game")
    user_number = int(input("Enter a number between 0-9: "))

    # process
    if user_number == constants.SPECIAL_NUMBER:
        print("YAY! You guessed the correct number!")

    if user_number != constants.SPECIAL_NUMBER:
        print("Try again.")

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
