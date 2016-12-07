"""This module contains an implementation of a trigram algorithm."""

import io


def two_words():
    """Take a list and return a string of the first two indices."""
    return str(BOOK_LIST[0:2])


def pulltext():
    text = io.open("../sample.txt")
