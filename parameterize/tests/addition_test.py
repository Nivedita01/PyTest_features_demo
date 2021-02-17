import sys

import pytest

from markers.two.addition import add


@pytest.mark.parametrize("a, b, c",
                         [(1, 2, 3),
                          ("a", "b", "ab"),
                          ([1, 2], [3], [1, 2, 3])],
                         ids=["num", "str", "list"])
def test_add(a, b, c):
    assert add(a, b) == c