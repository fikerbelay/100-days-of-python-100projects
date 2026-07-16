print("Welcome to Treasure island. \nYour mission is to find the treasure.")
print("You're at a cross road. where do you want to go? \n")
direction = input('Type "left" or "right" ')

if direction.upper() == "LEFT":
    print("You've come to a lake. There is an island in the middle of the lake.")
    boat_or_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across.')

    if boat_or_swim.upper() == "WAIT":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which colour do you choose?")

        if door.upper() == "RED":
            print("It's a room full of fire. Game Over.")

        elif door.upper() == "YELLOW":
            print("You found the treasure! You Win!")

        elif door.upper() == "BLUE":
            print("You enter a room of beasts. Game Over.")

        else:
            print("Invalid input. restart the game.")

    elif boat_or_swim.upper() == "SWIM":
        print("You get attacked by an angry trout. Game Over.")

    else:
        print("Invalid input. restart the game.")

elif direction.upper() == "RIGHT":
    print("You fell into a hole. Game Over.")

else:
    print("Invalid input. restart the game.")