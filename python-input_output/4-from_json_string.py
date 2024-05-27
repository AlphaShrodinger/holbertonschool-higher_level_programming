#!/usr/bin/python3
'''JASON string to object'''

import json


def from_json_string(my_str):
    '''json string to object method'''
    return json.loads(my_str)
