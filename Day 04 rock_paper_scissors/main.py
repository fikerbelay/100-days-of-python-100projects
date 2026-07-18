rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
signs = [rock, paper, scissors]

import random
while True:
    user = int(input("What do ypu choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    if user != 0 or user != 1 or user != 2:
        print("Invalid input. Try again.")
        continue

    computer = random.randint(0, 2)

    print(f' \n You chose  {signs[user]} \n computer chose {signs[computer]}')

    if user == computer:
        print("It's a draw!")
    elif user == 0 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 0:
        print("You lose")
    else:
        print("You win")
