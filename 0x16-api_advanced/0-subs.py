#!/usr/bin/python3
"""
Python script that displays number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the reddit API and returns number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome version 121.0.6167.161'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)

    try:
        results = response.json()
        return results.get('data').get('subscribers')

    except Exception:
        return 0
