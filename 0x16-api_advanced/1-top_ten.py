#!/usr/bin/python3
"""query the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ get 10 titles for a subreddit """
    header = {'User-Agent': 'School project'}
    pl = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers=header, params=pl, allow_redirects=False)
    if r.status_code == 200:
        l = r.json().get('data').get('children')
        for e in l:
            print(e.get('data').get('title'))
    else:
        print(None)
