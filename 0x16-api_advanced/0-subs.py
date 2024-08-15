#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the num of subscribers of a given subreddit
    Args: subreddit (str): The name of the subreddit.
    Returns: int: The number of subscribers, or 0 if the subreddit is invalid
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {'User-Agent': '0x16-api_advanced: \
            project: v1.0.0 (by /u/firdaus_cartoon_jr)'}
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers=headers).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
