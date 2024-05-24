#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
'''Import abstractmethod'''


class Shape(ABC):
    '''Shape class'''
    @abstractmethod
    def area(self):
        '''Area method'''
        pass

    @abstractmethod
    def perimeter(self):
        '''Perimeter method'''
        pass


class Circle(Shape):
    '''Circle class'''

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        '''Area method circle'''
        return pi * (self.radius ** 2)

    def perimeter(self):
        '''Perimeter method circle'''
        return 2 * pi * self.radius


class Rectangle(Shape):
    '''Rectangle class'''

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        '''Area method rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Perimeter method rectange'''
        return (self.width * 2 + self.height * 2)


def shape_info(self):
    '''Calls area and perimeter methods'''
    area = self.area()
    perimeter = self.perimeter()

    print(f'Area: {area}')
    print(f'Perimeter: {perimeter}')
