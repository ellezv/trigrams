"""This module contains tests for our trigrams module."""


import pytest

DICT_TABLE = [
    ["One night--it", ["was"]],
    ["night--it was", ["on"]],
    ["was on", ["the"]],
]

OUTPUT_LIST = ["up to the chamber which had formerly been in part my own"]


def test_pulltext():
    """Test pulling text and splitting it into a list of single words."""
    from trigrams import pulltext
    assert pulltext()[0] == "One"


@pytest.mark.parametrize("key, value", DICT_TABLE)
def test_build_tridict(key, value):
    """Test build_tridict function to build dictionary."""
    from trigrams import build_tridict
    assert build_tridict()[key] == value


def test_create_output():
    """Test create_output function which builds text off last 2 words in output file."""
    from trigrams import create_output
    assert create_output(10) == OUTPUT_LIST
