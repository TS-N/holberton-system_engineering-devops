#!/usr/bin/python3
"""query the Reddit API and returns the number of subscribers
for a given subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    """ get nb of subscribers for a subreddit """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json().get('data').get('subscribers'))
    return (0)
