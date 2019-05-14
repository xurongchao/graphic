from .link_list import Node
from .link_list import Link_list
import numpy as np

class Scan:
    def __init__(self, image, polygon):
        self._image = image
        self._polygon = polygon
        self._ET = []

    def _get_range(self):
        y_max = 0
        y_min = np.shape(self._image)[1]
        for [x, y] in enumerate(self._polygon):
            if y > y_max:
                y_max = y[1] #enumerate [1]
            if y < y_min:
                y_min = y[1]

        return y_min, y_max

    
