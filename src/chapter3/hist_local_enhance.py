#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2021/5/21 15:34
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : hist_local_enhance.py
@Title   : 局部直方图增强
@Description    :  
"""
import numpy as np


def get_dead_area(img:np.ndarray,local_size = 3,k0 = 0.,k1 = ):
    """返回暗色区域"""
    local_part_size = np.floor(local_size / 2.)
    for i,row in enumerate(img):
        for j,pix in enumerate(row):
            start_i = i - local_part_size
            end_i = i + local_part_size
            start_j = j - local_part_size
            end_j = j + local_part_size

            local_mean = np.mean(img[start_i:end_i,start_j:end_j].flatten())
            local_std = np.std(img[start_i:end_i,start_j:end_j].flatten())

            # TODO 比较local和global






def local_enhance(img:np.ndarray,local_size = 3):
    """"""
    """全局均值和标准差"""
    global_mean = np.mean(img.flatten())
    global_mean_std = np.std(img.flatten())

    """"""
    for
