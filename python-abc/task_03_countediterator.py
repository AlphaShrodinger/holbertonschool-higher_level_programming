#!/usr/bin/python3

class CountedIterator:
    '''CountedIterator class'''

    def __init__(self, iterable):
        '''Init method'''
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        '''Get count method'''
        return self.count

    def __next__(self):
        '''Next method'''
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration('No more items')
