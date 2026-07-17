from random import randint
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

# Write your code below this line 👇
game = True;
while game:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    computer_choice = randint(0, 2)
    print("you choose")
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
    print("computer choose: ")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)
    if computer_choice == user_choice:
        print("its a tie")
    elif computer_choice == 1 and user_choice == 0:
        print("computer won you lose")
    elif computer_choice == 2 and user_choice == 1:
        print("computer won you lose")
    elif computer_choice == 0 and user_choice == 2:
        print("computer won you lose")
    elif computer_choice == 0 and user_choice == 1:
        print("you won computer lost")
    elif computer_choice == 1 and user_choice == 2:
        print("you won computer lost")
    elif computer_choice == 2 and user_choice == 0:
        print("you won computer lost")
    game = input("wanna play again? yes/no ").lower()
    if game == "yes":
        game = True
    else:
        game = False






