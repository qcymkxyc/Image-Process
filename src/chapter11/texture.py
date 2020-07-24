#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/7/24 10:41
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : texture.py
@Title   : 纹理
@Description    :  
"""
import numpy as np

# ===================================================================
# 建立等级矩阵
# ===================================================================


def __get_rank_list(gray_rank:int,max_value:int = 255,min_value:int = 0) -> [int]:
    """返回等级的list

    :param gray_rank: int, 等级数
    :param max_value: int, 像素值的最大值
    :param min_value: int, 像素值的最小值
    :return: List[int],分段的list
    """
    rank_list = list()
    num_value = max_value - min_value + 1
    current_value = min_value
    while current_value <= max_value:
        rank_list.append(current_value)
        interval_value = num_value // gray_rank
        current_value += interval_value

    """最后加入max value"""
    if rank_list[-1] < max_value:
        rank_list.append(max_value)
    return rank_list


def __get_rank_index(gray_value: int, rank_list: [int]) -> int:
    """给定灰度值和一个等级的list，返回该灰度值对应的index

    :param gray_value: int, 灰度值
    :param rank_list: List[int], 等级list
    :return: int, 等级index
    """
    for i in range(len(rank_list) - 1):
        current_value = rank_list[i]
        next_value = rank_list[i + 1]
        if current_value <= gray_value < next_value:
            return i

    """如果该值刚好是最大值，则放回最大的rank Index"""
    if gray_value == rank_list[-1]:
        return len(rank_list) - 2

# =================================================================
# 建立共生矩阵
# =================================================================


def __get_occurrence_matrix_by_rank_matrix(rank_matrix: np.ndarray, gray_rank: int) -> np.ndarray:
    """跟定一个等级矩阵，返回共生矩阵

    :param rank_matrix: numpy.array, 等级矩阵
    :param gray_rank: int, 灰度等级
    :return: numpy.array, 共生矩阵
    """
    # 共生矩阵
    co_occurrence_matrix = np.zeros(shape=(gray_rank, gray_rank))
    for i_row in range(len(rank_matrix)):
        for i_col in range(len(rank_matrix[0]) - 1):
            current_value = rank_matrix[i_row][i_col]
            next_value = rank_matrix[i_row][i_col + 1]
            co_occurrence_matrix[current_value][next_value] += 1

    return co_occurrence_matrix


# =================================================================
# Main
# =================================================================


def get_co_occurrence_matrix(img: np.ndarray, gray_rank: int = 8) -> np.ndarray:
    """给定一张图片，返回灰度共生矩阵

    步骤如下：
        * 给出每一个像素值对应的等级
            * 给出等级分段的list
            * 给出该像素值对应的分段index
        * 从左到右扫描两个像素，在对应的共生矩阵加1
            * 初始化一个共生矩阵，里面的值全为0
            * 根据两个index锁定位置的元素加1
    :param img: numpy.array, 图片
    :param gray_rank: int, 共生矩阵的等级数
    :return: numpy.array, 共生矩阵
    """
    """排序list"""
    rank_list = __get_rank_list(gray_rank=gray_rank)
    """获取Rank矩阵"""
    get_rank_matrix_f = np.frompyfunc(lambda x: __get_rank_index(x,rank_list), 1, 1)
    rank_matrix = get_rank_matrix_f(img)

    """获取共生矩阵"""
    return __get_occurrence_matrix_by_rank_matrix(rank_matrix=rank_matrix,gray_rank=gray_rank)
