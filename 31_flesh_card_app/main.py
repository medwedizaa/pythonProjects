from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
delay_timer = None
current_word = {}


# Show a random word
def update_word():
    global delay_timer, current_word
    if delay_timer is not None:
        window.after_cancel(delay_timer)
    random_word = random.choice(words_to_learn)
    current_word = random_word
    show_french_word(random_word['French'])
    delay_timer = window.after(3000, show_english_word, random_word['English'])


def show_french_word(word):
    canvas.itemconfigure(card, image=front_image)
    canvas.itemconfigure(title_label, text='French', fill="black")
    canvas.itemconfigure(word_label, text=word, fill="black")


def show_english_word(word):
    canvas.itemconfigure(card, image=back_image)
    canvas.itemconfigure(title_label, text='English', fill="white")
    canvas.itemconfigure(word_label, text=word, fill="white")


# Mark a word as known
def know_word():
    words_to_learn.remove(current_word)
    pd.DataFrame.from_records(words_to_learn).to_csv("./data/words_to_learn.csv", index=False)
    update_word()


# UI setup
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=front_image)
title_label = canvas.create_text(400, 150, text="", fill='black', font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", fill='black', font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=know_word)
right_button.grid(column=0, row=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=update_word)
wrong_button.grid(column=1, row=2)

# Data preparation
try:
    words_to_learn = pd.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    words_to_learn = pd.read_csv("./data/french_words.csv").to_dict(orient="records")
print(len(words_to_learn))
update_word()

window.mainloop()
