from sentence_templates.negative_words.negative_words import negative_words_array


def analyze_positive_level(sentence: str, current_positive_level: int):
    for negative_word in negative_words_array():

        if negative_word in sentence:
            current_positive_level -= 5

    current_positive_level += 2

    return current_positive_level
