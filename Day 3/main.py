#Topics to be covered

#  python list syntax adding, deleting and updating item in the list
#  Who will pay the bill? --> Game
# indexing and Nested lists
# Index error
# Assignment --> Rock, scissor, paper game
# fizzbuzz
# Password generator

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# to add numbers

# def add(a ,b):
#     """To add two numbers """
#     return (a+b)
#
# print(add(b = 15, a = 10))

# def Check(num):
#     """To check a number is odd or even"""
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
# number = int(input("Enter a number:"))
# Check(number)

# list
# a = [1,2,4,8,"Risan", "Rosa", "Rachana", 4.58, 'Bikesh', "bidhan"]
#
# # print(a[10])
# # loop in list
# # for i in a:
# #     print(i)
#
# # # Add item to list
# # a.append(["Isha",'krishna'])
# # print(a[10][1])
# # a.remove()
# # a.pop()
# #
# # print(a)
#
# # Dictionary
# # bhandar = {
# #     'a':'A',
# #     'b' : 'B',
# #     'c' : 'C'
# # }
# #
# # # Access element of dictionary
# # print(bhandar['c'])
# #
# # # Update the value
# # bhandar['c'] = "Ritesh"
# #
# # print(bhandar)
# #
# # # Iteration in dictionary
# # for key in bhandar:
# #     print(bhandar[key])
#
# # dictionary of list
# a = {
#     'name' : ['risan', 'bikesh'],
#     'address': ['htd', 'butwal']
# }
#
# # list of dictionary
# b = [
#     {'name': 'ritesh'},
#     {'address': "Htd"}
# ]


from random import randint

# computer choice : 0 (rock), 1 (paper), or 2 (scissors)
choice = randint(0, 2)

num = int(input("Enter your choice: 0 for rock 🪨, 1 for paper 📃, 2 for scissors ✂: "))

if num < 0 or num > 2:
    print("Enter a valid choice idiot 🤨")
else:
    if num == 0:
        print("Your choice is rock 🪨\nNow it's your opponent's turn...")
    elif num == 1:
        print("Your choice is paper 📃\nNow it's your opponent's turn...")
    elif num == 2:
        print("Your choice is scissors ✂\nNow it's your opponent's turn...")

    # Show opponent's choice
    if choice == 0:
        print("Opponent chose rock 🪨")
    elif choice == 1:
        print("Opponent chose paper 📃")
    elif choice == 2:
        print("Opponent chose scissors ✂")

    # Determine the result
    if num == choice:
        print("It's a draw 🤝")
    elif num == 0 and choice == 2 or num == 1 and choice == 0 or num == 2 and choice == 1:
        print("Congratulations... You won 🏆")
    else:
        print("You lost 😓")



















