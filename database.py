# -*- coding: utf-8 -*-

import dataset
import operator
import random
from parser import TWEET_END


db = dataset.connect('sqlite:///:memory:')

table = db['markov']


def add(words):
    """
    Add word to database. First word of the tuple is followed by the second
    word in the tuple.
    :param words: Two words that will be added in database
    :type words: tuple
    :return:
    """
    if words[0] != "^" or words[1] != "$":
        # ignore cases where both start and end exist in same pair
        table.insert({"first": words[0], "second": words[1]})


def pick_by_weight(d):
    """Given dictionary of words as keys and their weights as values
    return random key based on their weight compared to sum of all the
    weights
    :param d: dictionary of key value pairs of words and weights
    :return based on weights randomly selected word
    """
    r = random.uniform(0, sum(d.itervalues()))
    su = 0.0
    for key, weight in d.iteritems():
        su += weight
        if r < su:
            return key
    return max(d.iteritems(), key=operator.itemgetter(1))[0]


def find(word):
    """
    Given word, return word that follows it in database.
    :param word: First word of sequence
    :type word: str
    :return:
    """

    results = table.find(first=word)
    results_count = dict()
    for r in results:
        next_word = r['second']
        if next_word in results_count.keys():
            results_count[next_word] += 1
        else:
            results_count[next_word] = 1
    if len(results_count) > 0:
        return pick_by_weight(results_count)
    return TWEET_END
