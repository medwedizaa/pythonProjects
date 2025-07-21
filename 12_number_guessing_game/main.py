import random
def greeting():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
greeting()
mode = input("Choose a difficulty. Print 'easy' or 'hard': ")
lives = 0

if mode == 'easy':
    lives = 10
else:
    lives = 5

while True:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")

    lives -= 1
    if lives > 0:
        print("Guess again.")
    else:
        print(f"You have run out of guessed. The number was {number}")
        print("Restart to play again")
        break
