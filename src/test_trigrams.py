"""This module contains tests for our trigrams module."""


import pytest

DICT_TABLE = [
    ["One night--it", "was"],
    ["night--it was", "on"],
    ["was on", "the"],
]


def test_pulltext():
    """Test pulling text and splitting it into a list of single words."""
    from trigrams import pulltext
    assert pulltext()[0] == "One"


@pytest.mark.parametrize("key, value", DICT_TABLE)
def test_build_tridict(key, value):
    """Test build_tridict function to build dictionary."""
    from trigrams import build_tridict
    assert build_tridict()[key] == value
