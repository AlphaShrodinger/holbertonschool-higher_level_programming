#!/usr/bin/python3
from abc import ABC, abstractmethod
'''Import abstractmethod'''


class Animal(ABC):
    '''Animal class'''
    @abstractmethod
    def sound(self):
        '''Sound method'''
        pass


class Dog(Animal):
    '''Dog class'''

    def sound(self):
        return 'Bark'


class Cat(Animal):
    '''Cat class'''

    def sound(self):
        return 'Meow'
