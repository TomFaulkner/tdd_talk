import pytest_tdd as pyt


# without items
def test_append_to_list_no_items():
    assert pyt.append_to_list(5) == [5]


def test_append_to_list_no_items_again():
    assert pyt.append_to_list(5) == [5]


def test_append_to_list_no_items_returns_list():
    assert isinstance(pyt.append_to_list(5), list)


# with items
def test_append_to_list_with_items():
    assert pyt.append_to_list(5, []) == [5]


def test_append_to_list_with_items_again():
    assert pyt.append_to_list(5, []) == [5]


def test_append_to_list_with_populated_items():
    assert pyt.append_to_list(5, [1]) == [1, 5]


def test_append_to_list_wo_items_returns_list():
    assert isinstance(pyt.append_to_list(5, [1]), list)
