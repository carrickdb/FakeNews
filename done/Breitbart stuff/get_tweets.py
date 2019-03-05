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
    timeline = api.GetUserTimeline(screen_name=screen_name, count=1)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    # prinst("getting tweets before:", earliest_tweet)

    while False:
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
        print(tweet._json)
        assert False
        f.write('\n')
