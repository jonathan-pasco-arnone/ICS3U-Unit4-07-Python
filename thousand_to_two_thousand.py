#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program displays every number from 1000 to 2000


def main():
    # This function displays every number from 1000 to 2000

    counter = 1000
    numbers_in_line = 0
    print("")
    print("This program shows every integer from 1000 to 2000")
    print("")
    while counter <= 2000:
        if numbers_in_line == 5:
            numbers_in_line = 1
            print("")  # end line
        else:
            numbers_in_line = numbers_in_line + 1
        counter_str = str(counter)
        print(counter_str, end=", ")
        counter = counter + 1


if __name__ == "__main__":
    main()
