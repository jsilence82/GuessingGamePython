# Guessing game built in python, using Tkinter for GUI.
import tkinter as tk
import random


# Tkinter configure the game window. Window is not resizable to prevent user from enlarging the window since the
# buttons are not resizeable.
window = tk.Tk()
window.geometry("400x400")
window.config(bg="#ffffff")
window.resizable(width=False, height=False)
window.title("Take a Guess")


# Global variables. Random computer generated number between 0 and 100. Tries = number of user attempts.
# Used by new_game function and the main_loop function.
computer_number = random.randint(0, 100)
tries = 15


# Configure the result label to display the results from the game's main loop.
def update_result(text):
    result.config(text=text)


# Function to initialize a new game when the "New Game" button is pressed
def new_game():
    guess_button.config(state='normal')
    number_form.config(state='normal')
    guesses_numbers.config(state='normal')
    global computer_number, tries
    computer_number = random.randint(0, 100)
    tries = 15
    guesses_numbers.config(text=str(tries))
    update_result(text="Guess a number between\n 1 and 100")


# Game loop. Exception placed in case the user enters an invalid value.
def play_game():

    global tries

    try:
        user_guess = int(number_form.get())

        if tries == 0:
            result = "Sorry. Out of guesses. \nThe correct number is {}".format(str(computer_number))
            guess_button.configure(state='disabled')
            result += "\n" + "Click New Game to start a new game"

        elif user_guess != computer_number:
            tries -= 1

            result = "Nope, that's not the number. Try again"
            if user_guess > 100 or user_guess < 0:
                hint = "You're supposed to guess between 1 and 100. Try again"
                result = "Woops. Something's not right."
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
            result = "Congrats! \nYou've guessed the number after \n{} tries!".format(tries)
            guess_button.configure(state='disabled')
            result += "\n" + "Click New Game to start a new game"
    except Exception as e:
        result = "Are you sure that's a number? Try again"

    update_result(result)
    guesses_numbers.config(text=str(tries))


# UI place Labels and titles
title = tk.Label(window, text="Take a Guess", font=("Arial", 24), fg="Black", bg="#ffffff")
result = tk.Label(window, text="Click New Game to start",
                  font=("Arial", 12), fg="Black", bg="#ffffff", justify=tk.LEFT)
guesses = tk.Label(window, text="Guesses Left: ", font=("Arial", 15), fg="Black", bg="#ffffff")
guesses_numbers = tk.Label(window, text=str(tries), font=("Arial", 15), fg="Black", bg="#ffffff")
guesses.place(x=100, y=100)
guesses_numbers.place(x=230, y=100)
title.place(x=75, y=30)
result.place(x=75, y=210)


# UI place buttons
exit_button = tk.Button(window, text="Exit Game", font=("Arial", 14), fg="Black", bg="#ffffff", command=exit)
exit_button.place(x=250, y=320)
play_button = tk.Button(window, text="New Game",
                        font=("Arial", 14), fg="Black", bg="#ffffff", command=new_game)
guess_button = tk.Button(window, text="Guess",
                         font=("Arial", 14), state='disabled', fg="Black", bg="#ffffff", command=play_game)

# Binding Return key to guess_button
window.bind('<Return>', lambda event=None: guess_button.invoke())

guess_button.place(x=275, y=150)
play_button.place(x=75, y=320)


# UI place forms
guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=("Arial", 12), state='disabled', textvariable=guessed_number)
number_form.place(x=75, y=165)

window.mainloop()
