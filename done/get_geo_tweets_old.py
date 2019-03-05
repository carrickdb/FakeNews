"""
Get tweets of users and keep the ones that are geotagged.
"""

import twitter
import json

CONSUMER_KEY = 'RB2uGEKWHjFHwRSGuIzZ6mItx'
CONSUMER_SECRET ='930KYZtksZ1hXeJRHa7R4eCjDUAbvz5BlumTGUSiDrr6Eu9RCK'
TOKEN = '15693746-LwtO5dxDOYOe82tGeEP7jYTDRKKuPT3e35bHvvqk5'
TOKEN_SECRET = '0XpaxHAcpQJKWCCbK37TkJA8iF5XDEBa6TeveUQPyWCNx'

def get_tweets(api=None, user_id=None):
    timeline = api.GetUserTimeline(user_id=int(user_id), count=200)
    # prinst("getting tweets before:", earliest_tweet)
	for tweet in timeline[5]:
		if tweet['place']:
			place_type = tweet['place']['place_type']
			if place_type == 'poi' or \
				place_type == 'city' or \
				place_type == 'neighborhood':
				return timeline
    return None


api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=TOKEN,
                  access_token_secret=TOKEN_SECRET)

				  
with open("JoeBiden.dat", 'r') as f:
	i = 0
	for line in f:
		userid = line.strip()
		timeline = get_tweets(api=api, user_id=userid)
		if timeline:
			with open("Biden_geo.json", 'a') as g:
				g.write(userid + '\n') 
			with open("Biden_tweets.json", 'a') as g:
				g.write("User:" + userid + '\n')
				for tweet in timeline:
					g.write(tweet._json)
					g.write("\n")
		i += 1
		if i > 1490:
			print("Sleeping for 15 mins")
			sleep(15*60)
			i = 0
