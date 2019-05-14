from link_list import Link_list
import numpy as np
import matplotlib.pyplot as plt


class Scan:
    def __init__(self, image, polygon):
        self._image = image
        self._polygon = polygon
        self._ET = []

    def get_image(self):
        return self._image

    def _get_range(self):
        y_max = 0
        y_min = np.shape(self._image)[1]
        for [x, y] in enumerate(self._polygon):
            if y[1] > y_max:
                y_max = y[1] #enumerate [1]
            if y[1] < y_min:
                y_min = y[1]
        #print(y_min, y_max)
        return y_min, y_max

    def _gen_ET(self):
        if len(self._ET) == 0:
            (width, height) = np.shape(self._image)
            for i in range(height):
                self._ET.append(None)

            Ymin, Ymax = self._get_range()
            l = len(self._polygon)
            for i in range(Ymin, Ymax+1): #range不包括最后
                for j in range(0, l):
                    if self._polygon[j][1] == i:
                        if self._polygon[(j+1+l)%l][1] > self._polygon[j][1]:
                            [x1, y1] = self._polygon[(j+1+l)%l]
                            [x0, y0] = self._polygon[j]
                            dalta = (x0 - x1) / (y0 - y1)
                            self._ET[i] = Link_list()
                            self._ET[i].insert([x0, y1, dalta])
                        if self._polygon[(j-1+l)%l][1] > self._polygon[j][1]:
                            [x1, y1] = self._polygon[(j - 1 + l) % l]
                            [x0, y0] = self._polygon[j]
                            dalta = (x0 - x1) / (y0 - y1)
                            if self._ET[i] is None:
                                self._ET[i] = Link_list()
                                self._ET[i].insert([x0, y1, dalta])
                            else:
                                self._ET[i].insert([x0, y1, dalta])



    def paint(self):
        self._gen_ET()
        [Ymin, Ymax] = self._get_range()
        AET = Link_list()
        for i in range(Ymin, Ymax+1):
            if not AET.is_empty():
                head = AET.get_head()
                while head is not None:
                    [s_x, s_y, s_dalta] = head.get_data()
                    s_x += s_dalta
                    head.set_data([s_x, s_y, s_dalta])
                    head = head.get_next()

            if not AET.is_empty():
                head = AET.get_head()
                x_list = []
                while head is not None:
                    [start_x,_,_] = head.get_data()
                    x_list.append(start_x)
                    head = head.get_next()

                x_list.sort()
                print(len(x_list))
                for i1 in range(0, len(x_list), 2):
                    x1 = x_list[i1]
                    x2 = x_list[i1+1]
                    for j in range(int(x1), int(x2)+1):
                        self._image[j][i] = 0
                        #print([j, i])

            if not AET.is_empty():
                head = AET.get_head()
                while head is not None:
                    [s_x, s_y, s_dalta] = head.get_data()
                    if s_y == i:
                        AET.remove([s_x, s_y, s_dalta])
                    head = head.get_next()

            if self._ET[i] is not None:
                head = self._ET[i].get_head()
                while head is not None:
                    AET.insert(head.get_data())
                    head = head.get_next()

if __name__ == '__main__':
    image = np.ones([500, 500])

    plt.xlim(0, 500)
    plt.ylim(0, 500)
    polygon = [
        [180, 80],
        [90, 200],
        [140, 380],
        [220, 290],
        [360, 400],
        [320, 250],
        [260, 100],
    ]
    my_scan = Scan(image, polygon)
    my_scan.paint()
    plt.imshow(image, plt.cm.autumn)
    plt.show()











