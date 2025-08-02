import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cycle_number = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    reset_button.config(state="disabled")
    start_button.config(state="normal")
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global cycle_number
    cycle_number = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global cycle_number
    cycle_number += 1
    start_button.config(state="disabled")
    reset_button.config(state="normal")

    if cycle_number == 8:
        time_to_start = LONG_BREAK_MIN
        title.config(text="Break", fg=RED)
    elif cycle_number % 2 == 1:
        time_to_start = WORK_MIN
        title.config(text="Work", fg=GREEN)
    else:
        time_to_start = SHORT_BREAK_MIN
        title.config(text="Break", fg=PINK)

    count_down(time_to_start * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(50, count_down, count - 1)
    else:
        start_timer()
        check_marks.config(text="✓" * math.floor(cycle_number / 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "normal"))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(108, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.config(state="disabled")
reset_button.grid(column=2, row=2)

check_marks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))
check_marks.grid(column=1, row=3)

window.mainloop()
