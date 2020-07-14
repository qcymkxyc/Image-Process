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
import cv2
import unittest
from src.chapter11 import freeman_code
from PIL import Image
import os
import numpy as np


def get_freeman_box_list(img, n_box_x, n_box_y):
    return freeman_code.__get_freeman_box_list(img, n_box_x, n_box_y)


def get_freeman_coordination(point, freeman_x_list, freeman_y_list):
    return freeman_code.__get_freeman_coordination(
        point, freeman_x_list, freeman_y_list)


class FreemanTest(TestCase):
    def setUp(self) -> None:
        root, _ = os.path.split(os.getcwd())
        img_path = os.path.join(root, "image_data")
        img_path = os.path.join(
            img_path, r"DIP3E_CH11_Original_Images/Fig1105(a)(noisy_stroke).tif")
        self.img = Image.open(img_path)
        self.img = np.asarray(self.img)

    def test_get_freeman_coordination_by_img(self):
        import matplotlib.pyplot as plt
        img_path = "../../image_data/DIP3E_CH11_Original_Images/Fig1105(a)(noisy_stroke).tif"
        img = Image.open(img_path)
        img = np.asarray(img)

        tmp_img = cv2.blur(img, (9, 9))
        th, tmp_img = cv2.threshold(
            tmp_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        image, contours, hierarchy = cv2.findContours(
            tmp_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        contour = contours[-1]
        contour = np.reshape(contour, (contour.shape[0], contour.shape[-1]))
        x = [i[0] for i in contour]
        y = [i[1] for i in contour]
        plt.plot(x, y)
        plt.show()

        a = freeman_code.get_freeman_coordination(tmp_img, contour)
        x = [i[0] for i in a]
        y = [i[1] for i in a]
        plt.plot(x, y)
        plt.show()

    def test_get_freeman_code(self):
        import matplotlib.pyplot as plt
        img_path = "../../image_data/DIP3E_CH11_Original_Images/Fig1105(a)(noisy_stroke).tif"
        img = Image.open(img_path)
        img = np.asarray(img)

        tmp_img = cv2.blur(img, (9, 9))
        th, tmp_img = cv2.threshold(
            tmp_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        image, contours, hierarchy = cv2.findContours(
            tmp_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        contour = contours[-1]
        contour = np.reshape(contour, (contour.shape[0], contour.shape[-1]))
        x = [i[0] for i in contour]
        y = [i[1] for i in contour]
        plt.plot(x, y)
        plt.show()

        a = freeman_code.get_freeman_code(tmp_img, contour)
        print(a)

    def test_get_freeman_coordination_by_point(self):
        freeman_x_list = np.arange(0, 100, 10).tolist()
        freeman_y_list = np.arange(0, 100, 10).tolist()

        """刚好在交点上"""
        point = (10, 10)
        r = get_freeman_coordination(point, freeman_x_list, freeman_y_list)
        self.assertEqual(r, (1, 1))

        """在横轴上"""
        point = (10, 22)
        r = get_freeman_coordination(point, freeman_x_list, freeman_y_list)
        self.assertEqual(r, (1, 2))

        """在纵轴上"""
        point = (22, 10)
        r = get_freeman_coordination(point, freeman_x_list, freeman_y_list)
        self.assertEqual(r, (2, 1))

        """没在线上"""
        point = (22, 22)
        r = get_freeman_coordination(point, freeman_x_list, freeman_y_list)
        self.assertIsNone(r)

    def test_get_freeman_box_list(self):
        n_box_x = 10
        n_box_y = 10
        x_list, y_list = get_freeman_box_list(self.img, n_box_x, n_box_y)
        self.assertEqual(len(x_list), n_box_x + 1)
        self.assertEqual(len(y_list), n_box_y + 1)

        img_h, img_w = self.img.shape
        self.assertLessEqual(x_list[-1], img_w)
        self.assertLessEqual(x_list[-1], img_h)


if __name__ == "__main__":
    unittest.main()
