#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    Args:
    subreddit (str): The name of the subreddit.
    """
    # Set the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 \
      (by /u/firdaus_cartoon_jr)'}
    
    try:
        # Make the request without following redirects
        response = requests.get(
                url, headers=headers, allow_redirects=False, timeout=10)
        
        # Check if the response is OK
        if response.status_code == 200:
            # Parse the response as JSON
            data = response.json().get('data', {})
            
            # Get the list of articles
            children = data.get('children', [])
            
            # Print the titles of the first 10 hot posts
            for i, article in enumerate(children[:10]):
                print(f"{i + 1}. {article['data']['title']}")
        else:
            # If the subreddit is invalid, print None
            print(None)
    except requests.RequestException:
        # In case of a request failure, print None
        print(None)