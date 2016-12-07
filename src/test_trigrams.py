"""This module contains tests for our trigrams module."""


def test_trigrams():
    """Test that the two_word function returns a two-word string."""
    from trigrams import two_words
    assert two_words().count(" ") == 1


def test_pulltext():
    """Test pulling text and splitting it into a list of single words."""
    from trigrams import pulltext
    assert pulltext()[0] == "One"
