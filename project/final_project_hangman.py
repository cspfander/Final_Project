"""
Program: final_project_hangman.py
Author: Colten pfander
Date last modified: 11/26/19


The purpose of this program is to make a GUI that will allow the user to play a more friendly game of Hangman.
"""
import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class LetterGuesser:
    """
    Class to hold the primary aspects of the game like guesses and magic words
    """

    def __init__(self):
        self.magic_number = random.randint(0, 100)
        self.list_of_words = ["coil", "suspect", "route", "dynamic", "number", "request", "prefer", "certain",
                              "smell, wilderness", "pleasant", "yard", "husky", "inject", "slope", "unsuitable",
                              "lunch", "best", "rings", "guard", "whip", "shoes", "ready", "tasteful", "cloudy",
                              "tired", "knowledge", "cycle", "unsightly", "lose", "gaping", "produce", "line",
                              "important", "angle", "floor", "food", "educated", "threatening", "acid", "draconian",
                              "event", "nauseating", "sturdy", "smiling", "scorch", "quaint", "supreme", "start",
                              "flaky", "appreciate", "thundering", "plate", "minor", "offer", "loaf", "fork", "absurd",
                              "soap", "grade", "stereotype", "trouble", "oil", "fuzzy", "example", "steam", "bow",
                              "fire", "manage", "tickle", "bath", "illegal", "bad", "players", "toxic", "silly", "mean",
                              "ban", "hostile", "spotted", "hostage", "fuse", "mortar", "border", "rush", "ash", "lit",
                              "preparation", "sledge", "tango", "intentionally", "feeding", "reported", "mouse", "pad",
                              "keyboard", "computer", "shields", "cheese", "slow", "friendship", "tactical", "ilk"]
        self.magic_word = self.list_of_words[self.magic_number]
        self.guessed_list = []
        self.num_of_guesses = 6
        self.listed_magic_word = list(self.magic_word)
        self.blanks = "_" * len(self.listed_magic_word)
        self.blanks_list = list(self.blanks)

    def add_guess(self, temp_guess):
        """
        Function to add the guess into the list of guessed letters
        :param temp_guess: Accepts the guess as input
        :return:
        """
        allowed_guess_input = set("abcdefghijklmnopqrstuvwxyz")
        if str(temp_guess).isdigit():
            messagebox.showinfo("Invalid Guess", "Please only guess letters!")
            raise InvalidGuess
        else:
            a_guess = temp_guess.lower()
            if allowed_guess_input.issuperset(a_guess):
                self.guessed_list.append(a_guess)
            else:
                raise InvalidGuess

    def check_guess(self, temp_guess):
        """
        Function that will take the guess and cross check it with the magic word to see if it contains any of that letter
        :param temp_guess: Accepts the guess as input
        :return:
        """
        matched_letters = 0
        allowed_guess_input = set("abcdefghijklmnopqrstuvwxyz")
        if str(temp_guess).isdigit():
            messagebox.showinfo("Invalid Guess", "Please guess only letters!")
            raise InvalidGuess
        else:
            a_guess = temp_guess.lower()
            if allowed_guess_input.issuperset(a_guess):
                for x in range(0, len(letters_for_game.listed_magic_word)):
                    if a_guess == letters_for_game.listed_magic_word[x]:
                        letters_for_game.blanks_list[x] = a_guess
                        matched_letters += 1
                        if letters_for_game.blanks_list == letters_for_game.listed_magic_word:
                            messagebox.showinfo("You Win!", "CONGRATULATIONS, YOU WIN!\nYou have correctly guessed the "
                                                            "word '" + letters_for_game.magic_word +
                                                "'!\nThe program will now close, thank you for playing.")
                            print("Thanks for playing!")
                            exit_button.invoke()
                            exit()
                if matched_letters > 0:
                    messagebox.showinfo("Correct!", "Yes! There is " + str(matched_letters) + " " + a_guess)
                    tk.Label(m, text=letters_for_game.guessed_list).grid(row=5, column=1)
                    tk.Label(m, text=letters_for_game.blanks_list).grid(row=2, column=1)
                    tk.Label(m, text=str(letters_for_game.num_of_guesses)).grid(row=6, column=1)
                else:
                    messagebox.showinfo("Sorry!", "Unfortunately there are no '" + a_guess + "' in the word.")
                    self.num_of_guesses -= 1
                    tk.Label(m, text=letters_for_game.guessed_list).grid(row=5, column=1)
                    tk.Label(m, text=letters_for_game.blanks_list).grid(row=2, column=1)
                    tk.Label(m, text=str(letters_for_game.num_of_guesses)).grid(row=6, column=1)
                    if self.num_of_guesses == 0:
                        messagebox.showinfo("You Lose!",
                                            "Uh oh! You are out of guesses and have lost!\nThe magic word was '"
                                            + letters_for_game.magic_word +
                                            "'\nThe program will now close, thank you for playing.")
                        print("Thanks for playing!")
                        exit_button.invoke()


def guess():
    """
    This is the function that will actually run when the guess button is clicked, calling the add guess and check guess
    :return:
    """
    allowed_guess_input = set("abcdefghijklmnopqrstuvwxyz")
    letter_guessed = new_guess.get().lower()
    if allowed_guess_input.issuperset(letter_guessed):
        if len(letter_guessed) <= 0 or len(letter_guessed) > 1:
            messagebox.showinfo("Invalid Guess", "Please guess 1 letter at a time!")
            raise InvalidGuess("Please only guess 1 letter!")
        else:
            if letter_guessed not in letters_for_game.guessed_list:
                letters_for_game.add_guess(letter_guessed)
                letters_for_game.check_guess(letter_guessed)
            else:
                messagebox.showinfo("Sorry!", "This letter has already been guessed, try guessing another letter!")
    else:
        messagebox.showinfo("Invalid Guess", "Please guess only letters!")
        raise InvalidGuess("Please only guess letters!")
    new_guess.delete(0, 1)


def start_game():
    """
    This function will start by creating a new instance of the game and resetting attempts remaining
    :return:
    """
    pass


class InvalidGuess(Exception):
    # This custom exception gets raised if the user's guess does not meet the accepted conditions
    pass


if __name__ == '__main__':
    try:
        global num_of_guesses
        letters_for_game = LetterGuesser()
        m = tk.Tk()
        m.title("Hangman")
        length_of_magic_word = len(letters_for_game.magic_word)
        tk.Label(m, text="The magic word is " + str(length_of_magic_word) + " letters long!").grid(row=1, columnspan=2)
        tk.Label(m, text="Letters found:").grid(row=2)
        tk.Label(m, text=letters_for_game.blanks_list).grid(row=2, column=1)
        tk.Label(m, text="Please guess a letter:").grid(row=3, columnspan=2)
        new_guess = tk.Entry(m)
        new_guess.grid(row=4)
        guess_button = tk.Button(m, text="Guess", command=guess, width=14)
        guess_button.grid(row=4, column=1)
        m.bind('<Return>', lambda event=None: guess_button.invoke())
        tk.Label(m, text="Already guessed letters:").grid(row=5)
        tk.Label(m, text=letters_for_game.guessed_list).grid(row=5, column=1)
        tk.Label(m, text="Guesses remaining: ").grid(row=6)
        tk.Label(m, text=str(letters_for_game.num_of_guesses)).grid(row=6, column=1)
        exit_button = tk.Button(m, text="Exit", command=m.destroy, width=16)
        exit_button.grid(row=7, columnspan=2)
        now = datetime.now()
        current_time = now.strftime('%I:%M %m/%d/%Y')
        tk.Label(m, text="Start Time: " + current_time).grid(row=8, column=1)
        m.mainloop()
    except ValueError:
        print("The program has been closed due to a ValueError!")
