import json
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'negative_words.json')

negative_words = json.load(open(filename))



def negative_words_array():
    return negative_words['negative_words']
