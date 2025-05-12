# Day 6: OOP - Part 2 + Modules
# •	- Inheritance in Python
# •	- Parent and Child Classes Example
# •	- Using External Python Modules / Import
# •	- Module Aliasing
# •	- Hands-on: Classes using Inheritance

# Inheritance is a mechanism where a new class can acquire the properties and behaviour of another class.
# Super class or base class or parent class --> the class which has properties and behaviour.
# Derived or child class --> the class which inherits the another existing class.

# Base class
# class Calculate:
#     def add(self, a, b):
#         return (a + b)
#
#     def subtract(self, a, b):
#         return (a - b)
#
# # Derived class
# class ChildClass(Calculate):
#     def product(self, a, b):
#         return (a * b)
#
#     def divide(self, a, b):
#         return (a / b)
#
# # Object of derived class
# child_class = ChildClass()
#
# # using method of both base and child class
# add = child_class.add(11,5)
# subtract = child_class.subtract(45,8)
# pro = child_class.product(4,5)
# divide = child_class.divide(11, 5)
#
# print(f"Addition = {add} \nSubtraction: {subtract} \nProduct:{pro} \ndivide: {divide}")

# Create a base class called Vehicle with method like brand and speed.
# Create two child classes: Car and Bike.
# Add a custom method in each child class (like honk() or wheelie()).

# Parent class
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def drive(self):
#         print(f"{self.brand} is driving.")
#
# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)  # Call the parent class constructor
#         self.model = model
#
#     # def drive(self):
#     #     super().drive()
#
#     def show_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}")
#
# my_car = Car("Toyota", "Corolla")
# my_car.drive()
# my_car.show_info()

# import package as p
#
# p.Girlpower("Susmita", 20, "hetauda")
# p.Girlpower("Rachana", 19, "Hetauda")
# p.Girlpower("Krishna", 19,"Hetauda")
# p.Girlpower("Isha", 19, "Hetauda")



