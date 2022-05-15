import tkinter as tk
import random

window = tk.Tk()
window.geometry("600x400")
window.config(bg="#fffAfA")
window.title("The Guessing Game")

TARGET = random.randint(0, 100)
RETRIES = 0

def update_result(text):
    result.config(text=text)

def new_game():
    guess_button.config(state='normal')
    global TARGET, RETRIES
    TARGET = random.randint(0, 100)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 100")

def play_game():
    global RETRIES

    userGuess = int(number_form.get())

    if userGuess != TARGET:
        RETRIES += 1

        result = "Sorry, try again"
        if TARGET < userGuess:
            hint = "The number lies between 0 and {}".format(userGuess)
        else:
            hint = "The number lies between {} and 100".format(userGuess)
        result += "\n\nHINT :\n" + hint
    else:
        result = "Congrats! You've guessed the correct number after {} tries!".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click Play to start a new game"

    update_result(result)


exit_button = tk.Button(window,text="Exit Game", font=("Arial",14), fg="Black", bg="#fffAfA", command=exit)
exit_button.place(x=300,y=320)

title = tk.Label(window,text="The Guessing Game",font=("Arial", 24), fg="Black",bg="#fffAfA")
result= tk.Label(window, text= "Click Play to start a new game", font=("Arial",12), fg="Black", bg="#fffAfA", justify=tk.LEFT)
title.place(x=170, y=50)
result.place(x= 180, y=210)

play_button = tk.Button(window, text="Play", font=("Arial", 14), fg="Black", bg="#fffAfA", command=new_game)
guess_button = tk.Button(window, text="Guess", font=("Arial", 14), state='disabled', fg="Black", bg="#fffAfA", command=play_game)
guess_button.place(x=350, y=147)
play_button.place(x=170, y=320)

guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=("Arial", 12), textvariable=guessed_number)
number_form.place(x=180, y=150)


window.mainloop()