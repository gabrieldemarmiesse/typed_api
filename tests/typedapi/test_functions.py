import pytest

from typedapi.functions import API, NotTypedError


ADDITIONAL_MSG = "The evil rabbit"


def dodo(dummy_arg_1: int, dummy_arg_2) -> float:
    return 2.8


def test_ensure_api_is_typed_func_1():
    api = API([], [dodo], '')
    api.check_api_of_object(dodo)


def test_ensure_api_is_typed_func_2():
    with pytest.raises(NotTypedError) as excinfo:
        api = API([], [], additional_message=ADDITIONAL_MSG)
        api.check_api_of_object(dodo)

    error_msg = str(excinfo.value)
    assert "dodo" in error_msg
    assert "dummy_arg_2" in error_msg
    assert ADDITIONAL_MSG in error_msg

    # ensure there is a link for a tutorial.
    assert "http" in error_msg


def dudo(dummy_arg_1: int, dummy_arg_2: str):
    return 2.8


def test_ensure_api_is_typed_func_3():
    with pytest.raises(NotTypedError) as excinfo:
        api = API([], [], additional_message=ADDITIONAL_MSG)
        api.check_api_of_object(dudo)
    error_msg = str(excinfo.value)
    assert "return type" in error_msg
    assert ADDITIONAL_MSG in error_msg

    # ensure there is a link for a tutorial.
    assert "http" in error_msg


def gru(dummy_arg_1: int, dummy_arg_2: str) -> float:
    return 2.8


def test_ensure_api_is_typed_func_all_typed():
    api = API([], [], '')
    api.check_api_of_object(gru)

class Dada:
    def __init__(self, a: int):
        pass


def test_ensure_api_is_typed_class_1():
    api = API([], [], "")
    api.check_api_of_object(Dada)


class Dudu:
    def __init__(self, a: int, not_typed_arg=10):
        pass


def test_ensure_api_is_typed_class_2():
    with pytest.raises(NotTypedError) as excinfo:
        api = API([], [], ADDITIONAL_MSG)
        api.check_api_of_object(Dudu)

    error_msg = str(excinfo.value)
    assert "Dudu.__init__" in error_msg
    assert "not_typed_arg" in error_msg
    assert ADDITIONAL_MSG in error_msg

    # ensure there is a link for a tutorial.
    assert "http" in error_msg
