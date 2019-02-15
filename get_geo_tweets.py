"""
Get tweets of users and keep the ones that are geotagged.
"""

import twitter
import json
from time import sleep
from sys import argv

with open(argv[1], 'r') as f:
	line = f.readline()
	CONSUMER_KEY = line.strip()
	line = f.readline()
	CONSUMER_SECRET = line.strip()
	line = f.readline()
	TOKEN = line.strip()
	line = f.readline()
	TOKEN_SECRET = line.strip()
	
num = argv[2]

def get_tweets(api=None, user_id=None):
	try:
		timeline = api.GetUserTimeline(user_id=user_id, count=200, include_rts=False)
		for tweet in timeline[:5]:
			tweet_json = tweet._json
			if tweet_json['place']:
				place_type = tweet_json['place']['place_type']
				if place_type == 'poi' or \
					place_type == 'city' or \
					place_type == 'neighborhood':
					return timeline
	except:
		pass
	return None

api = twitter.Api(consumer_key=CONSUMER_KEY,
				  consumer_secret=CONSUMER_SECRET,
				  access_token_key=TOKEN,
				  access_token_secret=TOKEN_SECRET)

last = None
with open("liberal_geo" + num + ".json", 'r') as f:
	for line in f:
		line = line.strip()
		if line:
			last = line
				  
with open("unchecked_libs" + num, 'r') as f:
	queries = 0
	timelines = 0
	done = True
	for line in f:
		userid = line.strip()
		if not done:
			timeline = get_tweets(api=api, user_id=userid)
			if timeline:
				timelines += 1
				with open("liberal_geo" + num + ".json", 'a') as g:
					g.write(userid + '\n') 
				with open("liberal_tweets" + num + ".json", 'a') as g:
					g.write("User:" + userid + '\n')
					for tweet in timeline:
						tweet_json = tweet._json
						json.dump(tweet_json, g)
						g.write("\n")
				if timelines % 10 == 0:
					print("Number of timelines retrieved so far: ", timelines)
			queries += 1
			if queries > 1495:
				print("Sleeping for 15 mins")
				sleep(15*60)
				queries = 0
		else:
			if userid == last:
				print("Starting after " + last)
				done = False
				print("Sleeping for 15 minutes.")
				sleep(15*60)