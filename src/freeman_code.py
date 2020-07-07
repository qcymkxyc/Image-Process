#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/7/7 14:45
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : freeman_code.py
@Title   : Freeman链码实现
@Description    :
"""
import numpy as np

"""表示是按4方向编码还是按8方向编码"""
FOUR_DIRECTION = 1
EIGHT_DIRECTION = 2


def __get_freeman_box_list(
        img: np.ndarray, n_box_x: int = 10, n_box_y: int = 10) -> ([int], [int]):
    """给定一张图片，返回该图片对应的Freeman网格对应的坐标，坐标分为
    x和y，所以返回的是两个list，分别是x的list和y的list

    :param img: numpy.ndarray, 图片
    :param n_box_x: int ,x轴的网格数
    :param n_box_y: int, y轴的网格数
    :return: [int],[int]
        网格对应的list,list中的个数等于网格数加一
    """
    freeman_x_coordination_list = list()
    freeman_y_coordination_list = list()
    '''获取图像的长宽'''
    if len(img.shape) == 2:
        img_h, img_w = img.shape
    else:
        img_h, img_w, _ = img.shape

    # 获取每个网格的长和宽
    cell_w, cell_h = img_w / n_box_x, img_h / n_box_y
    for i in range(n_box_x + 1):
        freeman_x_coordination_list.append(i * cell_w)
    for i in range(n_box_y + 1):
        freeman_y_coordination_list.append(i * cell_h)

    return freeman_x_coordination_list, freeman_y_coordination_list


def __get_freeman_coordination(
        point: (int, int), freeman_x_list: list, freeman_y_list: list) -> (int, int):
    """给出当前点，放回该点在Freeman网格中的坐标

    :param point: (int,int), 点的坐标
    :param freeman_x_list: List[float], Freeman网格x
    :param freeman_y_list: List[float], Freeman网格y
    :return:
    """
    x, y = point
    '''如果该点在网格的线上'''
    if x in freeman_x_list or y in freeman_y_list:
        try:
            x_index = freeman_x_list.index(x)
        except ValueError:
            '''如果该点在横线上'''
            # TODO
            pass
        else:
            try:
                y_index = freeman_y_list.index(y)
            except ValueError:
                '''如果该点在纵线上'''
                # TODO
                pass
            else:
                '''如果该点刚好在Freeman编码的坐标点上'''
                # TODO
                pass
    else:
        '''如果没有'''
        return


def get_freeman_code(img: np.ndarray, contour: [
                     (int, int)], mode=EIGHT_DIRECTION) -> [int]:
    """给定图像和对应的边界，返回Freeman链码

    :param img: numpy.ndarray,  图像
    :param contour: List[(int,int)],边界的list
    :param mode: int,编码方式，表示是按4方向编码还是按8方向编码
    :return: [int], 弗雷曼链码
    """
    '''获取Freeman链码的网格坐标'''
    freeman_x_coordination_list, freeman_y_coordination_list = \
        __get_freeman_box_list(img=img)

    for point in contour:
        x, y = point
        if x in freeman_x_coordination_list and y in freeman_y_coordination_list:
            # TODO
            pass
