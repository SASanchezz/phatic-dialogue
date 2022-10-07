import json
import random
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'nouns.json')

nouns = json.load(open(filename))


def random_general_noun():
    return nouns['general'][random.randint(0, len(nouns['general'])-1)]
