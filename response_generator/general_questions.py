import json
from sentence_templates.sentence_parts.verbs import random_preference_verb
from sentence_templates.sentence_parts.nouns import random_general_noun
from sentence_templates.sentence_parts.adjectives import random_positive_adjective, random_neutral_adjective
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, '../question_templates/general.json')

default_answer = 'default_answer'


def handle_question(sentence: str, positive_level: int):
    file = open(filename)
    template = json.load(file)

    for key, value in template.items():
        if key in sentence.casefold():
            if positive_level < 50:
                return template[key][default_answer]

    return generate_random_answer(positive_level)


def generate_random_answer(positive_level: int):
    if positive_level > 100:
        return f'I {random_preference_verb()} your {random_positive_adjective()} {random_general_noun()}'
    else:
        return f'I {random_preference_verb()} my {random_neutral_adjective()} {random_general_noun()}'
