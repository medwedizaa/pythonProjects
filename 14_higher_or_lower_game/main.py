from art import logo, vs
from game_data import data
import random

score = 0
a = random.choice(data)
b = random.choice(data)
is_wrong = False
while True:
    print(logo)
    if is_wrong:
        print(f"Sorry, that's wrong! Final score is {score}")
        break
    if score > 0:
        print(f"You are right! Current score is {score}")

    print(f"Compare A: {a['name']}, {a['description']} from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']} from {b['country']}")
    guess = input("Who has more followers? Type A or B: ")
    if ((guess == "A" and a['follower_count'] > b['follower_count'])
            or (guess == "B" and a['follower_count'] < b['follower_count'])):
        score += 1
        a = b
        b = random.choice(data)

    else:
        is_wrong = True
