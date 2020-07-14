#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/14 14:50
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : test_shape_number.py
@Title   :
@Description    :
"""
import unittest
from src.chapter11 import shape_number
import os
from PIL import Image
import numpy as np


def get_shape_number_by_freeman_difference(
        freeman_difference_list: [int]) -> [int]:
    return shape_number.__get_shape_number_by_freeman_difference(freeman_difference_list)


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        root, _ = os.path.split(os.getcwd())
        img_path = os.path.join(root, "image_data")
        img_path = os.path.join(
            img_path, r"DIP3E_CH11_Original_Images/Fig1105(a)(noisy_stroke).tif")
        self.img = Image.open(img_path)
        self.img = np.asarray(self.img)

    def test_shape_number_by_freeman_difference(self):
        x = np.random.randint(0, 8, size=10)
        print(x)
        y = get_shape_number_by_freeman_difference(x)
        print(np.asarray(y))

    def test_get_shape_number(self):
        pass


if __name__ == '__main__':
    unittest.main()
