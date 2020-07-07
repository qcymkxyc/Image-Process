#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/7/7 15:13
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : test_freeman_code.py
@Title   :
@Description    :
"""
from unittest import TestCase
import unittest
from src import freeman_code
from PIL import Image
import os
import numpy as np


def get_freeman_box_list(img, n_box_x, n_box_y):
    return freeman_code.__get_freeman_box_list(img, n_box_x, n_box_y)


class FreemanTest(TestCase):
    def setUp(self) -> None:
        root, _ = os.path.split(os.getcwd())
        img_path = os.path.join(root, "image_data")
        img_path = os.path.join(
            img_path, r"DIP3E_CH11_Original_Images/Fig1105(a)(noisy_stroke).tif")
        self.img = Image.open(img_path)
        self.img = np.asarray(self.img)

    def test_get_freeman_code(self):
        pass

    def test_get_freeman_box_list(self):
        n_box_x = 10
        n_box_y = 10
        x_list,y_list = get_freeman_box_list(self.img,n_box_x,n_box_y)
        self.assertEqual(len(x_list),n_box_x + 1)
        self.assertEqual(len(y_list),n_box_y + 1)

        img_h,img_w = self.img.shape
        self.assertLessEqual(x_list[-1],img_w)
        self.assertLessEqual(x_list[-1],img_h)


if __name__ == "__main__":
    unittest.main()
