"""This module contains an implementation of a trigram algorithm."""

import io
import re


def pulltext():
    """Open a text file and turn it into a list of single word strings."""
    text_file = io.open("../sample.txt").read()
    return re.findall('\w+', text_file)


def build_tridict():
    """Enumerate through file to build 2-word keys and the value pairs."""
    tridict = {}
    text = pulltext()
    for idx, item in enumerate(text):
        try:
            tridict.setdefault(text[idx] + " " + text[idx + 1], []).append(text[idx + 2])
        except:
            break
    return tridict
