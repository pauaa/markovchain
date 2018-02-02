# -*- coding: utf-8 -*-

import re

TWEET_START = '^'
TWEET_END = '$'
IGNORE_TAGS = True
TAG_REGEX = 'https?:\/\/t\.co\/\w*'


class Parser:

    def __init__(self):
        pass

    @staticmethod
    def remove_tags(sentence):
        """
        This function strips tags off from sentence and returns that.
        :param sentence: Sentence fro where the tags are removed
        :type sentence: str
        :return: sentence without tags
        """
        r = re.compile(TAG_REGEX)
        return r.sub('', sentence)

    def parse(self, text):
        """
        Given texts, forms lists of words based on their order to use in
        Markov chains of depth of 2.
        :param text: Any text that is used to teach Markov model
        :return: Lists of words based on their order
        """

        sentences = text.split('\n')

        for sentence in sentences:
            sentence = sentence.strip()

            if IGNORE_TAGS:
                sentence = self.remove_tags(sentence)

            words = [TWEET_START]
            words.extend(map(lambda w: w.lower(), sentence.split(" ")))
            words.extend([TWEET_END])
            words = filter(None, words)

            for n in range(0, len(words) - 1):
                yield words[n:n + 2]
