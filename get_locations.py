#!/usr/bin/env python3.7

"""
Get the locations, if any, of users.

"""

# make sure it's not a RT

import twitter
import json

CONSUMER_KEY = 'IghI8fP7qGo8wzPukFqtC0WQC'
CONSUMER_SECRET ='MlxWDaUXy00GLoW6w9ipczfD8Y4veP1qKujJ7Cfp8d39e6AzWr'
TOKEN = '15693746-HHDMz6E4o6epMTC9qWwo9aAipDGsZZYz3QHLH3w9U'
TOKEN_SECRET = 'z5KeM6diAVuxKMpX4wFHxt1e2MHJIooHKYsVvRZHG81k4'

def get_tweets(api=None, user_id=None):
    timeline = api.GetUserTimeline(user_id=user_id, count=200)
    return timeline


api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=TOKEN,
                  access_token_secret=TOKEN_SECRET)

likers = set()

locations = {}

with open('likers.json', 'r') as f:
    for line in f:
        liker = line.strip()
        if liker not in likers:
            """
            see if this person provides their location (['user']['location'])
            get this person's original (non-RT) tweets
            see if there's any location data associated with the tweet
                utc_offset
                time_zone
                geo
                geo_enabled
                coordinates
                place
            """
            likers.add(liker)
            liker_data = {'location': None, 'geo': None, 'geo_enabled': None, \
                          'coordinates': None, 'place': None, 'utc_offset': None, \
                          'time_zone': None}
            profile_location = None
            timeline = get_tweets(api=api, user_id=liker)
            use = False
            for tweet in timeline:
                if tweet.geo:
                    print("tweet.geo", tweet.geo)
                if tweet.coordinates:
                    print("tweet.coordinates", tweet.coordinates)
                if tweet.place and tweet.place['type'] =='point':
                    # if data[0]:
                    #     print(data[0])
                    print(tweet.place)
                    break
