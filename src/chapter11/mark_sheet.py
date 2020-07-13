#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/7/10 14:21
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : mark_sheet.py
@Title   : 标记图
@Description    :
"""
from scipy.spatial.distance import euclidean
import numpy as np
import cv2


def get_centroid(img: np.ndarray) -> (int, int):
    """给定一张图的，返回其亮点的质心

    :param img: numpy.ndarray, 图像
    :return: (int,int), 质心的坐标
    """
    white_point = np.where([img == 1])
    x = white_point[1].mean()
    y = white_point[2].mean()

    return x, y


def get_mark_sheet(img: np.ndarray) -> np.ndarray:
    """根据图像返回标记图

    :param img: numpy.array,
    :return:
    """
    # TODO 结果有问题
    distance_list = list()
    '''获取质心'''
    centroid = get_centroid(img)

    '''获取边界'''
    image, contours, hierarchy = cv2.findContours(
        img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contour = contours[0]
    '''距离list'''
    for point in contour:
        dist = euclidean(centroid, point)
        distance_list.append(dist)
    return distance_list


def get_mark_sheet_by_contour(
        centroid: (int, int), contour: [(int, int)]):
    """给定边界的list，返回距离的list

    :param centroid: (int,int),质心
    :param contour: List[(int,int)],边界
    :return: List[int], 距离的List
    """
    distance_list = list()
    '''距离list'''
    for point in contour:
        dist = euclidean(centroid, point)
        distance_list.append(dist)
    return distance_list
