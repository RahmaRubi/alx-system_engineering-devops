#!/usr/bin/python3
"""all hottest posts"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """hottest posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom user agent'}
    params = {'after': after, 'limit': 100}  # limit to 100 posts per request
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])
    after = data.get('after', None)

    hot_list.extend([post['data']['title'] for post in posts])

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list if hot_list else None
