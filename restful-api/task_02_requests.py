#!/usr/bin/python3
'''Requests'''
import requests
import csv


def fetch_and_print_posts():
    '''Fetch and prints'''
    data = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {data.status_code}")
    if data.status_code == 200:
        for post in data.json():
            print(post['title'])


def fetch_and_save_posts():
    '''Fetch and save'''
    data = requests.get('https://jsonplaceholder.typicode.com/posts')
    if data.status_code == 200:
        postlist = []
        for post in data.json():
            postlist.append({'id': post['id'], 'title': post['title'],
                             'body': post['body']})

        with open("posts.csv", 'w', encoding="utf-8") as file:
            map = ['id', 'title', 'body']
            author = csv.DictWriter(file, fieldnames=map)
            author.writeheader()
            for post in postlist:
                author.writerow(post)
