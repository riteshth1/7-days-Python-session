# Game link
# https://appbrewery.github.io/python-day3-demo/
# This should be your output

# Exercise:
# https://github.com/ashutoshkrris/100-Days-of-Python?tab=readme-ov-file
# https://github.com/ashutoshkrris/100-Days-of-Python/tree/master/Day%203
#
# This is for me
# https://github.com/ashutoshkrris/100-Days-of-Python?tab=readme-ov-file

print(r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
player_choice = input("Type 'left' or 'right': ").strip().lower()

if player_choice == 'right':
    print("You fall into a hole. Game Over💀")
elif player_choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    second_choice = input("Type 'wait' to wait for a boat. Type 'swim' to across.").strip().lower()
    if second_choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door_choice = input("One red, one yellow and one blue. Which color do you choose?").strip().lower()

        if door_choice == "red":
            print("You're Burned by Fire. Game Over💀")
        elif door_choice == "blue door":
            print("You're Eatten by Beasts. Game Over💀")
        elif door_choice == "yellow":
            print("You have become the Billionaire by obtaining the Treasure.Congrats!!🎉🎊")
        else:
            print("Invalid user input..")

    elif second_choice == "swim":
        print("You're attacked by trout. Game over💀")
    else:
        print("Invalid input.")
else:
    print("Invalid Input.")





