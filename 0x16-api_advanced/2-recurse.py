#!/usr/bin/python3
"""
recursive function for the reddit api query
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    """Define the Reddit API URL for the subreddit's hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=25"

    """Add 'after' parameter if it's provided"""
    if after:
        url += f'&after={after}'

    """Set a custom User-Agent to avoid Reddit API request issues"""
    headers = {'User-Agent': 'YourBotName/1.0'}

    """Send a GET request to the API"""
    response = requests.get(url, headers=headers)

    """Check if the response status code indicates success"""
    if response.status_code == 200:
        try:
            """Parse the JSON response"""
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            if not posts:
                return hot_list
            else:
                for post in posts:
                    hot_list.append(post['data']['title'])

                """Recursively call the function with the 'after' parameter"""
                return recurse(subreddit, hot_list, after)
        except (KeyError, ValueError):
            """Handle JSON parsing errors"""
            return None
    else:
        """Invalid subreddit or another issue with the request"""
        return None
