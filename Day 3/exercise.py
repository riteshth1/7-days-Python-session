#Topics to be covered
import random

from attr.converters import optional

#  python list, dictionary syntax adding, deleting and updating item in the list
#  Who will pay the bill? --> Game
# indexing and Nested lists
# Index error
# Assignment --> Rock, scissor, paper game
# Password generator

# Day 3: Functions & Collections
# •	- Functions (Defining and Calling)
# •	- Positional and Keyword Arguments
# •	- Returning Functions (return vs print)
# •	- Python Dictionaries and Lists
# •	- Nested Collections
# •	- Hands-on Mini Project

# Function -->  a reusable block of code that performs a specific task

# features of function
# Reusability:
# Once defined, a function can be used multiple times throughout a program without rewriting the same code.
# Modularity:
# Functions break down complex programs into smaller, manageable parts, making them easier to understand, develop, and maintain.
# Abstraction:
# Functions hide the internal details of their implementation, allowing programmers to focus on what the function does rather than how it does it.
# Input and Output:
# Functions can take input data (parameters) and return output data (results)

# defining function --> def keyword
# def function_name():
#     print("Ritesh")
#     print("This is function demo")
#
# # Calling a function
# function_name()
# function_name()
# function_name()
# function_name()

# Positional Argument
# check if the number is odd or even
# def check(num, b):
#     """This functions accepts a number and check if it is even or odd."""
#     if num % 2 ==0:
#         print("It's even")
#     else:
#         print("It's odd")
#     print(b)
#
# number = int(input("Enter any number:"))
# check(54, number)

# Keyword argument
# def check(num, b):
#     """This functions accepts a number and check if it is even or odd."""
#     if num % 2 ==0:
#         print("It's even")
#     else:
#         print("It's odd")
#     print(b)
#
# number = int(input("Enter any number:"))
# check(b= 54, num= number)

# Returning Functions (return vs print)
# def add(a, b):
#     """Adds two number and return the value """
#     return a+b
#
# print(add(1, 5))

# lists -->  collection of items or elements
a = [1,2,54,8,87,"ritesh", "pabitra", "bikesh", "isha","risan", True, False, 4.5887]

# To find the length of list
# print(len(a))
#
# # to know the length of string
# print(len('books'))
#
# # Accessing the elements of list
# # list_name[index] --> to get the element of list
# print(a[6])
#
# # Negative index to access element
# print(a[-5])
#
# # Slicing
# # list_name[starting_index : ending_index : steps(optional)]
# print(a[0:4:1])
# print(a[0:4:2])
# print(a[0:4:3])

# looping in list
# for loop in list_name: --> gives every element of list
# for var_name in a:
#     print(var_name)

# for index in range(len(a)):
#     print(a[index])

# This line of code produce index error
# print(a[14]) #IndexError: list index out of range

# To add values or elements in list (list_name.append(what to add))
# a.append("syavcdycvavicd")
# a.append("aubdvvavb")
# a.append("ajdbvha")
# a.append(4588)
#
# print(f"list after adding data: {a}")
#
# # To remove elements from list
# a.remove("ritesh")
# print(f"list after removing data: {a}")
#
# # To update a value of the list
# a[5] = "aaditya"
# print(f"Updating a list: {a}")
#
# # Reverse a list
# print(f"Reverse a list: {a[::-1]}")

# Dictionary --> collection of key-value pair
b = {
    "key": "value",
    "name": "ritesh",
    "college": "HSMSS"
}

# Accessing a dictionary
print(b['name'])
print(b['college'])

print(b)
# Update a value
b['name'] = "Pabitra Gunda Gang "
print(b)

# looping in dictionary
# for key in b:
#     print(b[key])

# for value in b.keys():
#     print(b[value])

# Adding a new key and value
# b['students'] = {0:'pabitra', 1:'krishna',2:'isha'}
# print(b['students'])

# Nested Collections
c = [
    [1,5,4,8],
    [2,4,6,7]
]

c[0][3] = 10
print(c)

for i in c:
    for j in i:
        print(j)

d = {
    "a":{
        1:"k",
        2:'ho',
        3:'timro',
        4:'nam',
        5:'baini'
    },
    "b":{
        "hindi":["kya", "hua", "Tera", "Wada"],
        "hero":{
            'name' : "hrithik"
            
        }
    }
}