import unittest
from project import final_project_hangman as fph


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # creates a new object to test
        self.new_game = fph.LetterGuesser()

    def tearDown(self):
        # deletes the created new_game object
        del self.new_game

    def test_exception_invalid_guess(self):
        # test whether or not an invalid guess will throw the custom exception InvalidGuess
        with self.assertRaises(fph.InvalidGuess):
            my_guess = 1
            self.new_game.add_guess(my_guess)

    def test_exception_valid_guess(self):
        # test to ensure that with given a valid guess that the guess is added to the guessed list
        my_guess = "a"
        expected_output = ["a"]
        self.new_game.add_guess(my_guess)
        self.assertEqual(expected_output, self.new_game.guessed_list)

    def test_magic_word_selection(self):
        # test to ensure that the word in the list is chosen correctly
        expected_output = "coil"
        self.assertEqual(self.new_game.list_of_words[0], expected_output)


if __name__ == '__main__':
    unittest.main()
