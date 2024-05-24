#!/usr/bin/python3

class Fish:
    '''Fish class'''

    def swim(self):
        '''Swim method'''
        print('The fish is swimming')

    def habitat(self):
        '''Habitat method'''
        print('The fish lives in water')


class Bird:
    '''Bird class'''

    def fly(self):
        '''Fly method'''
        print('The bird is flying')

    def habitat(self):
        '''Habitat method'''
        print('The bird lives in the sky')


class FlyingFish(Fish, Bird):
    '''FlyingFish class'''

    def fly(self):
        '''Re-writing fly class'''
        print('The flying fish is soaring!')

    def swim(self):
        '''Re-writing swim class'''
        print('The flying fish is swimming!')

    def habitat(self):
        '''Re-writing habitat class'''
        print('The flying fish lives both in water and the sky!')
