#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/9/3 11:32
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : moment_invariants.py
@Title   : 不变矩
@Description    :
"""
import numpy as np
import logging


def get_rank_moment(image: np.ndarray, row_moment: int,
                    col_moment: int) -> np.ndarray:
    """返回不变矩,阶数为row_moment + col_moment

    :param image: numpy.array, 图像
    :param row_moment: int, 行阶数
    :param col_moment: int, 列阶数
    :return: numpy.array,不变矩
    """
    """初始化"""
    moment = 0.

    """计算矩"""
    n_row, n_col = image.shape
    for i_row in range(n_row):
        for j_col in range(n_col):
            moment += np.power(i_row, row_moment)\
                * np.power(j_col, col_moment) * image[i_row][j_col]
    return moment


def get_center_moment(image: np.ndarray, row_moment: int,
                      col_moment: int) -> np.ndarray:
    """计算中心矩

    :param image: numpy.array, 图像
    :param row_moment: int，行阶数
    :param col_moment: int，列阶数
    :return: numpy.array, 中心矩
    """
    """计算均值"""
    '''计算1阶矩'''
    rank_moment00 = get_rank_moment(image, row_moment=0, col_moment=0)
    rank_moment10 = get_rank_moment(image, row_moment=1, col_moment=0)
    rank_moment01 = get_rank_moment(image, row_moment=0, col_moment=1)

    '''计算均值'''
    mean_row = rank_moment10 / rank_moment00
    mean_col = rank_moment01 / rank_moment00

    """计算不变矩"""
    moment = 0.
    n_row, n_col = image.shape
    for i_row in range(n_row):
        for j_col in range(n_col):
            moment += np.power((i_row - mean_row), row_moment) * \
                np.power((j_col - mean_col), col_moment) * image[i_row][j_col]
    return moment


def normal_center_moment(image: np.ndarray, row_moment: int,
                         col_moment: int) -> np.ndarray:
    """计算归一化后的中心矩

    :param image: numpy.array, 图像
    :param row_moment: int，行阶数
    :param col_moment: int，列阶数
    :return: numpy.array, 中心矩
    """
    """中心矩"""
    center_moment = get_center_moment(
        image, row_moment=row_moment, col_moment=col_moment)

    """归一化的分母部分"""
    tmp_center_moment = get_center_moment(image, row_moment=0, col_moment=0)
    tmp_power = (row_moment + col_moment) / 2 + 1
    tmp_moment = tmp_center_moment ** tmp_power

    return center_moment / tmp_moment


def get_moment_invariants_seq(image: np.ndarray) -> list:
    """返回二阶和三阶不变矩组（7个）

    :param image: numpy.array, 图片
    :return:
    """

    """计算归一化后的中心矩"""
    '''二阶'''
    logging.info("正在计算二阶中心矩")
    moment20 = normal_center_moment(image, row_moment=2, col_moment=0)
    moment02 = normal_center_moment(image, row_moment=0, col_moment=2)
    moment11 = normal_center_moment(image, row_moment=1, col_moment=1)
    '''三阶'''
    logging.info("正在计算三阶中心矩")
    moment03 = normal_center_moment(image, 0, 3)
    moment12 = normal_center_moment(image, 1, 2)
    moment21 = normal_center_moment(image, 2, 1)
    moment30 = normal_center_moment(image, 3, 0)

    """计算不变矩组"""
    logging.info("正在计算不变矩组")
    num1 = moment02 + moment20
    num2 = (moment02 - moment20) ** 2 + 4 * moment11 ** 2
    num3 = (moment30 - 3 * moment12) ** 2 + (3 * moment21 - moment03) ** 2
    num4 = (moment30 + moment12) ** 2 + (moment21 + moment03) ** 2
    num5 = (moment30 - 3 * moment12) * (moment30 + moment12) * ((moment30 + moment12) ** 2 - 3 * (moment21 + moment03) ** 2) + \
        (3 * moment21 - moment03) * (moment21 + moment03) * \
        (3 * (moment30 - moment12) ** 2 - (moment21 - moment03) ** 2)
    num6 = (moment20 - moment02) * ((moment30 + moment12) ** 2 - (moment21 + moment03)
                                    ** 2) + 4 * moment11 * (moment30 + moment12) * (moment21 + moment03)
    num7 = (3 * moment21 - moment03) * (moment30 + moment12) * ((moment30 + moment12) ** 2 - 3 * (moment21 + moment03) ** 2) + \
        (3 * moment12 - moment03) * (moment21 + moment03) * \
        (3 * (moment30 + moment12) ** 2 - (moment21 - moment03) ** 2)

    moment_invariants_list = [num1, num2, num3, num4, num5, num6, num7]
    return moment_invariants_list
