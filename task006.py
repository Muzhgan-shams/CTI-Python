# Treasure Island
# Acsii Art
print(
    '''
*******************************************************************************
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
*******************************************************************************
'''
)
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

crossroad = input(
    "You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if crossroad == 'left':
    lake = input(
        "You come to a lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if lake == 'wait':
        house = input(
            "You arrive at a house with 3 doors: red, yellow, and blue. Which color do you choose? ").lower()
        if house == 'yellow':
            print("You found the treasure room 🎉")
            chests = input(
                "You see 3 chests: A, B, and C. Which one do you open? ").lower()
            if chests == 'a':
                print("Chest A is full of gold! You won 🎉🥳")
            else:
                print("Game over 🥲")
        else:
            print("Game over 🥲")
    else:
        print("Game over 🥲")
else:
    print("Game over 🥲")
