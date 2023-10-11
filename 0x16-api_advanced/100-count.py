#!/usr/bin/python3
"""
a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests
import re


def count_words(subreddit, word_list, counts=None, after=None):
    if counts is None:
        counts = {}
    if after is None:
        after = ''

    """Define the Reddit API URL for the subreddit's hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=25&after={after}"

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

            for post in posts:
                title = post['data']['title'].lower()
                for keyword in word_list:
                    """Check if the keyword appears
                    in the title, ignoring case and word boundaries"""
                    occurrences = len(re.findall(rf'\b{re.escape(keyword)}\b', title, re.IGNORECASE))
                    if occurrences > 0:
                        counts[keyword] = counts.get(keyword, 0) + occurrences

            if after:
                """Recursively call the function with the 'after' parameter"""
                return count_words(subreddit, word_list, counts, after)
            else:
                """Sort the counts in descending order
                by count and then alphabetically"""
                sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

                for keyword, count in sorted_counts:
                    print(f"{keyword}: {count}")

        except (KeyError, ValueError):
            """Handle JSON parsing errors"""
            return
    else:
        """Invalid subreddit or another issue with the request"""
        return
