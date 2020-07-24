#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/24 11:16
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : test_texture.py
@Title   :
@Description    :
"""
import unittest
from src.chapter11 import texture
import numpy as np


def get_rank_list(grak_rank, max_value=255, min_value=0):
    return texture.__get_rank_list(grak_rank, max_value, min_value)


def get_rank_index(gray_value: int, rank_list: [int]) -> int:
    return texture.__get_rank_index(gray_value, rank_list)


class TextureTestCase(unittest.TestCase):
    def test_get_rank_list(self):
        rank_list = get_rank_list(8)
        print(rank_list)
        self.assertEqual(len(rank_list), 9)

    def test_get_rank_index(self):
        rank_list = get_rank_list(8)
        print(rank_list)
        gray_value = 130
        rank_index = get_rank_index(gray_value, rank_list=rank_list)
        self.assertEqual(rank_index, 4)

        rank_index = get_rank_index(255, rank_list=rank_list)
        print(rank_index)
        self.assertEqual(rank_index, 7)

        rank_index = get_rank_index(0, rank_list)
        self.assertEqual(rank_index, 0)

    def test_co_occurrence_matrix(self):
        img = np.random.randint(0, 255, size=(10, 10))
        occurrence_matrix = texture.get_co_occurrence_matrix(img)
        print(occurrence_matrix)


if __name__ == '__main__':
    unittest.main()
