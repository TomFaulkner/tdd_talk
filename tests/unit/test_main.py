import pytest

import pytest_tdd as pyt


def test_func_a():
    assert pyt.return_same(1) == 1


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert pyt.is_palindrome(maybe_palindrome) == expected_result
