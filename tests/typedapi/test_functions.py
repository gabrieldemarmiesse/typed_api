import pytest

from typedapi import ensure_api_is_typed, NotTypedError


ADDITIONAL_MSG = "The evil rabbit"


def dodo(dummy_arg_1: int, dummy_arg_2) -> float:
    return 2.8


def test_ensure_api_is_typed_func_1():
    ensure_api_is_typed([dodo], [dodo], init_only=True)


def test_ensure_api_is_typed_func_2():
    with pytest.raises(NotTypedError) as excinfo:
        ensure_api_is_typed(
            [dodo], [], init_only=True, additional_message=ADDITIONAL_MSG
        )

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
        ensure_api_is_typed(
            [dudo], [], init_only=True, additional_message=ADDITIONAL_MSG
        )

    error_msg = str(excinfo.value)
    assert "return type" in error_msg
    assert ADDITIONAL_MSG in error_msg

    # ensure there is a link for a tutorial.
    assert "http" in error_msg


def gru(dummy_arg_1: int, dummy_arg_2: str) -> float:
    return 2.8


def test_ensure_api_is_typed_func_all_typed():
    ensure_api_is_typed([gru], [], init_only=True)


class Dada:
    def __init__(self, a: int):
        pass


def test_ensure_api_is_typed_class_1():
    ensure_api_is_typed([Dada], [], init_only=True)


class Dudu:
    def __init__(self, a: int, not_typed_arg=10):
        pass


def test_ensure_api_is_typed_class_2():
    with pytest.raises(NotTypedError) as excinfo:
        ensure_api_is_typed(
            [Dudu], [], init_only=True, additional_message=ADDITIONAL_MSG
        )

    error_msg = str(excinfo.value)
    assert "Dudu.__init__" in error_msg
    assert "not_typed_arg" in error_msg
    assert ADDITIONAL_MSG in error_msg

    # ensure there is a link for a tutorial.
    assert "http" in error_msg
