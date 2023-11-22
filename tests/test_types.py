"""
Types tests
"""
import pytest

from tests.utils import setup_confstar_default


@pytest.mark.skip(reason="All fields must fail")
def test_types_fail():
    Config = setup_confstar_default()

    # Will throw an error
    Config.PUBLIC_RANGE_FIELD = 6
    Config.PRIVATE_INT_FIELD = 321
    Config.PUBLIC_MIN_FIELD = [1, 2, 3, 4]
    Config.PUBLIC_MAX_FIELD.extend([4, 5, 6])

    assert Config.PUBLIC_RANGE_FIELD == 6
    assert Config.PRIVATE_INT_FIELD == 321
    assert Config.PUBLIC_MIN_FIELD == [1, 2, 3, 4]
    assert Config.PUBLIC_MAX_FIELD == [4, 5, 6]
