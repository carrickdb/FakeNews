#!/usr/bin/env python

"""
Get list of users who liked Breitbart's tweets.
"""

import urllib2
import re

def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib2.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids
    except urllib2.HTTPError:
        return False

# Example:
# https://twitter.com/golan/status/731770343052972032

user_id = '457984599'  # Breitbart's user id
with open('timeline.json') as f:
    with open('likers.json', 'w') as g:
        for line in f:
            # g.write(line)
            currIDs = get_user_ids_of_post_likes(int(line))
            for id in currIDs:
                if id != user_id:
                    g.write(id + '\n')
            # g.write('\n')
