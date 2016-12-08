"""This module contains an implementation of a trigram algorithm."""

import io


def pulltext():
    """Open a text file and turn it into a list of single word strings."""
    return io.open("../sample.txt").read().split()
