#!/usr/bin/python3
"""
function that queries the reddit api and
prints the titles of the 10 trending post.
"""
import requests


def top_ten(subreddit):
    """Define the Reddit API URL for the subreddit's hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"

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

            if not posts:
                print("No hot posts found for this subreddit.")
            else:
                for index, post in enumerate(posts):
                    """Extract and print the title of each post"""
                    print(f"{index + 1}. {post['data']['title']}")
        except (KeyError, ValueError):
            """Handle JSON parsing errors"""
            print("Error parsing the Reddit API response.")
    else:
        """Invalid subreddit or another issue with the request"""
        print("None")
