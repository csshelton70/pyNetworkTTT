import pytest
import uuid
from server.main import add
from server.game import *
from server.player import Player


def test_add():
    """
    Sample test to make sure the pyTest system works
    """
    res = add(4, 5)
    assert res == 9
