#!/usr/bin/python3
"""
Python script that uses recursive function to query reddit

"""
import json
from requests import get


def count_words(subreddit, word_list, after="", count=0):
    """
    print counts of a given words found in hot posts
    """

    user_agent = {'User-agent': 'Google Chrome version 121.0.6167.161'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, params=params,
                   allow_redirect=False)

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    for i in results.get("children"):
        title = i.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([m for m in title if m == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after_data is not None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print(f"{k}: {v}") for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
