"""
Program: final_project_hangman.py
Author: Colten pfander
Date last modified: 11/26/19


The purpose of this program is to make a GUI that will allow the user to play the game Hangman.
"""
import random
import tkinter as tk
from tkinter import messagebox


class LetterGuesser:
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

    def add_guess(self, a_guess):
        self.guessed_list.append(a_guess)


def guess():
    guessed_letters.append(new_guess.get())
    pass


def start_game():
    """
    This function will contain a list of words that will be randomly selected to be the magic word to guess
    :return:
    """
    global letters_for_game
    letters_for_game = LetterGuesser()


class InvalidGuess(Exception):
    # This custom exception gets raised if the user's guess does not meet the accepted conditions
    pass


if __name__ == '__main__':
    m = tk.Tk()
    m.title("Hangman")
    guessed_letters = []
    start_game_button = tk.Button(m, text="Start Game!", command=start_game, width=33)
    start_game_button.grid(row=1, columnspan=2)
    tk.Label(m, text="Please guess a letter:").grid(row=2)
    new_guess = tk.Entry(m)
    new_guess.grid(row=2, column=1)
    tk.Label(m, text="Already guessed letters:").grid(row=3)
    tk.Label(m, text=guessed_letters).grid(row=3, column=1)
    exit_button = tk.Button(m, text="Exit", command=m.destroy, width=16)
    exit_button.grid(row=4, columnspan=2)
    m.mainloop()
