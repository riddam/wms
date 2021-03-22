import pytest
from . import validators


@pytest.mark.parametrize("test_input, expected", [("2", 2), ("3", 3)])
def test_validate_int(test_input, expected):
    """
    postive test case for integer validator
    :param test_input: test data
    :param expected:  expected behaviour
    :return:
    """
    assert validators.validate_int(test_input) == expected


def test_negative_validate_int():
    """
    Negative test case for int validator
    :return:
    """
    assert validators.validate_int('string') is None


@pytest.mark.parametrize("test_input, expected", [("2.5", 2.5), ("3.6", 3.6)])
def test_validate_float(test_input, expected):
    """
    postive test case for float validator
    :param test_input: test data
    :param expected:  expected behaviour
    :return:
    """
    assert validators.validate_float(test_input) == expected


def test_negative_validate_float():
    """
    Negative test case for float validator
    :return:
    """
    assert validators.validate_float('string') is None
