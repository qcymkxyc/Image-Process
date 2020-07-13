#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/10 14:25
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : test_mark_sheet.py
@Title   :
@Description    :
"""
import unittest
from PIL import Image
import numpy as np
from src import mark_sheet


class MarkSheetTestCase(unittest.TestCase):
    def setUp(self) -> None:
        img_path = r"../image_data/DIP3E_CH11_Original_Images/Fig1111(a)(triangle).tif"
        self.img = Image.open(img_path)
        self.img = np.asarray(self.img)
        self.img = self.img.astype(np.uint8)

    def test_get_centroid(self):
        centroid = mark_sheet.get_centroid(self.img)
        print(centroid)
        import matplotlib.pyplot as plt
        plt.imshow(self.img, cmap="gray")
        plt.plot([centroid[1]], [centroid[0]], linewidth="10", color="green")
        plt.show()

    def test_get_mark_sheet(self):
        r = mark_sheet.get_mark_sheet(self.img)
        import matplotlib.pyplot as plt
        plt.plot(r)
        plt.show()


if __name__ == '__main__':
    unittest.main()
