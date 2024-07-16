import pytest
from server.main import add


# def test_add():
# res = main.add(4,5)
# assert(res==9)


def test_add():
    res = add(4, 5)
    assert res == 9
