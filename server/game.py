from random import randint
from .player import Player


class Game:

    _player1: Player
    _player2: Player
    _board: list
    _active: int

    def __init__(self, p1: Player, p2: Player) -> None:
        self._player1 = p1
        self._player2 = p2
        self._board = self.initialize_board()
        return

    def initialize_board(self) -> list[str]:
        result = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        return result

    def xy_to_pos(self, x: int, y: int) -> int:
        _p: int = ((y - 1) * 3) + x - 1

        return _p

    @property
    def board(self) -> list:
        result = self._board
        return result

    def add_move(self, x: int, y: int, p: Player) -> tuple:
        if p.active == False:
            return 0, "Not active player"

        _pos = self.xy_to_pos(x, y)

        if _pos < 0 or _pos > 8:
            return 0, "Invalid position"

        if self._board[_pos] != "-":
            return 0, "Location not empty"

        self._board[_pos] = p.xo

        if self.winner_winner_chicken_dinner() == True:
            return 2, self.board, self._active

        return 1, self.board

    def choose_starting_player(self) -> int:
        _r = randint(1, 2)
        if _r == 1:
            self._player1.active = True
            self._player2.active = False
            self._active = 1
        else:
            self._player1.active = False
            self._player2.active = True
            self._active = 2
        return _r

    def winner_winner_chicken_dinner(self) -> bool:
        # Horizontal
        if self._board[0] != "-":
            # horizontal 1
            if self._board[0] == self._board[1] == self._board[2]:
                return True
            # vertical 1
            if self._board[0] == self._board[3] == self._board[6]:
                return True
            # cross 1
            if self._board[0] == self._board[4] == self._board[8]:
                return True

        if self._board[6] != "-":
            # horizontal 3
            if self._board[6] == self._board[7] == self._board[8]:
                return True
            # cross 2
            if self._board[2] == self._board[4] and self._board[4] == self._board[6]:
                return True
        elif self._board[5] != "-":
            # horizontal 2
            if self._board[3] == self._board[4] == self._board[5]:
                return True
            # vertical 3
            if self._board[2] == self._board[5] == self._board[8]:
                return True
        elif self._board[1] != "-":
            # Vertical 2
            if self._board[1] == self._board[4] == self._board[7]:
                return True

        return False
