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


def test_game_xy_to_pos(setup_data) -> None:
    """Tests the xy_to_pos function to make sure it returns a valid value from 0-8

    Args:
        setup_data (game): The game setup in pytest.fixture
    """
    _g = setup_data

    assert _g.xy_to_pos(1, 1) == 0
    assert _g.xy_to_pos(2, 1) == 1
    assert _g.xy_to_pos(3, 1) == 2
    assert _g.xy_to_pos(1, 2) == 3
    assert _g.xy_to_pos(2, 2) == 4
    assert _g.xy_to_pos(3, 2) == 5
    assert _g.xy_to_pos(1, 3) == 6
    assert _g.xy_to_pos(2, 3) == 7
    assert _g.xy_to_pos(3, 3) == 8
