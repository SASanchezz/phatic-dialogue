import random
import json
import os

here = os.path.dirname(os.path.abspath(__file__))
greeting_file = os.path.join(here, 'greetings.json')
bye_file = os.path.join(here, 'bye.json')


def get_greeting_response(sentence: str):
    for key, value in greetings().items():
        if key in sentence.split(' '):
            return value[random.randint(0, len(value)-1)]
    return None


def get_bye_response(sentence: str):
    for key, value in bye().items():
        if key in sentence.split(' '):
            return value[random.randint(0, len(value) - 1)]
    return None


def greetings():
    file = open(greeting_file)
    return json.load(file)


def bye():
    file = open(bye_file)
    return json.load(file)

