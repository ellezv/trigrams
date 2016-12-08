"""This module contains an implementation of a trigram algorithm."""

import io
import re
import random


def pulltext(file_path):
    """Open a text file and turn it into a list of single word strings."""
    text_file = io.open(file_path).read()
    return re.findall('\w+', text_file)


def build_tridict(file_path):
    """Enumerate through file to build 2-word keys and the value pairs."""
    tridict = {}
    text = pulltext(file_path)
    for idx, item in enumerate(text):
        try:
            key = text[idx] + " " + text[idx + 1]
            value = text[idx + 2]
            tridict.setdefault(key, []).append(value)
        except:
            break
    return tridict


def create_output(file_path, user_int):
    """Create a list of words generated with a trigram."""
    tridict = build_tridict(file_path)
    output = []
    random_key = "I was"
    output.extend(random_key.split())
    for i in range(user_int):
        try:
            new_key = ' '.join(output[-2:])
            output.append(random.choice(tridict[new_key]))
            print(new_key)
        except IndexError:
            print("no more combination")
    return " ".join(output)
