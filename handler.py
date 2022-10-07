from response_generator.response_generator import questions
from sentence_templates.simple.simple import get_greeting_response, get_bye_response

NOT_FOUND_RESPONSE = 'Excuse me, I don\'t understand you'


def handle(sentence: str, positive_level: int):
    greeting = get_greeting_response(sentence)
    if greeting is not None:
        return greeting

    bye = get_bye_response(sentence)
    if bye is not None:
        exit()
        return bye

    return questions(sentence, positive_level)
