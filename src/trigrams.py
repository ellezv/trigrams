"""This module contains an implementation of a trigram algorithm."""
import io
import re
import random
import sys


def pulltext(file_path):
    """Open a text file and turn it into a list of single word strings."""
    text_file = io.open(file_path).read()
    return re.findall("[A-Za-z0-9 .,!?/$]*", text_file)


def build_tridict(file_path):
    """Enumerate through file to build 2-word keys and the value pairs."""
    tridict = {}
    text = pulltext(file_path)
    for idx, item in enumerate(text):
        try:
            key = text[idx] + " " + text[idx + 1]
            value = text[idx + 2]
            tridict.setdefault(key, []).append(value)
        except IndexError:
            break
    generate_key_list(tridict)
    return tridict


def generate_key_list(tridict):
    """Generate a key list."""
    return [key for key in tridict]


def generate_random_key(tridict):
    """Generate a random key."""
    random_key = random.choice(generate_key_list(tridict))
    return random_key


def create_output(file_path, user_int):
    """Create a list of words generated with a trigram."""
    tridict = build_tridict(file_path)
    output = []
    output.extend(generate_random_key(tridict).split())
    while len(output) < user_int:
        try:
            new_key = ' '.join(output[-2:])
            output.append(random.choice(tridict[new_key]))
        except KeyError:
            new_key = generate_random_key(tridict)
            output.extend(new_key.split())
    print(" ".join(output))


if __name__ == '__main__':
    create_output(sys.argv[1], int(sys.argv[2]))
