#!/usr/bin/python3
'''Pickle'''
import pickle


class CustomObject:
    '''Class'''

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''Display'''
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        '''Serialized'''
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        '''Deserialize'''
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
