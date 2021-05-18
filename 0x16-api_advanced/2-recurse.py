#!/usr/bin/python3
"""query the Reddit API and
and returns a list containing the titles of
all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], before=None):
    """ get hot titles for a subreddit """
    header = {'User-Agent': 'School project'}
    pl = {'after': before}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers=header, params=pl, allow_redirects=False)
    if r.status_code == 200:
        after = r.json().get('data').get('after')
        for e in r.json().get('data').get('children'):
            hot_list.append(e.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    return None
