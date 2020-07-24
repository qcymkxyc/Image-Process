#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/7/14 14:31
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : shape_number.py
@Title   : 形状数
@Description    :
"""
import numpy as np
from src.chapter11 import freeman_code


# =============================================================
# 获取差分编码
# =============================================================


def __get_freeman_difference(freeman_code_list: [int]) -> [int]:
    """给定Freeman List，返回Freeman差分

    :param freeman_code_list: List[int],Freeman编码的List，
    :return: List[int], 差分后的编码
    """
    # 用于保存差分后的编码
    different_code_list = list()
    for i in range(len(freeman_code_list) - 1):
        current_code = freeman_code_list[i]
        next_code = freeman_code_list[i + 1]
        if next_code < current_code:
            next_code += 8
        different_code_list.append(next_code - current_code)
    return different_code_list


# ===============================================================
# 获取形状数
# ===============================================================

def __get_shape_number_by_freeman_difference(
        freeman_difference_list: [int]) -> [int]:
    """给定已经差分后的freeman编码，返回形状数

    :param freeman_difference_list: List[int], 差分后的Freeman编码
    :return: List[int],形状数
    """
    queue1, queue2 = list(), list()
    min_num = np.min(freeman_difference_list)

    # queue1用于存放最小数前面的数字，queue2用于存放最小数后面的数字（包括最小数）
    # 最后将两个queue拼接在一起即是最后的结果
    queue = queue1
    for num in freeman_difference_list:
        if num == min_num:
            queue = queue2
        queue.append(num)
    return queue2 + queue1


# ===============================================================
# 主函数
# ===============================================================

def get_shape_number(img: np.ndarray, contour: [(int, int)]) -> [int]:
    """给定一幅图像以及边界的List，返回形状数

    :param img: numpy.ndarray, 图像
    :param contour: List[(int,int)],边界的list
    :return: List[int],形状数
    """
    """获取Freeman编码"""
    freeman_code_list = freeman_code.get_freeman_code(img, contour)

    """获取差分编码"""
    freeman_difference_list = __get_freeman_difference(freeman_code_list)

    """获取形状数"""
    return __get_shape_number_by_freeman_difference(freeman_difference_list)
