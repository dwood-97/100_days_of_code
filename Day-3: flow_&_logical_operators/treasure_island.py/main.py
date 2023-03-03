print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

left_or_right = input('As you navigate down the path you come to a fork, would you like to go right or left? Type either "Right" or "Left".\n\n').lower()

if left_or_right == "left":
    swim_or_wait = input('You chose the correct path! You reach the ocean and see an island in the distance and have a feeling the treasure is there and need to get to it first, however the tide is really bad right now. Do you swim to the island now or wait? Type either "Swim" or "Wait"\n\n').lower()
    if swim_or_wait == "wait":
        which_door = input ('Now that you made it to the island, you see a building. The building has three doors, a red door, a blue door and a green door. Which door would you like to open? Type "Red", "Green" or  "Blue"\n\n').lower()    
        if which_door == "blue":
            print("You open the blue door, and see a treasure chest overfilled with gold and jewlery!")
        elif which_door == "green":
            print("You open the green door, and behind it are a group of aggresive savages! You do not survive.")
        elif which_door == "red":
            print("You open the red door, and it's a trap! The room bursts into flames, and the building burns to the ground. You did not survive.")
        else:
            print("You have not chosen one of the options. Game over.")
    elif swim_or_wait == "swim":
        print ("The ocean tide was too extreme and you did not survive")
    else:
        print("You have not chosen one of the options. Game over.")
elif left_or_right == "right":
    print ("You go down the path on the right and fall into a trop hole and you did not survive")
else:
    print("You have not chosen one of the options. Game over.")