#!/usr/bin/python3
"""query the Reddit API and
and returns a list containing the titles of
all hot articles for a given subreddit
"""
import requests


def count_words(subreddit, word_list, result={}, before=None):
    """ get hot titles for a subreddit """
    header = {'User-Agent': 'School project'}
    pl = {'after': before}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers=header, params=pl, allow_redirects=False)

    if result == {}:
        for word in word_list:
            word = word.lower()
            result[word] = 0

    if r.status_code == 200:
        after = r.json().get('data').get('after')
        for e in r.json().get('data').get('children'):
            buf = e.get('data').get('title').lower().split()
            for w in word_list:
                w = w.lower()
                if (buf.count(w) > 0):
                    result[w] += buf.count(w)

        if after is not None:
            count_words(subreddit, word_list, result, after)
        else:
                s = sorted(result.items(), key=lambda x: x[1], reverse=True)
                for k in s:
                    if k[1] != 0:
                        print('{}: {}'.format(k[0], k[1]))
