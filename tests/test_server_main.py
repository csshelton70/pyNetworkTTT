import pytest
from server.main import add
from server.game import *


def test_add():
    """
    Sample test to make sure the pyTest system works
    """
    res = add(4, 5)
    assert res == 9


@pytest.fixture
def setup_data():
    _game = Game()

    yield _game


def test_game_initialize_board(setup_data) -> None:
    """Test:
        the game board only contains 9 positions
        each postition is set to "-"

    Args:
        setup_data (game): The game setup in pytest.fixture
    """
    _b = setup_data.initialize_board()

    assert len(_b) == 9

    for pos in _b:
        assert pos == "-"
