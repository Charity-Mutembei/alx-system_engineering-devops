#!/usr/bin/python3
"""
function that queries the reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """Define the Reddit API URL for the subreddit's about page"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    """Set a custom User-Agent to avoid Reddit API request issues"""
    headers = {'User-Agent': 'YourBotName/1.0'}

    """Send a GET request to the API"""
    response = requests.get(url, headers=headers)

    """Check if the response status code indicates success"""
    if response.status_code == 200:
        try:
            """Parse the JSON response"""
            data = response.json()
            """Extract the number of subscribers"""
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            """Handle JSON parsing errors"""
            return 0
    else:
        """Invalid subreddit or another issue with the request"""
        return 0
