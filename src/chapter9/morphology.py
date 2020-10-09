#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/9/28 17:14
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : hit.py
@Title   : 
@Description    :  
"""
import numpy as np
import cv2


def hit(img: np.ndarray, shape1: np.ndarray, shape2: np.ndarray):
    """击中

    :param img: numpy.array, 图像
    :param shape1: numpy.array, 匹配的模板，即目标模板
    :param shape2: numpy.array, 匹配模板的反模板，即背景模板
    """
    if shape1.dtype != np.uint8 or shape2.dtype != np.uint8:
        raise TypeError

    part1 = cv2.erode(img, shape1)
    part2 = cv2.erode(1 - img, shape2)

    return np.logical_and((part1 == part2), part1 == 1).astype(int)


def connected_area(img:np.ndarray, start_coordination:(int, int)) -> np.ndarray:
    """提取连通分量

    :param img: numpy.array, 图像
    :param start_coordination: (int,int), 起始位置
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    last_temp_img = np.zeros_like(img)
    last_temp_img[start_coordination] = 1
    current_temp_img = cv2.dilate(last_temp_img, kernel)

    while (current_temp_img != last_temp_img).any():
        last_temp_img = current_temp_img
        current_temp_img = cv2.dilate(current_temp_img, kernel)
        current_temp_img = np.logical_and((current_temp_img == img), current_temp_img == 1).astype(float)

    return current_temp_img


def blank_fill(img:np.ndarray, start_coordination:(int,int)) -> np.ndarray:
    """孔洞填充

    :param img: numpy.array, 图像
    :param start_coordination: 起始位置
    :return: numpy.array:填充结果
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

    last_temp_img = np.zeros_like(img)
    last_temp_img[start_coordination] = 1
    current_temp_img = cv2.dilate(last_temp_img, kernel)

    while (current_temp_img != last_temp_img).any():
        last_temp_img = current_temp_img
        current_temp_img = cv2.dilate(current_temp_img, kernel)

        current_temp_img = np.logical_and(current_temp_img == 1, current_temp_img == (1 - img)).astype(float)

    return current_temp_img


def rebuild_open(img: np.ndarray, kernel: np.ndarray, erode_time: int = 1) -> np.ndarray:
    """重建开操作

    :param img: numpy.array, 图像
    :param kernel: numpy.array, 开操作的核
    :param erode_time: int, 腐蚀次数
    """
    """多次腐蚀"""
    temp_img = img.copy()
    for i in range(erode_time):
        temp_img = cv2.erode(temp_img, kernel)

    """测地膨胀"""
    dialate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    last_img = temp_img.copy()

    while True:
        current_img = cv2.dilate(last_img, dialate_kernel)
        current_img = np.logical_and(current_img == 1, current_img == img)
        current_img = current_img.astype(float)

        if (current_img == last_img).all():
            break
        else:
            last_img = current_img

    return current_img
