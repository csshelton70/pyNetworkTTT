import pytest
from client.main import add


def test_add():
    res = add(4, 5)
    assert res == 9
