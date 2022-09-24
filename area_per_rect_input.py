#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: September 21, 2022
# This program calculates and displays the area and perimeter of a rectangle
# based on the input.


def main():
    # Takes in user input for length and width of rectangle
    length = float(input("Enter the length of the rectangle (cm): "))
    width = float(input("Enter the width of the rectangle (cm): "))
    # Calculates Area and Perimeter of rectangle
    area = length * width
    perimeter = 2 * (length + width)
    # Outputs Area and Perimeter back to user
    print(f"The area: {area}cm^2")
    print(f"The perimeter: {perimeter}cm")


if __name__ == "__main__":
    main()
