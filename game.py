# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string

class Game:
    GRID_SIZE = 9

    def __init__(self):
        self.grid = self.__generate_random_grid()

    def is_valid(self, word):
        if not word:
            return False

        for letter in word:
            if letter not in self.grid:
                return False

        return True

    def __generate_random_grid(self):
        return [random.choice(string.ascii_uppercase) for _ in range(self.GRID_SIZE)]
