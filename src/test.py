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
    
