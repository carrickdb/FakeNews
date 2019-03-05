#!/usr/bin/env python3

"""
Get ids of tweets
"""

import twitter
import json

CONSUMER_KEY = 'RB2uGEKWHjFHwRSGuIzZ6mItx'
CONSUMER_SECRET ='930KYZtksZ1hXeJRHa7R4eCjDUAbvz5BlumTGUSiDrr6Eu9RCK'
TOKEN = '15693746-LwtO5dxDOYOe82tGeEP7jYTDRKKuPT3e35bHvvqk5'
TOKEN_SECRET = '0XpaxHAcpQJKWCCbK37TkJA8iF5XDEBa6TeveUQPyWCNx'

def get_tweets(api=None, screen_name=None):
	with open("Biden_followers.dat", 'w') as f:
		next_cursor, previous_cursor, followers = api.GetFollowerIDsPaged(screen_name=screen_name, count=50)
		for follower in followers:
			print(follower)
			assert False		
    # print("getting tweets before:", earliest_tweet)

    while False:
        followers = api.GetFollowerIDs(
            screen_name=screen_name, count=5000
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            print("getting tweets before:", earliest_tweet)
            timeline += tweets



api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=TOKEN,
                  access_token_secret=TOKEN_SECRET)

screen_name = "JoeBiden"
timeline = get_tweets(api=api, screen_name=screen_name)


