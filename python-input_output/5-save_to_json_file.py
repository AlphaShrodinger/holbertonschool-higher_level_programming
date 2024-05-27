#!/usr/bin/python3
'''Save to json file'''

import json


def save_to_json_file(my_obj, filename):
    '''Save object to file'''
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
