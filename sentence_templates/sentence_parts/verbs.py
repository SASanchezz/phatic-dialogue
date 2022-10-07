import json
import random
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'verbs.json')

verbs = json.load(open(filename))


def random_preference_verb():
    return verbs['preferences'][random.randint(0, len(verbs['preferences'])-1)]


def random_habits_verb():
    return verbs['habits'][random.randint(0, len(verbs['habits'])-1)]
