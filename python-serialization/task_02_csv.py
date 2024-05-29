#!/usr/bin/python3
'''CSV'''
import csv
import json


def convert_csv_to_json(csvfile):
    '''Convert to JSON'''
    try:
        with open(csvfile, 'r', encoding="utf-8") as f:
            csvReader = csv.DictReader(f)
            data = [row for row in csvReader]

        with open("data.json", 'w', encoding="utf-8") as g:
            json.dump(data, g)

        return True

    except FileNotFoundError:
        return False
