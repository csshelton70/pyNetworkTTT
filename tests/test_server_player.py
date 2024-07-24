import pytest
from server.player import Player

_id = "sdfsfdasfdasf"
_name = "james t kirk"


@pytest.fixture
def setup_data():
    _p = Player(_id, 1, _name)
    yield _p


def test_get_id(setup_data) -> None:
    _p = setup_data

    assert len(_p.id) > 0
    assert _p.id == _id


def test_set_id(setup_data) -> None:
    _p = setup_data

    with pytest.raises(AttributeError) as e_info:
        _p.id = "sdf"


def test_set_active_true(setup_data) -> None:
    _p = setup_data
    _p.active = True

    assert _p.active == True


def test_set_active_false(setup_data) -> None:
    _p = setup_data
    _p.active = False

    assert _p.active == False


def test_set_active_error(setup_data) -> None:
    _p = setup_data

    with pytest.raises(TypeError) as e_info:
        _p.active = "fred"


def test_set_xo(setup_data) -> None:
    _p = setup_data
    _p.xo = "x"
    _v = _p.xo
    assert _v == "x"

    _p.xo = "X"
    _v = _p.xo
    assert _v == "x"

    _p.xo = "o"
    _v = _p.xo
    assert _v == "o"

    _p.xo = "O"
    _v = _p.xo
    assert _v == "o"


def test_set_xo_error(setup_data) -> None:
    _p = setup_data
    with pytest.raises(ValueError) as e_info:
        _p.xo = "0"


def test_set_name(setup_data) -> None:
    _p = setup_data
    _p.name = "fred"
    assert _p.name == "fred"


def test_get_name(setup_data) -> None:
    _p = setup_data

    assert _p.name == _name
