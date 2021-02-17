import sys

import pytest

from markers.two.addition import add


@pytest.mark.skip(reason="Skipping basic addition")
def test_add_num():
    assert add(1, 2) == 3


@pytest.mark.skipif(sys.version_info > (3, 7), reason="Ignore if python version is greater than 3.7")
def test_add_str():
    assert add("a", "b") == "ab"


@pytest.mark.xfail(sys.platform == "win32", reason="do not run this on win32")
def test_add_list():
    assert add([1], [2]) == [1, 2]
    raise Exception()
