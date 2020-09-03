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


def __get_rank_list(gray_rank: int, max_value: int = 255,
                    min_value: int = 0) -> [int]:
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


def __get_occurrence_matrix_by_rank_matrix(
        rank_matrix: np.ndarray, gray_rank: int, n_step: int = 1) -> np.ndarray:
    """跟定一个等级矩阵，返回共生矩阵，且会根据不同的跳数返回不同的共生矩阵

    :param rank_matrix: numpy.array, 等级矩阵
    :param gray_rank: int, 灰度等级
    :param n_step: int, 跳数,默认为1，表示相邻的元素建立跳数
    :return: numpy.array, 共生矩阵
    """
    if n_step < 1:
        raise ValueError("跳数设定错误")
    """初始化"""
    # 共生矩阵
    co_occurrence_matrix = np.zeros(shape=(gray_rank, gray_rank))

    """计算共生矩阵"""
    for i_row in range(len(rank_matrix)):
        for i_col in range(len(rank_matrix[0]) - n_step):
            current_value = rank_matrix[i_row][i_col]
            next_value = rank_matrix[i_row][i_col + n_step]
            co_occurrence_matrix[current_value][next_value] += 1

    return co_occurrence_matrix


# ================================================================
# 共生矩阵描述子辅助函数
# ================================================================

def __get_probability_matrix(occurrence_matrix: np.ndarray) -> np.ndarray:
    """给定共生矩阵，返回概率矩阵

    :param occurrence_matrix: numpy.array, 共生矩阵
    :return: numpy.array, 概率矩阵
    """
    return occurrence_matrix / np.sum(occurrence_matrix)


def __get_occurrence_mean(occurrence_matrix: np.ndarray, axis=0) -> float:
    """返回共生矩阵的平均值

    :param occurrence_matrix: numpy.array, 共生矩阵
    :param axis: int, 方向，同numpy
    :return: numpy.array, 行平均向量
    """
    prob_matrix = __get_probability_matrix(occurrence_matrix)
    tmp_mean = np.sum(prob_matrix, axis=axis)

    mean_value = 0.
    for i in range(len(tmp_mean)):
        mean_value += (i + 1) * tmp_mean[i]
    return mean_value


def __get_occurrence_variance(occurrence_matrix: np.ndarray, axis=0) -> float:
    """返回共生矩阵的方差

    :param occurrence_matrix: numpy.array,共生矩阵
    :param axis: int, 方向
    :return: float, 方差
    """
    prob_matrix = __get_probability_matrix(occurrence_matrix)
    tmp_mean_vec = np.sum(prob_matrix, axis=axis)
    mean_value = __get_occurrence_mean(occurrence_matrix, axis=axis)

    var_value = 0.
    for i in range(len(tmp_mean_vec)):
        var_value += (i + 1 - mean_value) ** 2 * tmp_mean_vec[i]

    return var_value


# =================================================================
# Main
# =================================================================


def get_co_occurrence_matrix(
        img: np.ndarray, gray_rank: int = 8) -> np.ndarray:
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
    get_rank_matrix_f = np.frompyfunc(
        lambda x: __get_rank_index(
            x, rank_list), 1, 1)
    rank_matrix = get_rank_matrix_f(img)

    """获取共生矩阵"""
    return __get_occurrence_matrix_by_rank_matrix(
        rank_matrix=rank_matrix, gray_rank=gray_rank)


def get_co_occurrence_correlation_seq(
        img: np.ndarray, gray_rank: int = 8, start_step: int = 1, end_step: int = 50) -> list:
    """

    :param img: numpy.array, 图像
    :param gray_rank: int,共生矩阵的等级数
    :param start_step: int,开始跳数
    :param end_step: int, 结束跳数
    :return: list, 共生矩阵相关性序列
    """
    """获取等级矩阵"""
    '''排序list'''
    rank_list = __get_rank_list(gray_rank=gray_rank)
    '''获取Rank矩阵'''
    get_rank_matrix_f = np.frompyfunc(
        lambda x: __get_rank_index(
            x, rank_list), 1, 1)
    rank_matrix = get_rank_matrix_f(img)

    """计算共生矩阵的相关性"""
    correlation_list = list()
    for step in range(start_step, end_step):
        occurrence_matrix = __get_occurrence_matrix_by_rank_matrix(
            rank_matrix=rank_matrix, gray_rank=gray_rank, n_step=step)
        correlation = get_correlation(occurrence_matrix)
        correlation_list.append(correlation)
    return correlation_list


# ================================共生矩阵描述子=========================


def get_max_probability(occurrence_matrix: np.ndarray):
    """给定共生矩阵，返回最大概率

    :param occurrence_matrix: numpy.array, 共生矩阵
    :return: float, 最大概率
    """
    return np.max(occurrence_matrix) / np.sum(occurrence_matrix)


def get_correlation(occurrence_matrix: np.ndarray) -> float:
    """给定共生矩阵，返回其相关性

    :param occurrence_matrix: numpy.array, 共生矩阵
    :return: float, 相关性
    """
    """概率矩阵"""
    prob_matrix = __get_probability_matrix(occurrence_matrix)
    """行平均以及列平均"""
    row_mean = __get_occurrence_mean(occurrence_matrix, axis=0)
    col_mean = __get_occurrence_mean(occurrence_matrix, axis=1)
    """行方差以及列方差"""
    row_var = __get_occurrence_variance(occurrence_matrix, axis=0)
    col_var = __get_occurrence_variance(occurrence_matrix, axis=1)

    """计算相关性"""
    correlation_value = 0.
    for i_row in range(len(prob_matrix)):
        for j_col in range(len(prob_matrix[0])):
            tmp = (i_row + 1 - row_mean) * (j_col + 1 -
                                            col_mean) * prob_matrix[i_row][j_col]
            tmp /= row_var * col_var
            correlation_value += tmp
    return correlation_value


def get_contrast(occurrence_matrix: np.ndarray) -> float:
    """给定共生矩阵，返回其对比度

    :param occurrence_matrix: numpy.array, 共生矩阵
    :return: float，对比度
    """
    prob_matrix = __get_probability_matrix(occurrence_matrix)

    contrast_value = 0.
    for i_row in range(len(occurrence_matrix)):
        for j_col in range(len(occurrence_matrix[0])):
            contrast_value += ((i_row + 1) - (j_col + 1)
                               ) ** 2 * prob_matrix[i_row][j_col]

    return contrast_value


def get_consistency(occurrence_matrix: np.ndarray) -> np.ndarray:
    """给定共生矩阵，返回一致性

    :param occurrence_matrix: numpy.array,共生矩阵
    :return: float,一致性
    """
    prob_matrix = __get_probability_matrix(occurrence_matrix)
    return np.sum(prob_matrix ** 2)


def get_homogeneity(occurrence_matrix: np.ndarray) -> float:
    """给定灰度共生矩阵，返回其同质性

    :param occurrence_matrix: numpy.array,灰度共生矩阵
    :return: float,  同质性
    """
    prob_matrix = __get_probability_matrix(occurrence_matrix)

    homogeneity_value = 0.
    for i_row in range(len(prob_matrix)):
        for j_col in range(len(prob_matrix[0])):
            tmp = prob_matrix[i_row][j_col] / \
                (1 + abs((i_row + 1) - (j_col + 1)))
            homogeneity_value += tmp
    return homogeneity_value


def get_entropy(occurrence_matrix: np.ndarray) -> float:
    """给定灰度共生矩阵，返回信息熵

    :param occurrence_matrix: numpy.array, 灰度共生矩阵
    :return: float,信息熵
    """
    prob_matrix = __get_probability_matrix(occurrence_matrix)
    tmp_log_matrix = np.log2(prob_matrix)
    '''替换计算熵时出现的无穷小'''
    tmp_log_matrix[tmp_log_matrix == -np.inf] = 0

    return - np.sum(prob_matrix * tmp_log_matrix)
