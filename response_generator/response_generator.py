import json
from response_generator.general_questions import handle_question
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, '../sentence_templates/simple/greetings.json')


def simple_responses():
    file = open(filename)
    return json.load(file)


def questions(sentence: str, positive_level: int):
    return handle_question(sentence, positive_level)
