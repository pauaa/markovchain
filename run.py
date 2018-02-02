# -*- coding: utf-8 -*-

import sys
from markov import generate


if __name__ == '__main__':

    args = sys.argv
    twitter_names = args[1:]

    if len(twitter_names) == 0:
        print "Usage: python run.py twitter_name1 twitter_name2"
        print "List as many Twitter names as you wish."

    print generate(twitter_names)
