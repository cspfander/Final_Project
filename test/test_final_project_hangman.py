import unittest
from project import final_project_hangman as fph


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_game = fph.LetterGuesser()

    def tearDown(self):
        del self.new_game

    def test_exception_invalid_guess(self):
        with self.assertRaises(fph.InvalidGuess):
            my_guess = 1
            self.new_game.add_guess(my_guess)

    def test_exception_valid_guess(self):
        my_guess = "a"
        expected_output = ["a"]
        self.new_game.add_guess(my_guess)
        self.assertEqual(expected_output, self.new_game.guessed_list)


if __name__ == '__main__':
    unittest.main()
