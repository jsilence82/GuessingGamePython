import tkinter as tk
import random

window = tk.Tk()
window.geometry("400x400")
window.config(bg="#ffffff")
window.resizable(height=0, width=0)
window.title("Take a Guess")

# Declare global variables. random computer generated number between 0 and 100. tries = number of .
computer_number = random.randint(0, 100)
tries = 0


def update_result(text):
    result.config(text=text)


def new_game():
    guess_button.config(state='normal')
    number_form.config(state='normal')
    global computer_number, tries
    computer_number = random.randint(0, 100)
    tries = 0
    update_result(text="Guess a number between\n 1 and 100")


# Game's main loop
def play_game():
    global tries

    user_guess = int(number_form.get())

    if user_guess != computer_number:
        tries += 1

        result = "Sorry, try again"
        if user_guess > 100 or user_guess < 0:
            hint = "Woops. \nYou're supposed to guess between 1 and 100. Try again"
        elif (computer_number - 5) <= user_guess <= (computer_number + 5):
            hint = "Getting hot. Within 5"
        elif (computer_number - 10) <= user_guess <= (computer_number + 10):
            hint = "Getting warmer. Within 10"
        elif computer_number < user_guess:
            hint = "The number lies between 0 and {}".format(user_guess)
        else:
            hint = "The number lies between {} and 100".format(user_guess)
        result += "\n\nHINT :\n" + hint
    else:
        result = "Congrats! \nYou've guessed the correct number after {} tries!".format(tries)
        guess_button.configure(state='disabled')
        result += "\n" + "Click New Game to start a new game"

    update_result(result)


# UI placement
exit_button = tk.Button(window, text="Exit Game", font=("Arial", 14), fg="Black", bg="#ffffff", command=exit)
exit_button.place(x=250, y=320)


title = tk.Label(window, text="Take a Guess", font=("Arial", 24), fg="Black", bg="#ffffff")
result = tk.Label(window, text="Click New Game to start", font=("Arial", 12), fg="Black", bg="#ffffff", justify=tk.LEFT)
title.place(x=75, y=50)
result.place(x=75, y=210)


play_button = tk.Button(window, text="New Game", font=("Arial", 14), fg="Black", bg="#ffffff", command=new_game)
guess_button = tk.Button(window, text="Guess", font=("Arial", 14), state='disabled', fg="Black", bg="#ffffff", command=play_game)
guess_button.place(x=275, y=150)
play_button.place(x=75, y=320)

guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=("Arial", 12), state='disabled', textvariable=guessed_number)
number_form.place(x=75, y=165)

window.mainloop()
