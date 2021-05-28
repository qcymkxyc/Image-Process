#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2021/5/24 15:39
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : edge_connect.py
@Title   : 边界连接
@Description    :  
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2


def connect_gap(binary_matrix:np.ndarray,gap_length:int):
    """连接缝隙"""
    for i,row in enumerate(binary_matrix):
        last_1_index = - np.inf
        for j,pix in enumerate(row):
            if pix != 0:
                """填充缝隙"""
                if j - last_1_index < gap_length:
                    binary_matrix[i][last_1_index + 1:j + 1] = 1
                last_1_index = j
    return binary_matrix


def _check_binary_matrix(gradient_value_matrix:np.ndarray,
                         gradient_angel_matrix:np.ndarray,
                         gradient_value_threshold:float,
                         gradient_angle_threshold:float,
                         gradient_angle_bandwidth:float):
    """条件二值化"""
    tmp1 = gradient_value_matrix > gradient_value_threshold
    tmp2 = gradient_angel_matrix == (gradient_angle_threshold - gradient_angle_bandwidth)
    tmp3 = gradient_angel_matrix == (gradient_angle_threshold + gradient_angle_bandwidth)
    matrix = np.logical_and(tmp1,np.logical_or(tmp2,tmp3))

    matrix = matrix.astype(int)
    return matrix


def _horizontal_connect(img: np.ndarray,
                  gradient_angle_threshold:float,
                  gradient_angle_bandwidth:float,
                  gradient_value_threshold_rate:float, ) -> np.ndarray:
    img_diff_x = cv2.Sobel(img, -1, 1, 0)
    img_diff_y = cv2.Sobel(img, -1, 0, 1)

    # TODO 角度有nan出现
    gradient_value = np.sqrt(img_diff_x ** 2 + img_diff_y ** 2)
    gradient_angle = np.rad2deg(np.arctan(img_diff_y / img_diff_x))

    """计算梯度的阈值"""
    gradient_value_threshold = np.max(gradient_value) * gradient_value_threshold_rate

    """判断"""
    matrix = _check_binary_matrix(
        gradient_angel_matrix=gradient_angle,
        gradient_value_matrix=gradient_value,
        gradient_value_threshold=gradient_value_threshold,
        gradient_angle_bandwidth=gradient_angle_bandwidth,
        gradient_angle_threshold=gradient_angle_threshold,)

    """缝隙连接"""
    matrix = connect_gap(binary_matrix=matrix, gap_length=50)

    plt.imshow(img)
    plt.title("img")
    plt.show()

    tmp = np.logical_or(matrix,img)
    tmp = tmp.astype(int)
    plt.imshow(tmp)
    plt.title("t")
    plt.show()


    # return tmp * img
    return matrix + img


def local_connect(img: np.ndarray,
                  gradient_angle_threshold:float,
                  gradient_angle_bandwidth:float,
                  gradient_value_threshold_rate:float, ) -> np.ndarray:
    """"""
    res_img = _horizontal_connect(img,
                                  gradient_angle_threshold,
                                  gradient_angle_bandwidth,
                                  gradient_value_threshold_rate)

    import matplotlib.pyplot as plt
    plt.imshow(res_img)
    plt.show()

    res_img = cv2.rotate(res_img,cv2.ROTATE_90_COUNTERCLOCKWISE)
    res_img = res_img.astype("uint8")
    res_img = _horizontal_connect(res_img,
                                  gradient_angle_threshold,
                                  gradient_angle_bandwidth,
                                  gradient_value_threshold_rate)
    res_img = cv2.rotate(res_img,cv2.ROTATE_90_CLOCKWISE)

    return res_img
