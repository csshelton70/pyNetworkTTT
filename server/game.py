class Game:

    _player1: str
    _player2: str
    _board: list

    def __init__(self) -> None:
        self._board = self.initialize_board()
        return

    def initialize_board(self) -> list[str]:
        """Initializes game board to default state

        Returns:
            list[str]: 9 element list for each position on the board
        """
        result = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        return result

    def xy_to_pos(self, x: int, y: int) -> int:
        """Takes in an x,y value and returns what that position would be in a list

        Args:
            x (int): x position in grid
            y (int): y position in grid

        Returns:
            int: position in list
        """
        _p: int = ((y - 1) * 3) + x - 1

        return _p
