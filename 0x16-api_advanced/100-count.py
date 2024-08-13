#!/usr/bin/python3
""" count words"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """count function"""

    # URL construction
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom user agent'}
    params = {'after': after, 'limit': 100}

    # API request
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return

    # Parse the response JSON
    data = response.json().get('data', {})
    posts = data.get('children', [])
    after = data.get('after', None)

    # Initialize word count dictionary
    word_list = [word.lower() for word in word_list]
    if not word_count:
        word_count = {word: 0 for word in word_list}

    # Count the occurrences of each word in the titles
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            word_count[word] += title.split().count(word)

    # Recursively call the function if there are more posts
    if after:
        return count_words(subreddit, word_list, after, word_count)
    else:
        # Sort and print the word count
        sorted_words = sorted(word_count.items(),
                              key=lambda item: (-item[1], item[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")

# Example usage:
# count_words('programming', ['react', 'python', 'java',
# 'javascript', 'scala', 'no_results_for_this_one'])
