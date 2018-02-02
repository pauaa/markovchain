# -*- coding: utf-8 -*-

from parser import Parser
from twitter_parser import get_statuses
import database

MAX_LENGTH = 300


def generate(twitter_names):
    text = ""
    for name in twitter_names:
        text += get_statuses(name)

    parser = Parser()
    results = parser.parse(text)
    for words in results:
        # add to database
        database.add(words)

    sentence = ['^']
    while True:
        if len(' '.join(sentence)) > MAX_LENGTH:
            break
        last_word = sentence[-1]
        word = database.find(last_word)
        if word == '$':
            break
        sentence.append(word)
    # generate sentence
    return ' '.join(sentence[1:])
