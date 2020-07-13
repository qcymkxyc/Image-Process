#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/4/28 11:13
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : mat.py
@Title   : MAT算法
@Description    :
    MAT算法用于给定一个字的图片，通过MAT算法返回这个字对应的骨架图片
"""
import numpy as np
from functools import reduce


# =================================================================
# MAT算法提取骨架
# =================================================================


def __mat_process_first(around_area: np.ndarray) -> bool:
    """MAT算法步骤1

    对于相邻像素区域：
    [
        [p9,p2,p3],
        [p8,p1,p4],
        [p7,p6,p5]
    ]
    包括以下几个部分：
    a. 2 <=非零像素个数 <= 6
    b. 顺时针跳数 = 1
    c. p2 * p4 * p6 = 0
    d. p4 * p6 * p8 = 0

    :param around_area: numpy.array, 一个像素的相邻像素，为3*3
    :return: bool，是否满足以上所有条件
    """
    result_list = list()    # 保存所有步骤是否符合条件
    """步骤a"""
    near_one_count = __near_pix_equal_one_count(around_area)
    result_list.append(2 <= near_one_count <= 6)
    """步骤b"""
    result_list.append(__binary_transform_count(around_area) == 1)
    """步骤c"""
    pix_2 = around_area[0][1]
    pix_4 = around_area[1][2]
    pix_6 = around_area[2][1]
    result_list.append(pix_2 * pix_4 * pix_6 == 0)
    """步骤d"""
    pix_8 = around_area[1][0]
    result_list.append(pix_4 * pix_6 * pix_8 == 0)

    return bool(reduce(lambda x, y: x and y, result_list))


def __mat_process_second(around_area: np.ndarray) -> bool:
    """MAT算法步骤2
    对于相邻像素区域：
    [
        [p9,p2,p3],
        [p8,p1,p4],
        [p7,p6,p5]
    ]
    包括以下几个部分：
    a. 2 <=非零像素个数 <= 6
    b. 顺时针跳数 = 1
    c. p2 * p4 * p8 = 0
    d. p2 * p6 * p8 = 0
    :param around_area: numpy.array, 周围的区域
    :return: bool,是否全部子条件
    """
    result_list = list()    # 保存所有步骤是否符合条件
    """步骤a"""
    near_one_count = __near_pix_equal_one_count(around_area)
    result_list.append(2 <= near_one_count <= 6)
    """步骤b"""
    result_list.append(__binary_transform_count(around_area) == 1)
    """步骤c"""
    pix_2 = around_area[0][1]
    pix_4 = around_area[1][2]
    pix_8 = around_area[1][0]
    pix_6 = around_area[2][1]
    result_list.append(pix_2 * pix_4 * pix_8 == 0)
    """步骤d"""
    result_list.append(pix_2 * pix_6 * pix_8 == 0)

    return bool(reduce(lambda x, y: x and y, result_list))


def __near_pix_equal_one_count(around_area: np.ndarray) -> int or np.int:
    """计算相邻像素中为1的个数(不包括中间点)

    即，对于相邻像素区域：
    [
        [p9,p2,p3],
        [p8,p1,p4],
        [p7,p6,p5]
    ]
    统计出p1之外所有的1的个数
    :param around_area: numpy.array, 一个像素的相邻像素，为3*3
    :return int,像素为1的个数
    """
    temp_around_area = np.copy(around_area)
    temp_around_area[1][1] = 0
    return int(np.sum(temp_around_area, dtype=np.int))


def __binary_transform_count(around_area: np.ndarray) -> int or np.int:
    """给定一个3*3的二进制图片，获取其顺时针的跳数（从0到1）

    即，对于相邻像素区域：
    [
        [p9,p2,p3],
        [p8,p1,p4],
        [p7,p6,p5]
    ]
    以p9,p2,p3,p4,p5,p6,p7,p8的顺序访问，如果是0到1，则为一跳
    :param around_area: numpy.array, 一个像素的相邻像素，为3*3
    :return int, 顺时针跳数
    """
    def __next_index(current_coor: (int, int)) -> (int, int):
        """给定当前位置，返回下一个位置

        :param current_coor: (int,int),当前位置
        :return: (int,int), 下一个位置
        """
        '''四个方向的下一个位置'''
        right_next = (current_coor[0], current_coor[1] + 1)
        down_next = (current_coor[0] + 1, current_coor[1])
        left_next = (current_coor[0], current_coor[1] - 1)
        up_next = (current_coor[0] - 1, current_coor[1])

        """按照指定的规则寻找，不报错则表示正确的方向"""
        next_coordinate_list = [right_next, down_next, left_next, up_next]
        for i, next_coordinate in enumerate(next_coordinate_list):
            try:
                around_area[next_coordinate]
            except IndexError:
                continue
            else:
                '''如果该点已经走过'''
                if is_walked[next_coordinate[0], next_coordinate[1]]:
                    continue
                else:
                    is_walked[next_coordinate[0], next_coordinate[1]] = True
                    return next_coordinate

    is_walked = np.full_like(around_area, False)  # 用于标识该点是否已经走过
    is_walked[1][1] = True
    transform_count = 0  # 用于记录跳数
    """循环对比"""
    last_pix = around_area[0][0]  # 上一个的值
    current_coordinate = (0, 1)
    while current_coordinate != (0, 0):
        current_pix = around_area[current_coordinate[0], current_coordinate[1]]
        if last_pix == 0 and current_pix == 1:
            transform_count += 1

        last_pix = current_pix
        current_coordinate = __next_index(current_coordinate)

    '''当循环到第一个点时再对比一次'''
    current_pix = around_area[current_coordinate[0], current_coordinate[0]]
    if last_pix == 0 and current_pix == 1:
        transform_count += 1

    return transform_count


def __remove_pix_by_coordination(img: np.ndarray, points: list):
    """给定坐标的list，删除图像上的点（实际就是标记为0）

    :param img: numpy.array,图像
    :param points: List[(int,int)]
    """
    for single_coordination in points:
        i_row, i_col = single_coordination
        img[i_row][i_col] = 0


def __get_remove_points(img: np.ndarray, func) -> [(int, int)]:
    """给定图像以及，删除点的规则，返回要删除的点

    :param img: numpy.array, 原图像
    :param func: function, 规则，也就是一个函数
    :return: List[（int,int）],坐标的list
    """
    remove_points_list = list()
    temp_img = img
    img_iter = np.nditer(temp_img, flags=["multi_index"])
    while not img_iter.finished:
        current_pix = img_iter[0]
        i_row, i_col = img_iter.multi_index
        img_iter.iternext()
        '''如果是背景点则直接跳过'''
        if current_pix != 1:
            continue

        """如果是前景点"""
        around_area = temp_img[i_row - 1:i_row + 2, i_col - 1:i_col + 2]
        if func(around_area):
            remove_points_list.append((i_row, i_col))

        img_iter.iternext()
    return remove_points_list


def get_img_skeleton_by_mat(img: np.ndarray) -> np.ndarray:
    """根据字体的图像得到字的骨架

    :param img, numpy.array, 原图片
    :raise ValueError
        - 图片不为单通道
        - 图片并未归一化
        - 图片并未标准化
    :return: numpy.array, 骨架图
    """
    '''检验图片是否是单通道'''
    if len(img.shape) != 2:
        raise ValueError("该图片不是单通道")
    """检验标准化"""
    if img.max() > 1:
        raise ValueError("该图片并未标准化")
    """检验二值化"""
    if (np.unique(img.flatten()) != (0, 1)).all():
        raise ValueError("该函数并未二值化")

    temp_img = img.copy()
    """遍历每一个像素点"""
    is_remove_flag = True  # 表示是否继续删除的标志
    i_round = 1  # 记录迭代的轮数
    while is_remove_flag:
        is_remove_flag = False
        print("正在执行MAT算法的第{}轮".format(i_round))
        """执行步骤1"""
        remove_points = __get_remove_points(temp_img, __mat_process_first)
        if len(remove_points) != 0:
            is_remove_flag = True
            __remove_pix_by_coordination(temp_img, remove_points)

        """执行步骤2"""
        remove_points = __get_remove_points(temp_img, __mat_process_second)
        if len(remove_points) != 0:
            is_remove_flag = True
            __remove_pix_by_coordination(temp_img, remove_points)

        i_round += 1

    return temp_img
