from random import randint

from art import vs,logo
from game_data import data

SCORE = 0
game = True
print(logo)

player_a = data[randint(0, 49)]
print(f"Compare A: {player_a['name']}, a {player_a['description']} from {player_a['country']}.")

def compare(a,b):
    if a > b:
        return 'a'
    elif b > a:
        return 'b'
    else:
        return a



while game:
    print(vs)

    player_b = data[randint(0, 49)]
    print(f"Compare B: {player_b['name']}, a {player_b['description']} from {player_b['country']}.")

    user_answer = input("who has more followers? Type 'A' or 'B': ").lower()

    if compare(player_a['follower_count'], player_b['follower_count']) == user_answer :
        player_a = player_b
        print(f"Compare A: {player_a['name']}, a {player_a['description']} from {player_a['country']}.")
        SCORE += 1

    else:
        print(f"Sorry, that's wrong. final score: {SCORE}")
        game = False
