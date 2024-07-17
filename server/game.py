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
