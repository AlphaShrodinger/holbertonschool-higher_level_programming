#!/usr/bin/python3
'''Student file'''


class Student:
    '''Student class'''

    def __init__(self, first_name, last_name, age):
        '''init method'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''to json method'''
        return self.__dict__
