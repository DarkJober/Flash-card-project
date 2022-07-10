from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

# ---------------------------- DATA READING ------------------------------- #

try:
    df = pandas.read_csv(r"data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv(r"data/french_words.csv")

to_learn = df.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #

def remove_from_list():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def turn_card():
    global current_card
    canvas.itemconfig(card_background, image=background_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(guess, text=current_card["English"], fill="white")


def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=background_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(guess, text=current_card["French"], fill="black")
    flip_time = window.after(3000, func=turn_card)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_time = window.after(3000, func=turn_card)

# FLASHY CARD
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
background_front = PhotoImage(file="images/card_front.png")
background_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=background_front)
canvas.grid(column=0, row=0, columnspan=2)

# TEXT ON CARD
language = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
guess = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))


# BUTTONS
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=remove_from_list)
right_btn.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()