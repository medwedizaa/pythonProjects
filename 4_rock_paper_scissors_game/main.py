import random

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

images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_choice > 2 or user_choice < 0:
    print("Ok, that wasn't the option. I think you ment 0")
    user_choice = 0

print(images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
print(images[computer_choice])

if user_choice == computer_choice:
    print("Oh, it's a draw my friend :)")
elif user_choice - computer_choice == 1 or user_choice - computer_choice == -2:
    print("You win! congratulations!")
else:
    print("You loose. That's a pity :(")