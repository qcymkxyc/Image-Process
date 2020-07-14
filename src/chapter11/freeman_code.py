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
from deprecated.sphinx import deprecated

"""表示是按4方向编码还是按8方向编码"""
FOUR_DIRECTION = 1
EIGHT_DIRECTION = 2

# =========================================================
# 获取Freeman链码坐标
# =========================================================


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

# ===============================================================
# 获取边缘对应的Freeman链码坐标
# ===============================================================


def __get_close_num(num: float, num_list: [float]) -> (float, float):
    """给定一个数字以及一个有序的list，返回离该数字最近的两个数组中的元素

    :param num: float,该数字
    :param num_list: List[float],有序的list
    :return: Tuple(flaot,float),最近的两个元素
    """
    for i in range(len(num_list) - 1):
        current_num = num_list[i]
        next_num = num_list[i + 1]
        if current_num <= num <= next_num:
            return current_num, next_num


def __get_freeman_coordination(
        point: (int, int), freeman_x_list: list, freeman_y_list: list) -> (int, int):
    """给出当前点，放回该点在Freeman网格中的坐标

    :param point: (int,int), 点的坐标
    :param freeman_x_list: List[float], Freeman网格x
    :param freeman_y_list: List[float], Freeman网格y
    :return: (int,int) or None
        如果该点在Freeman网格线上则返回对应的Freeman网格坐标，否则返回None
    """
    x, y = point
    x_index, y_index = None, None
    """如果该点在网格的线上"""
    if x in freeman_x_list or y in freeman_y_list:
        try:
            x_index = freeman_x_list.index(x)
        except ValueError:
            '''如果该点在横线上'''
            last_freeman_x, next_freeman_x = __get_close_num(x, freeman_x_list)
            mean_freeman_x = (last_freeman_x + next_freeman_x) / 2
            x_index = freeman_x_list.index(last_freeman_x)
            x_index = x_index if x < mean_freeman_x else x_index + 1
            y_index = freeman_y_list.index(y)

            return x_index, y_index

        else:
            """如果该点在纵线上"""
            try:
                y_index = freeman_y_list.index(y)
            except ValueError:
                '''如果该点在纵线上'''
                last_freeman_y, next_freeman_y = __get_close_num(
                    y, freeman_y_list)
                mean_freeman_y = (last_freeman_y + next_freeman_y) / 2
                y_index = freeman_y_list.index(last_freeman_y)
                y_index = y_index if y < mean_freeman_y else y_index + 1
                x_index = freeman_x_list.index(x)
            else:
                '''如果该点刚好在Freeman编码的坐标点上'''
                x_index = freeman_x_list.index(x)
                y_index = freeman_y_list.index(y)
        finally:
            return x_index, y_index
    else:
        '''如果没有'''
        return


# ============================================================
# FreeMan编码
# ============================================================
@deprecated(version="1.0", reason="该函数判断不合理")
def __is_freeman_coordination_correct(
        freeman_coordination_list: [(int, int)]) -> bool:
    """验证Freeman链码是否正确

    如果下一个点和当前点仅差一个距离（即8个方向），则判定下一个点是正确的，否则判定下一个
    点是错误的

    :param freeman_coordination_list: List[(int,int)],得到的Freeman链码的List
    :return: bool,链码是否正确
    """
    for i in range(len(freeman_coordination_list) - 1):
        current_freeman_point = freeman_coordination_list[i]
        current_point_x, current_point_y = current_freeman_point
        next_freeman_point = freeman_coordination_list[i + 1]

        # 8个方向候选点(包括当前点),如果在候选点中得到超出范围的Freeman坐标点，不影响结果
        candidate_point_list = list()
        for x_direct_offset in [-1, 0, 1]:
            for y_direct_offset in [-1, 0, 1]:
                candidate_point_list.append(
                    (current_point_x + x_direct_offset,
                     current_point_y + y_direct_offset))
        if next_freeman_point not in candidate_point_list:
            # print(current_freeman_point, next_freeman_point)
            return False
    return True


def __get_freeman_code_by_two_point(
        point1: (int, int), point2: (int, int),) -> int:
    """给定两个点（Freeman点），返回Freeman编码

    :param point1: (int,int),点1
    :param point2: (int,int),点2
    :return: int， Freeman编码
    """
    freeman_code_dict = {
        str((1, 0)): 0,
        str((1, 1)): 1,
        str((0, 1)): 2,
        str((-1, 1)): 3,
        str((-1, 0)): 4,
        str((-1, -1)): 5,
        str((0, -1)): 6,
        str((1, -1)): 7,
    }
    point_gap = (point2[0] - point1[0], point2[1] - point1[1])
    try:
        return freeman_code_dict[str(point_gap)]
    except KeyError:
        return


def __get_freeman_code(freeman_coordination_list: [(int, int)]) -> [int]:
    """给定Freeman坐标，返回Freeman编码的结果

    :param freeman_coordination_list: List[(int,int)],Freman坐标组成的List
    :return: List[int],Freeman编码结果
    """
    freeman_code_list = list()
    for i in range(len(freeman_coordination_list) - 1):
        current_freeman_point = freeman_coordination_list[i]
        next_freeman_point = freeman_coordination_list[i + 1]

        freeman_code = __get_freeman_code_by_two_point(
            point1=current_freeman_point,
            point2=next_freeman_point)
        '''排除重复点 '''
        if freeman_code is not None:
            freeman_code_list.append(freeman_code)
    return freeman_code_list


# ============================================================
# 主函数
# ============================================================

def get_freeman_coordination(img: np.ndarray, contour: [(int, int)]) -> [int]:
    """给定图像和对应的边界，返回Freeman对应的坐标

    :param img: numpy.ndarray, 图像
    :param contour: List[(int,int)],边界的List
    :return: Freeman对应的坐标
    """
    freeman_coordination_list = list()  # 用于保存得出的Freeman链码坐标
    '''获取Freeman链码的网格坐标'''
    freeman_x_coordination_list, freeman_y_coordination_list = \
        __get_freeman_box_list(img=img)

    """得到边缘在Freeman链码上的坐标"""
    for point in contour:
        x, y = point
        point_freeman_coordination = __get_freeman_coordination(
            point=(x, y),
            freeman_x_list=freeman_x_coordination_list,
            freeman_y_list=freeman_y_coordination_list,
        )
        """如果该点在Freeman网格上"""
        if point_freeman_coordination is not None:
            freeman_coordination_list.append(point_freeman_coordination)

    '''添加最后一个点到第一个点的连线'''
    freeman_coordination_list.append(freeman_coordination_list[0])
    return freeman_coordination_list


def get_freeman_code(img: np.ndarray, contour: [
                     (int, int)]) -> [int]:
    """给定图像和对应的边界，返回Freeman链码

    :param img: numpy.ndarray,  图像
    :param contour: List[(int,int)],边界的list
    :return: [int], 弗雷曼链码
    """
    freeman_coordination_list = get_freeman_coordination(img, contour)
    """验证得到的Freeman坐标是否正确"""
    assert __is_freeman_coordination_correct(freeman_coordination_list)

    """根据方向得到Freeman链码"""
    return __get_freeman_code(freeman_coordination_list)
