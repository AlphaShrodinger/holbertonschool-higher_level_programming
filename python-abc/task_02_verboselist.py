#!/usr/bin/python3

class VerboseList(list):
    '''VerboseList class'''

    def append(self, item):
        '''Append method'''
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        '''Extend method'''
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        '''Remove method'''
        if item in self:
            print(f"Removed [{item}] from the list.")
        else:
            print(f"[{item}] not found in the list.")
        super().remove(item)

    def pop(self, index=None):
        '''Pop method'''
        if index is None:
            if self:
                item = super().pop()
                print(f"Popped [{item}] from the list.")
                return item
            else:
                raise IndexError("Cannot pop from an empty list.")
        else:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
