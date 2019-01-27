#!/usr/bin/env python3.7

"""
Get ids of tweets
"""

import twitter
import json

CONSUMER_KEY = 'IghI8fP7qGo8wzPukFqtC0WQC'
CONSUMER_SECRET ='MlxWDaUXy00GLoW6w9ipczfD8Y4veP1qKujJ7Cfp8d39e6AzWr'
TOKEN = '15693746-HHDMz6E4o6epMTC9qWwo9aAipDGsZZYz3QHLH3w9U'
TOKEN_SECRET = 'z5KeM6diAVuxKMpX4wFHxt1e2MHJIooHKYsVvRZHG81k4'

def get_tweets(api=None, screen_name=None):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=1)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    # prinst("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            print("getting tweets before:", earliest_tweet)
            timeline += tweets

    return timeline


api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=TOKEN,
                  access_token_secret=TOKEN_SECRET)

screen_name = "BreitbartNews"
timeline = get_tweets(api=api, screen_name=screen_name)

with open('timeline.json', 'w+') as f:
    for tweet in timeline:
        f.write(str(tweet._json['id']))
        f.write('\n')
