import pytest
import uuid
from server.game import *
from server.player import Player

p1 = Player(uuid.uuid4(), 1, "player1")
p2 = Player(uuid.uuid4(), 2, "player2")


@pytest.fixture
def setup_data():

    _game = Game()
    _game.assign_player_1(p1)
    _game.assign_player_2(p2)

    yield _game


def test_game_initialize_board(setup_data) -> None:
    _b = setup_data.initialize_board()

    assert len(_b) == 9

    for pos in _b:
        assert pos == "-"


def test_game_xy_to_pos(setup_data) -> None:
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


def test_game_get_board(setup_data) -> None:
    _g = setup_data
    _b = _g.board

    assert len(_b) == 9

    for pos in _b:
        assert pos == "-"


def test_game_set_active_player(setup_data) -> None:
    _g = setup_data

    _id = _g.choose_starting_player()

    assert _id == 1 or _id == 2


def test_game_set_active_player_both_responses(setup_data) -> None:
    _g = setup_data

    _p1 = 0
    _p2 = 0
    _p3 = 0

    for i in range(1, 100):
        _id = _g.choose_starting_player()
        if _id == 1:
            _p1 += 1
        elif _id == 2:
            _p2 += 1
        else:
            _p3 += 1

    assert _p1 > 0
    assert _p2 > 0
    assert _p3 == 0


def test_add_move_not_active_player(setup_data) -> None:
    _g = setup_data
    _active = _g.choose_starting_player()
    _result: list = []

    if _active == 1:
        _result = _g.add_move(2, 2, p2)
    else:
        _result = _g.add_move(2, 2, p1)

    assert _result[0] == 0
    assert _result[1] == "Not active player"


def test_add_move_invalid_position(setup_data) -> None:
    _g = setup_data
    _g.active = 1
    _g._player1.active = True
    _g._player2.active = False

    _result: list = []

    _result = _g.add_move(22, 2, p1)

    assert _result[0] == 0
    assert _result[1] == "Invalid position"


def test_add_move_location_not_empty(setup_data) -> None:
    _g = setup_data
    _g.active = 1
    _g._player1.active = True
    _g._player2.active = False
    _g._board[4] = "z"
    _result: list = []

    _result = _g.add_move(2, 2, p1)

    assert _result[0] == 0
    assert _result[1] == "Location not empty"


def test_winner_winner_horizontal_1(setup_data) -> None:
    _g = setup_data
    _b = _g.initialize_board()

    _r = [0, 1, 2]
    for i, p in enumerate(_r):
        _g._board[p] = "x"
    assert _g.winner_winner_chicken_dinner() == True


def test_winner_winner_horizontal_2(setup_data) -> None:
    _g = setup_data
    _b = _g.initialize_board()

    _r = [3, 4, 5]
    for i, p in enumerate(_r):
        _g._board[p] = "x"
    assert _g.winner_winner_chicken_dinner() == True


def test_winner_winner_horizontal_3(setup_data) -> None:
    _g = setup_data
    _b = _g.initialize_board()

    _r = [6, 7, 8]
    for i, p in enumerate(_r):
        _g._board[p] = "x"
    assert _g.winner_winner_chicken_dinner() == True


def test_winner_winner_vertical_1(setup_data) -> None:
    _g = setup_data
    _b = _g.initialize_board()

    _r = [0, 3, 6]
    for i, p in enumerate(_r):
        _g._board[p] = "x"
    assert _g.winner_winner_chicken_dinner() == True


def test_winner_winner_vertical_2(setup_data) -> None:
    _g = setup_data
    _b = _g.initialize_board()

    _r = [1, 4, 7]
    for i, p in enumerate(_r):
        _g._board[p] = "x"
    assert _g.winner_winner_chicken_dinner() == True


def test_winner_winner_vertical_3(setup_data) -> None:
    _g = setup_data
    _b = _g.initialize_board()

    _r = [2, 5, 8]
    for i, p in enumerate(_r):
        _g._board[p] = "x"
    assert _g.winner_winner_chicken_dinner() == True


def test_winner_winner_cross_1(setup_data) -> None:
    _g = setup_data
    _b = _g.initialize_board()

    _r = [0, 4, 8]
    for i, p in enumerate(_r):
        _g._board[p] = "x"
    assert _g.winner_winner_chicken_dinner() == True


def test_winner_winner_cross_2(setup_data) -> None:
    _g = setup_data
    _b = _g.initialize_board()

    _r = [2, 4, 6]
    for i, p in enumerate(_r):
        _g._board[p] = "x"
    assert _g.winner_winner_chicken_dinner() == True
