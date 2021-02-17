import pytest

from raises.one.age_validation import validate_age


def test_validate_age_valid_age():
    validate_age(4)


def test_validate_age_invalid_age():
    # when exception is expected, it can be caught here before it is thrown
    with pytest.raises(ValueError) as exc_info:
        validate_age(-2)
    assert (str(exc_info.value)) == "Age cannot be less than 0"


def test_validate_age_one_invalid_age():
    # when exception is expected, it can be matched for specific exception
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)
