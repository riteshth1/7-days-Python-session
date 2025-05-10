# Today's topic

# Day 5: OOP - Part 1
# •	- Introduction to OOP
# •	- Creating Classes and Objects
# •	- Class Initializers (__init__ method)
# •	- Getting and Setting Attributes
# •	- Python Methods
# •	- Hands-on: Simple Class Creation


# OOP --> way of writing code by grouping data and actions together into units\

# Creating class and object

# class --> the blueprint that are used to create objects.
# object --> instance of class
# class BcaSecond:
#     pass
#
# # Creating object
# bca_second = BcaSecond()
# print(bca_second)


# Constructor --> special method which is called automatically when an object is created.
# Features: a. Same name as Class, b. Helps to initialize object
# __init__()

class BcaSecond:

    # default initializer
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(f"Name:{self.name}, Grade: {self.grade}")



# Creating object
student = BcaSecond("Rachana", "A+")
student.show()

s1 = BcaSecond("Ram", "A+")
s1.show()



# Create an animal class, initialize two attributes name, sound, age.
# Add a method to display the details of animal.




