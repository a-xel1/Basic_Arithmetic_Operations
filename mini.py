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




# Quiz_Game

user = input("What is the fastest land animal?: ")
answer = "Cheetah"

if user.capitalize() == answer:
    print("Correct!")
    score = 5

else:
    print("Incorrect!")
    score = -5
    
user2 = int(input("What is the area of a triangle with 8 and 5 as base and height respectively?: "))

base = 8
height = 5
area = (1/2 * base ) * height

if user2 == area:
    print("Correct!")
    score1 = score + 5

else:
    print("Incorrect!")
    score1 = -5

user3 = input("A coin is tossed twice and a die is rolled once. What is the probability that the outcome is a head and a prime number?: " \
"       A. 5/4" \
"       B. 1/4" \
"       C. 3/8" \
"       D. 3/2" \
"        ")

option1 = "A"
option2 = "B"
option3 = "C"
option4 = "D"

head_as_outcome = 3/4
prime_number_as_outcome = 1/2
probability = head_as_outcome * prime_number_as_outcome

if user3 == prime_number_as_outcome or user3.capitalize() == option3:
    print("Correct!")
    score2 = score1 + 5

else:
    print("Incorrect!")
    score2 == -5

user4 = input("Who was the first computer scientist?: " \
"       A. Ada Lovelace" \
"       B. Alan Turing" \
"       C. Charles Babbage" \
"       D. Grace Hooper" \
"         ")

option_1 = "A"
option_2 = "B"
option_3 = "C"
option_4 = "D"

if user4.upper() == option_1:
    print("Correct!")
    score3 = score2 + 5

else:
    print("Incorrect!")
    score3 = -5

user5 = input("Who is the current president of Russia?: ")
answer5 = "Vladimir putin" 
answer_5 = "Putin"

if user5.capitalize() == answer5 or user5.capitalize() == answer_5:
    print("Correct!")
    score4 = score3 + 5

else:
    print("Incorrect!")
    score4 = -5

user6 = input("What is the estimated population of Ghana?: ")
answer6 = "33.79 million" or "33.79"

if user6 >= "30 million" or "30":
    print("Correct!")
    score5 = score4 + 5

else:
    print("Incorrect!")
    score5 = -5

user7 = input("Who is the richest person in the world right now?: ")
answer7 = "Elon musk"
answer_7 = "Elon"

if user7.capitalize() == answer7 or user7.capitalize() == answer_7:
    print("Correct!")
    score6 = score5 + 5

else:
    print("Incorrect!")
    score6 = -5

user8 = input("What is the scientific name for mosquito?: " \
"       A. Culicidae" \
"       B. Glosina" \
"       C. Mantodea" \
"       D. Musca Domestica" \
"       ")

options1 = "A"
options2 = "B"
options3 = "C"
options4 = "D"

if user8.capitalize() == options1:
    print("Correct!")
    score7 = score6 + 5

else:
    print("Incorrect!")
    score7 = -5

user9 = input("What is the most popular sport in the world?: ")
answer9 = "Football"

if user9.capitalize() == answer9:
    print("Correct!")
    score8 = score7 + 5
else:
    print("Incorrect!")
    score8 = -5

user10 = input("What is the most populated country?: ")
answer10 = "India"

if user10.capitalize() == answer10:
    print("Correct!")
    score9 = score8 + 5
else:
    print("Incorrect!")
    score9 = -5

user11 = input("Who is the most popular person in the world right now?: " \
"        A. Cristiano Ronaldo" \
"        B. Donald Trump" \
"        C. Lionel Messi" \
"        D. Jesus Christ" \
"           ")

options_1 = "A"
options_2 = "B"
options_3 = "C"
options_4 = "D"

if user11.capitalize() == options_4:
    print("Correct!")
    score10 = score9 + 5
else:
    print("Incorrect!")
    score10 = -5

if score10 == 55:
    print(f"Outstanding! You got {score10} out of 55")
elif score10 <= 55:
    print(f"You got {score10} out of 55")


# if score1 == 10:
#     print(f"Outstanding! You got {score1} out of 10")
# elif score1 <= 55:
#     print(f"You got {score1} out of 10")


# Calculator
operations = ["+", "-", "*", "/"]
while True:
    user = input(f"Enter the operation {operations}: ")
    if user not in  operations:
        print("Invalid choice!")
        continue
    break

numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
 
if user == "+":
    print(numb1 + numb2)
elif user == "-":
    print(numb1 - numb2)
elif user == "*":
    print(numb1 * numb2)
elif user == "/":
    if numb2 == 0:
        print("Error, cannot divide by zero")
    else:
        print(numb1 / numb2)
