import pytest
import string
from game import Game

@pytest.fixture
def my_game():
    g = Game()
    g.grid = list("ABCDEFGHI")
    return g

class TestGame:
    @staticmethod
    def test_game_is_well_initialized():
        new_game = Game()
        grid = new_game.grid
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    @staticmethod
    def test_valid_word(my_game):
        assert my_game.is_valid("FADE") is True

    @staticmethod
    def test_invalid_word(my_game):
        assert my_game.is_valid("BOLD") is False

    @staticmethod
    def test_empty_word(my_game):
        assert my_game.is_valid("") is False
