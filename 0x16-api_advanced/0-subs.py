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
    # Set the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditApp/0.1'}

    try:
        # Make the request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers from the API response
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0

    except requests.RequestException:
        return 0
        # In case of a request failure, return 0
