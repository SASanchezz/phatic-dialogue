import json
import random
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'adjectives.json')

adjectives = json.load(open(filename))


def random_positive_adjective():
    return adjectives['positive'][random.randint(0, len(adjectives['positive'])-1)]


def random_neutral_adjective():
    return adjectives['neutral'][random.randint(0, len(adjectives['neutral'])-1)]


def random_negative_adjective():
    return adjectives['negative'][random.randint(0, len(adjectives['negative'])-1)]
