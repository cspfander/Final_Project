"""
Program: final_project_hangman.py
Author: Colten pfander
Date last modified: 11/26/19


The purpose of this program is to make a GUI that will allow the user to play the game Hangman.
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
        self.magic_number = random.randint(0, 49)
        self.list_of_words = ["coil", "suspect", "route", "dynamic", "number", "request", "prefer", "certain",
                              "smell, wilderness",
                              "pleasant", "yard", "husky", "inject", "slope", "unsuitable", "lunch", "best", "rings",
                              "guard", "whip",
                              "shoes", "ready", "tasteful", "cloudy", "tired", "knowledge", "cycle", "unsightly",
                              "loss", "gaping",
                              "produce", "line", "important", "angle", "floor", "food", "educated", "threatening",
                              "acid", "draconian",
                              "event", "nauseating", "sturdy", "smiling", "scorch", "quaint", "supreme", "start",
                              "flaky"]
        self.magic_word = self.list_of_words[self.magic_number]
        self.guessed_list = []
        self.guessed_correctly = []
        self.num_of_guesses = 6

    def add_guess(self, temp_guess):
        """
        Function to add the guess into the list of guessed letters
        :param temp_guess: Accepts the guess as input
        :return:
        """
        allowed_guess_input = set("abcdefghijklmnopqrstuvwxyz")
        if str(temp_guess).isdigit():
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
            raise InvalidGuess
        else:
            a_guess = temp_guess.lower()
            if allowed_guess_input.issuperset(a_guess):
                for letter in self.magic_word:
                    if a_guess == letter:
                        self.guessed_correctly.append(a_guess)
                        matched_letters += 1
                if matched_letters > 0:
                    messagebox.showinfo("Correct!", "Yes! There is " + str(matched_letters) + " " + a_guess)
                    tk.Label(m, text=letters_for_game.guessed_list).grid(row=5, column=1)
                    tk.Label(m, text=letters_for_game.guessed_correctly).grid(row=2, column=1)
                    tk.Label(m, text=str(letters_for_game.num_of_guesses)).grid(row=6, column=1)
                else:
                    messagebox.showinfo("Sorry!", "Unfortunately there are no '" + a_guess + "' in the word.")
                    self.num_of_guesses -= 1
                    tk.Label(m, text=letters_for_game.guessed_list).grid(row=5, column=1)
                    tk.Label(m, text=letters_for_game.guessed_correctly).grid(row=2, column=1)
                    tk.Label(m, text=str(letters_for_game.num_of_guesses)).grid(row=6, column=1)

                    if self.num_of_guesses == 0:
                        messagebox.showinfo("You Lose!", "Uh oh! You are out of guesses and have lost!")
                        exit_button.invoke()


def guess():
    """
    This is the function that will actually run when the guess button is clicked, calling the add guess and check guess
    :return:
    """
    allowed_guess_input = set("abcdefghijklmnopqrstuvwxyz")
    letter_guessed = new_guess.get().lower()
    if allowed_guess_input.issuperset(letter_guessed):
        if len(letter_guessed) < 0 or len(letter_guessed) > 1:
            raise InvalidGuess("Please only guess 1 letter!")
        else:
            if letter_guessed not in letters_for_game.guessed_list:
                letters_for_game.add_guess(letter_guessed)
                letters_for_game.check_guess(letter_guessed)
            else:
                messagebox.showinfo("Sorry!", "This letter has already been guessed, try guessing another letter!")
    else:
        raise InvalidGuess("Please only guess letters!")


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
        global letters_for_game, num_of_guesses
        letters_for_game = LetterGuesser()
        m = tk.Tk()
        m.title("Hangman")
        length_of_magic_word = len(letters_for_game.magic_word)
        tk.Label(m, text="The magic word is " + str(length_of_magic_word) + " letters long!").grid(row=1, columnspan=2)
        tk.Label(m, text="Current letters found in the magic word:").grid(row=2)
        tk.Label(m, text="Please guess a letter:").grid(row=3, columnspan=2)
        new_guess = tk.Entry(m)
        new_guess.grid(row=4)
        guess_button = tk.Button(m, text="Guess", command=guess, width=14)
        guess_button.grid(row=4, column=1)
        tk.Label(m, text="Already guessed letters:").grid(row=5)
        tk.Label(m, text=letters_for_game.guessed_list).grid(row=5, column=1)
        tk.Label(m, text="Guesses remaining: ").grid(row=6)
        tk.Label(m, text=str(letters_for_game.num_of_guesses)).grid(row=6, column=1)
        exit_button = tk.Button(m, text="Exit", command=m.destroy, width=16)
        exit_button.grid(row=7, columnspan=2)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        tk.Label(m, text="Start Time: " + current_time).grid(row=8, column=1)
        m.mainloop()
    except ValueError:
        print("The program has been closed due to a ValueError!")
