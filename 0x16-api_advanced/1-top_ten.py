#!/usr/bin/python3
"""
Python script that displays number of subscribers for a given subreddit
first 10 posts of the given reddit
"""

from request import get


def top_ten(subreddit):
    """
    function that queries the reddit API and returns number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent - {'User-agent': 'Google Chrome version 121.0.6167.161'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for item in my_data:
            print(item.get('data').get('title'))

    except Exception:
        print("None")
