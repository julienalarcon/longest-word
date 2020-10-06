# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests

class Game:
    GRID_SIZE = 9

    def __init__(self):
        self.grid = self.__generate_random_grid()

    def is_valid(self, word):
        # Word not empty
        if not word:
            return False

        # Word in grid
        for letter in word:
            if letter not in self.grid:
                return False

        # Word exists
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        if not r.json()['found']:
            return False

        return True

    def __generate_random_grid(self):
        return [random.choice(string.ascii_uppercase) for _ in range(self.GRID_SIZE)]
