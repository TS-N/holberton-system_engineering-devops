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
            if word in result:
                result[word]['multiplier'] += 1
            else:
                result[word] = {'count': 0, 'multiplier': 1}

    if r.status_code == 200:
        after = r.json().get('data').get('after')
        for e in r.json().get('data').get('children'):
            buf = e.get('data').get('title').lower().split()
            for k in result.keys():
                if (buf.count(k) > 0):
                    result[k]['count'] = result[k]['count'] + buf.count(k)

        if after is not None:
            count_words(subreddit, word_list, result, after)
        else:
                for k in sorted(result, key=result.get('count')):
                    if result[k]['count'] != 0:
                        nb = result[k]['count'] * result[k]['multiplier']
                        print('{}: {}'.format(k, nb))
