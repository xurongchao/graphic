import numpy as np
import matplotlib.pyplot as plt

class Node:

    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next(self):
        return self._next

    def set_next(self, next):
        self._next = next

class Link_list:

    def __init__(self):
        self._head = None
        self._size = 0

    def get_head(self):
        return self._head

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._head is None

    def insert(self, data):
        temp = Node(data)
        if self._head is None:
            self._head = temp
        else:
            flag = self._head
            while flag.get_next() is not None:
                flag = flag.get_next()
            flag.set_next(temp)
        self._size += 1

    def remove(self, data):
        flag = self._head
        pre = None
        while flag.get_next() is not None:
            if flag.get_data() == data:
                if pre is None:
                    self._head = flag.get_next()
                else:
                    pre.set_next(flag.get_next())
                break
            else:
                pre = flag
                flag = flag.get_next()
        self._size -= 1



