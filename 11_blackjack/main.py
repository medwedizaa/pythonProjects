from art import logo
import random

users_hand = []
pc_hand = []
run = True

def greetings():
    print(logo)

def get_random_card():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def print_cards():
    print("-" * 40)
    print(f"    Your cards: {users_hand}. Current score: {sum(users_hand)}")
    print(f"    Computer's first card: {pc_hand[0]}.")

def print_finish_score():
    print("-" * 40)
    print(f"  Your final hand: {users_hand}. Final score: {sum(users_hand)}")
    print(f"  Computer's final hand: {pc_hand}. Final score: {sum(pc_hand)}")
    print("-" * 40)

def print_lose():
    print_finish_score()
    print("You lose (ノ ゜Д゜)ノ ︵ ┻━┻.")

def print_lose_over():
    print_finish_score()
    print("You vent over. You lose L(° O °L)")

def print_win():
    print_finish_score()
    print("You win (｡◕‿‿◕｡)")

def print_draw():
    print_finish_score()
    print("It's a draw ¯\_(ツ)_/¯")

def fill_pc_hand():
    if sum(pc_hand) < 17:
        pc_hand.append(get_random_card())
        fill_pc_hand()

def continue_game():
    continue_answer = input("Type 'y' to get another card, type 'n' to pass: ")
    if continue_answer == 'y':
        users_hand.append(get_random_card())
        print_cards()
        if sum(users_hand) > 21:
            print_lose_over()
        else:
            continue_game()
    else:
        fill_pc_hand()
        if sum(pc_hand) > 21:
            print_win()
        elif sum(pc_hand) == sum(users_hand):
            print_draw()
        elif sum(pc_hand) > sum(users_hand):
            print_lose()
        else:
            print_win()

while run:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == 'y':
        users_hand = []
        pc_hand = []
        greetings()

        users_hand.append(get_random_card())
        users_hand.append(get_random_card())
        pc_hand.append(get_random_card())
        pc_hand.append(get_random_card())
        print_cards()

        continue_game()
    else:
        run = False
    print()
