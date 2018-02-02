# -*- coding: utf-8 -*-
import sys
import operator
import requests
import json
import twitter

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_SECRET = ''


TWEET_AMOUNT = 300
LANGUAGE = 'fi'
TWEET_START = '^'
TWEET_END = '§'


def get_statuses(name):
    twitter_api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                              consumer_secret=TWITTER_CONSUMER_SECRET,
                              access_token_key=TWITTER_ACCESS_TOKEN,
                              access_token_secret=TWITTER_ACCESS_SECRET)

    statuses = twitter_api.GetUserTimeline(screen_name=name,
                                           count=TWEET_AMOUNT,
                                           include_rts=False)
    text = ""
    for status in statuses:
        if status.lang == LANGUAGE:
            status = unicode(status.text)
            text += status + '\n'
    return text
