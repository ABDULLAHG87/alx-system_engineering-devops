#!/usr/bin/python3
"""
Python script that uses recursive function to query reddit

"""

from requests import get

after = None


def recurse(subreddit, hot_list=[]):
    """
    function that queries the reddit API and returns number of subscribers
    """
    global after

    user_agent = {'User-agent': 'Google Chrome version 121.0.6167.161'}
    params = {'after': after}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, params=params, allow_redirect=False)

    if response.status_code == 200:
        results = response.json()
        after_data = results.get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.get("data").get("children")
        for item in all_titles:
            hot_list.append(item.get("data").get("title"))
        return hot_list
    else:
        return None
