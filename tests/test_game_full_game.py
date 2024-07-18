import pytest
import uuid
from server.main import add
from server.game import *
from server.player import Player

p1 = Player("ASdfasdf", "player1")
p2 = Player("edfvw4", "player2")


@pytest.fixture
def setup_data():

    _game = Game(p1, p2)

    yield _game


def test_full_game(setup_data) -> None:
    _g = setup_data
    _g._player1.xo = "x"
    _g._player2.xo = "o"

    _g._active = 1
    _g._player1._active = True
    _g._player2._active = False
    _r = _g.add_move(2, 2, p1)
    assert _r == (1, ["-", "-", "-", "-", "x", "-", "-", "-", "-"])

    _g._active = 2
    _g._player1._active = False
    _g._player2._active = True
    _r = _g.add_move(2, 1, p2)
    assert _r == (1, ["-", "o", "-", "-", "x", "-", "-", "-", "-"])

    _g._active = 1
    _g._player1._active = True
    _g._player2._active = False
    _r = _g.add_move(1, 1, p1)
    assert _r == (1, ["x", "o", "-", "-", "x", "-", "-", "-", "-"])

    _g._active = 2
    _g._player1._active = False
    _g._player2._active = True
    _r = _g.add_move(3, 3, p2)
    assert _r == (1, ["x", "o", "-", "-", "x", "-", "-", "-", "o"])

    _g._active = 1
    _g._player1._active = True
    _g._player2._active = False
    _r = _g.add_move(1, 3, p1)
    assert _r == (1, ["x", "o", "-", "-", "x", "-", "x", "-", "o"])

    _g._active = 2
    _g._player1._active = False
    _g._player2._active = True
    _r = _g.add_move(1, 2, p2)
    assert _r == (1, ["x", "o", "-", "o", "x", "-", "x", "-", "o"])

    _g._active = 1
    _g._player1._active = True
    _g._player2._active = False
    _r = _g.add_move(3, 1, p1)
    assert _r == (2, ["x", "o", "x", "o", "x", "-", "x", "-", "o"], 1)
