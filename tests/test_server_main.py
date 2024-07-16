import pytest
from server.main import add


def test_add():
    """
    Sample test to make sure the pyTest system works
    """
    res = add(4, 5)
    assert res == 9
