#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def top_ten(subreddit):
    """Read reddit API and return top 10 hotspots """
    username = 'ahmed'
    password = 'ahmed'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/ahmed API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        for a in list_titles[:10]:
            print(a['data']['title'])
    else:
        return(print("None"))
