import tkinter as tk
import random

window = tk.Tk()
window.geometry("600x400")
window.config(bg="#ffffff")
window.title("The Guessing Game")

#TARGET = random computer generated number between 0 and 100. Declare RETRIES variable.
TARGET = random.randint(0, 100)
RETRIES = 0

def update_result(text):
    result.config(text=text)

def new_game():
    guess_button.config(state='normal')
    number_form.config(state='normal')
    global TARGET, RETRIES
    TARGET = random.randint(0, 100)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 100")

#Game's main loop
def play_game():
    global RETRIES

    userGuess = int(number_form.get())

    if userGuess != TARGET:
        RETRIES += 1

        result = "Sorry, try again"
        if userGuess > 100 or userGuess < 0:
            hint = "Woops. \nYou're supposed to guess between 1 and 100. Try again"
        elif userGuess >= (TARGET - 5) and userGuess <= (TARGET + 5):
            hint = "Getting hot."
        elif userGuess  >= (TARGET - 10) and userGuess <= (TARGET + 10):
            hint = "Getting warmer."
        elif TARGET < userGuess:
            hint = "The number lies between 0 and {}".format(userGuess)
        else:
            hint = "The number lies between {} and 100".format(userGuess)
        result += "\n\nHINT :\n" + hint
    else:
        result = "Congrats! You've guessed the correct number after {} tries!".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click New Game to start a new game"

    update_result(result)

#UI placement
exit_button = tk.Button(window,text="Exit Game", font=("Arial",14), fg="Black", bg="#ffffff", command=exit)
exit_button.place(x=300,y=320)

title = tk.Label(window,text="The Guessing Game",font=("Arial", 24), fg="Black",bg="#ffffff")
result= tk.Label(window, text= "Click New Game to start", font=("Arial",12), fg="Black", bg="#ffffff", justify=tk.LEFT)
title.place(x=170, y=50)
result.place(x= 180, y=210)

play_button = tk.Button(window, text="New Game", font=("Arial", 14), fg="Black", bg="#ffffff", command=new_game)
guess_button = tk.Button(window, text="Guess", font=("Arial", 14), state='disabled', fg="Black", bg="#ffffff", command=play_game)
guess_button.place(x=400, y=147)
play_button.place(x=170, y=320)

guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=("Arial", 12), state='disabled', textvariable=guessed_number)
number_form.place(x=180, y=150)

window.mainloop()