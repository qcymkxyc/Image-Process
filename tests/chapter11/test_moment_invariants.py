#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/25 15:39
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : test_moment_invariants.py
@Title   : 
@Description    :  
"""
import unittest
from src.chapter11 import moment_invariants
import numpy as np
from PIL import Image


class MomentInvariantsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        img_path = r"../../image_data/DIP3E_CH11_Original_Images/Fig1137(a)(painting_original_padded).tif"
        self.img = Image.open(img_path)
        self.img = np.asarray(self.img)
        self.img = self.img.astype(np.uint8)

    def test_get_moment_invariants_seq(self):
        moment_invariants.get_moment_invariants_seq(self.img)


if __name__ == '__main__':
    unittest.main()
