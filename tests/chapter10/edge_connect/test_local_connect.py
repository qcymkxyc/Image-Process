#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2021/5/28 11:12
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : test_local_connect.py
@Title   : 
@Description    :  
"""
from src.chapter10.edge_connect import local_connect
import cv2
import matplotlib.pyplot as plt
import unittest


class LocalConnectTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.img = cv2.imread("1863694-20191206105727406-2050307115.jpg")
        self.gray_img = cv2.cvtColor(self.img,cv2.COLOR_RGB2GRAY)
        self.binary_img = cv2.threshold(self.gray_img,127,1,cv2.THRESH_BINARY)[1]
        self.binary_img = self.binary_img.astype("uint8")

    def test_local_connect(self):
        plt.imshow(self.gray_img)
        plt.show()

        gray_img = cv2.Laplacian(self.gray_img,-1)
        plt.imshow(gray_img)
        plt.show()

        res = local_connect.local_connect(self.binary_img,
                                    gradient_angle_threshold=90,
                                    gradient_angle_bandwidth=45,
                                    gradient_value_threshold_rate=0.3)
        plt.imshow(res)
        plt.show()


if __name__ == '__main__':
    unittest.main()
