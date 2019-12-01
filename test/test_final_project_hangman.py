import unittest
from project import final_project_hangman as fph


class MyTestCase(unittest.TestCase):
    def test_custom_exception_invalid_guess(self):
        with self.assertRaises(fph.InvalidGuess):
            my_guess = 1
            fph.guess(my_guess)


if __name__ == '__main__':
    unittest.main()
