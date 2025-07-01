# Arithmetic Operations
# Objectve: Build a small program that allows the user to choose from a menu and perform different geometry calculations.

import math
while True:
    print("Welcome to the Geometry Calculator")
    print("What would you like to calculate?")
    print("1. Area of a circle")
    print("2. Circumference of a circle")
    print("3. Hypotanus of a triangle")
    print("4. Exit")

    user = int(input("Enter a number to choose what you want to calculate? "))

    if user < 1 or user > 4:
        print("Invalid choice, choose again")
        continue
    break


if user == 1:
    radius = float(input("What is the radius of the circle? "))
    area = math.pi * pow(radius, 2)
    print(f"The area of the circle is {math.ceil(area)} cm^2")

elif user == 2:
    radius = float(input("What is the radius of the circle? "))
    circumference = 2 * math.pi * radius
    print(f"The circumference of the circle is {math.floor(circumference)} cm")

elif user == 3:
    first_side = float(input("Enter a number for the first side of the triangle: "))
    second_side = float(input("Enter a number for the second side of the triangle: "))
    hypotenuse = math.sqrt(pow(first_side, 2) + pow(second_side, 2))
    print(f"The hypotanus of the triangle is {hypotenuse}")


else:
    print("Thank you for using the geometry calculator")
