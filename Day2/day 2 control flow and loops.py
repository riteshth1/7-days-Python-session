# Day 2: Control Flow & Loops
# •	- Conditionals (if/elif/else)
# •	- Logical Operators
# •	- Randomisation Basics
# •	- Flowchart Programming (Simple Example)
# •	- For Loops
# •	- While Loops
# •	- Code Blocks and Indentation
# •	- Hands-on Exercises

# check a number if it is even or odd
# number = int(input("Enter a number:"))

# nested if-else
# if number.is_integer():
#     if number % 2 == 0:
#         print("It's even")
#     else:
#         print("It's odd")
# else:
#     print("Invalid input type")

# if-else-ladder
# if cond:
#     if cond:
#         if cond:

# if-elif-else
# n = int(input("Enter any number:"))
# for i in range(1, n+1):
#     if i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     elif i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     else:
#         print(i)

# Logical operator
# and, or, not
# if n == 12 or n == 15:
#     print(n)
# else:
#     print("Go away")

# if not True:
#     print("True")
# else:
#     print("False")

# age = int(input("Enter your age:"))
# if age > 0 and age < 100:
#     if age > 18:
#         print("You can vote")
#     else:
#         print("You can't vote")
# else:
#     print("Invalid age")

# Package import techniques

# Syntax:
# import package_name
# from package_name import function of package

import random as r
# from random import randint

# Number guessing game
computer_choice = r.randint(1,50)
user_input = int(input("Guess any number between 1 - 50:"))

if user_input == computer_choice:
    print("You win")
else:
    print("You Lose!!PLease try again")


print("""=============================================Exercise===================================================""")
# Check if score is 90 or above
# if score >= 90:
#     print("Grade: A")  # If true, print A grade
# # If the above condition fails, check if score is 75 or above
# elif score >= 75:
#     print("Grade: B")  # If true, print B grade
# # If none of the above conditions are met
# else:
#     print("Grade: C")  # Default grade C

# Logical operators
# Define age and driving license status
# age = 20
# has_license = True
#
# # Check if the person is 18 or older AND has a driving license
# if age >= 18 and has_license:
#     print("You can drive.")  # If both conditions are true
# else:
#     print("You cannot drive.")  # If any condition is false


# Module importing and using it with loops and if-else:
# Number Guessing game
# import random
#
# random.randint()
#
# import random as r
#
# # from random import randint
#
# winning_number = r.randint(0,5)
#
#
# while True:
#     num = int(input("Enter a number:"))
#     if num == winning_number:
#         print("You Win💖")
#     else:
#         print("You lose😭")

# BMI calculator
# Ask user for weight in kilograms and convert it to float

# weight = float(input("Enter your weight in kg: "))
#
# # Ask user for height in meters and convert it to float
# height = float(input("Enter your height in meters: "))
#
# # Calculate BMI using the standard formula
# bmi = weight / (height ** 2)
#
# # Display BMI rounded to 2 decimal places
# print(f"Your BMI is: {bmi:.2f}")
#
# # Interpret BMI based on standard classification
# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 24.9:
#     print("You have a normal weight.")
# elif 25 <= bmi < 29.9:
#     print("You are overweight.")
# else:
#     print("You are obese.")










