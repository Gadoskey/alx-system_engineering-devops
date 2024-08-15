#!/usr/bin/python3
"""Contains recurse function"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns 
    a list of titles of all hot articles for a given subreddit. 
    If the subreddit is invalid, it returns None.
    
    Args:
    subreddit (str): The name of the subreddit.
    hot_list (list): The list of hot articles' titles, accumulated recursively.
    after (str): The pagination token for the next page of results.
    
    Returns:
    list: The list of hot articles' titles, or None if the subreddit is invalid.
    """
    # Set the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 \
      (by /u/firdaus_cartoon_jr)'}
    
    # Set the query parameters (limit is optional, 'after' handles pagination)
    params = {'limit': 100, 'after': after}
    
    try:
        # Make the request without following redirects
        response = requests.get(url, headers=headers, \
          params=params, allow_redirects=False, timeout=10)
        
        # Check if the response is OK
        if response.status_code != 200:
            return None
        
        # Parse the response as JSON
        data = response.json().get('data', {})
        
        # Get the list of articles
        children = data.get('children', [])
        
        # Add the titles to hot_list
        for article in children:
            hot_list.append(article['data']['title'])
        
        # Check if there is another page
        after = data.get('after', None)
        
        # If there's a next page, recurse; otherwise, return the list
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except requests.RequestException as e:
        # In case of a request failure or invalid subreddit, return None
        return None
