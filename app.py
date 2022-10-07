from handler import handle
from positive_level_analyze.positive_level_analyzer import analyze_positive_level


def app():
    positive_level = 50

    while True:
        user_message = input()
        response = handle(user_message, positive_level)
        positive_level = analyze_positive_level(user_message, positive_level)

        print(response, end='\n\n')
