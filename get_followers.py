
"""
Get ids of tweets
"""

import twitter
import json
from datetime import datetime
from time import sleep

CONSUMER_KEY = ''
CONSUMER_SECRET =''
TOKEN = ''
TOKEN_SECRET = ''

def get_tweets(api=None, screen_name=None, next_cursor=None):
	queries = 0
	num_followers = 0
	# print("Sleeping for 15 mins")
	# sleep(15*60)
	if not next_cursor:
		with open(screen_name + ".dat", 'a') as f:
			next_cursor, previous_cursor, followers = api.GetFollowerIDsPaged(screen_name=screen_name, count=5000)
			for follower in followers:
				f.write(str(follower) + "\n")

			print("next_cursor:", next_cursor)
		num_followers = len(followers)
		print(num_followers, "followers downloaded")
		queries = 1

	while True:
		with open(screen_name + ".dat", 'a') as f:
			with open(screen_name + "_cursors.txt", "a") as g:
				next_cursor, previous_cursor, followers = api.GetFollowerIDsPaged(
					screen_name=screen_name, count=5000, cursor=next_cursor
				)
				print("next_cursor:", next_cursor)
				if next_cursor:
					g.write(str(next_cursor) + "\n")
				if not followers:
					break
				else:
					queries += 1
					num_followers += len(followers)
					for follower in followers:
						f.write(str(follower) + "\n")
					print(num_followers, "followers downloaded")
				if queries > 14:
					print("Sleeping for 15 mins")
					sleep(15*60)
					queries = 0
	print("Total followers:", num_followers)


api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=TOKEN,
                  access_token_secret=TOKEN_SECRET)

screen_name = "RealBenCarson"
timeline = get_tweets(api=api, screen_name=screen_name, next_cursor=None)
