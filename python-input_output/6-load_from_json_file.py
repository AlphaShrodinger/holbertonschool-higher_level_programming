#!/usr/bin/python3
'''Load from json to file'''

import json


def load_from_json_file(filename):
    '''load from json method'''
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
