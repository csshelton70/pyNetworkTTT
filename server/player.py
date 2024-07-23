class Player:
    _id: str
    _name: str
    _xo: str
    _number: int

    def __init__(self, id, number, name):
        self._active = False
        self._id = id
        self._name = name
        self._number = number

        return

    # region property:id

    @property
    def id(self) -> str:
        return self._id

    # endregion

    # region property:id

    @property
    def number(self) -> int:
        return self._number

    # endregion

    # region property:active
    _active: bool

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, flag: bool) -> None:
        if type(flag) != bool:
            raise TypeError("Invalid value used for player.active")
        self._active = flag
        return

    # endregion

    # region property:xo

    @property
    def xo(self) -> str:
        return self._xo

    @xo.setter
    def xo(self, val: str) -> None:
        val = val.lower()

        if val != "x" and val != "o":
            raise ValueError("Invalid value used for player.xo")

        self._xo = val

        return

    # endregion

    # region property:name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str) -> None:
        print(f"Player {self._number}'s name is now {val}")
        self._name = val
        return

    # endregion
