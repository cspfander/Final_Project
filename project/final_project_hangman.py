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
        self.magic_number = random.randint(1, 50)
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

    def add_guess(self, temp_guess):
        """
        Function to add the guess into the list of guessed letters
        :param temp_guess:
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

    def check_guess(self, a_guess):
        """
        Function that will take the guess and cross check it with the magic word to see if it contains any of that letter
        :param a_guess:
        :return:
        """
        for letter in self.magic_word:
            if a_guess == letter:
                pass
        pass


def guess():
    """
    This is the function that will actually run when the guess button is clicked, calling the add guess and check guess
    :return:
    """
    try:
        allowed_guess_input = set("abcdefghijklmnopqrstuvwxyz")
        letter_guessed = new_guess.get().lower()
        if allowed_guess_input.issuperset(letter_guessed):
            if len(letter_guessed) < 0 or len(letter_guessed) > 1:
                raise InvalidGuess("Please only guess 1 letter!")
            else:
                if letter_guessed not in letters_for_game.guessed_list:
                    letters_for_game.add_guess(letter_guessed)
                    tk.Label(m, text=letters_for_game.guessed_list).grid(row=4, column=1)
                else:
                    messagebox.showinfo("Sorry!", "This letter has already been guessed, try guessing another letter!")
        else:
            raise InvalidGuess("Please only guess letters!")
    except AttributeError:
        raise InvalidGuess()


def start_game():
    """
    This function will start by creating a new instance of the game and resetting attempts remaining
    :return:
    """
    new_game = LetterGuesser()
    length_of_magic_word = len(new_game.magic_word)
    tk.Label(m, text="The word is " + str(length_of_magic_word) + " letters long!").grid(row=2)
    print(new_game.magic_word)


class InvalidGuess(Exception):
    # This custom exception gets raised if the user's guess does not meet the accepted conditions
    pass


if __name__ == '__main__':
    try:
        global letters_for_game
        letters_for_game = LetterGuesser()
        m = tk.Tk()
        m.title("Hangman")
        start_game_button = tk.Button(m, text="Start Game!", command=start_game, width=33)
        start_game_button.grid(row=1, columnspan=2)
        tk.Label(m, text="Please guess a letter:").grid(row=3, columnspan=2)
        new_guess = tk.Entry(m)
        new_guess.grid(row=4)
        guess_button = tk.Button(m, text="Guess", command=guess, width=14)
        guess_button.grid(row=4, column=1)
        tk.Label(m, text="Already guessed letters:").grid(row=5)
        tk.Label(m, text=letters_for_game.guessed_list).grid(row=5, column=1)
        exit_button = tk.Button(m, text="Exit", command=m.destroy, width=16)
        exit_button.grid(row=6, columnspan=2)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        tk.Label(m, text="Start Time: " + current_time).grid(row=7, column=1)
        m.mainloop()
    except ValueError:
        print("The program has been closed due to a ValueError!")
