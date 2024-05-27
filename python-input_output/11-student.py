#!/usr/bin/python3
'''Student file'''


class Student:
    '''Student class'''

    def __init__(self, first_name, last_name, age):
        '''init method'''
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        '''to json method'''
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
