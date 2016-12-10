"""This module contains tests for our trigrams module."""


import pytest

DICT_TABLE = [
    ["../sample.txt", "One night", ["it"]],
    ["../sample.txt", "night it", ["was"]],
    ["../sample.txt", "on the", ["twentieth"]],
]

KEY_TABLE = [
    [{"a": 1, "b": 2, "c": 3}, ["a", "b", "c"]],
    [{"apple": "banana", "window": True, "hello goodbye": "false"}, ["apple", "window", "hello goodbye"]],
    [{"z": 0}, ["z"]],
]

OUTPUT_LIST = "up to the chamber which had formerly been in part my own"

LST_TABLE = [
    [{"does": 1, "my": 2, "test": 3, "work?": 4}, ["does", "my", "test", "work?"]],
    [{"g": 1, "d": 2, "v": 3, "w": 4, "e": 5, "r": 6, "t": 7}, ["g", "d", "v", "w", "e", "r", "t"]],
    [{"some words": 3, "some other words": 0, "other words": 1, "a": 2, "b": 4, "c": 5, "v": 5}, ["some words", "some other words", "other words", "a", "b", "c", "v"]],
    [{"All done": "yay"}, ["All done"]]
]


def test_pulltext():
    """Test pulling text and splitting it into a list of single words."""
    from trigrams import pulltext
    assert pulltext("../sample.txt")[0] == "One"


@pytest.mark.parametrize("file_path, key, value", DICT_TABLE)
def test_build_tridict(file_path, key, value):
    """Test build_tridict function to build dictionary."""
    from trigrams import build_tridict
    assert build_tridict(file_path)[key] == value


@pytest.mark.parametrize("dict, lst", KEY_TABLE)
def test_generate_key_list(dict, lst):
    """Test our key list generator."""
    from trigrams import generate_key_list
    assert sorted(generate_key_list(dict)) == sorted(lst)


@pytest.mark.parametrize("dic, lst", LST_TABLE)
def test_generate_random_key(dic, lst):
    """Test our generate_random_key_function."""
    from trigrams import generate_random_key
    assert generate_random_key(dic) in lst
