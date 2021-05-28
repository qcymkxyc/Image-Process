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


def _location_transform(c_position: int, total: int) -> int:
    """位置转换，返回正确位置"""
    if c_position < 0:
        return 0
    elif c_position > total:
        return total - 1
    else:
        return c_position


def _is_shadow(local_mean, local_std, global_mean, global_std, k0, k1, k2):
    """检测是否是阴影"""
    tmp1 = local_mean < k0 * global_mean
    tmp2 = (global_std * k1 <= local_std <= global_std * k2)
    return tmp1 and tmp2


def get_dead_area(img: np.ndarray, local_size=3, k0=0.4, k1=0.02, k2=0.4):
    """返回暗色区域"""
    """全局均值和标准差"""
    global_mean = np.mean(img.flatten())
    global_std = np.std(img.flatten())

    """"""
    shadow_matrix = np.zeros_like(img)

    """比较"""
    h, w, _ = img.shape
    local_part_size = np.floor(local_size / 2.)
    local_part_size = local_part_size.astype(int)
    for i, row in enumerate(img):
        for j, pix in enumerate(row):
            """局部位置坐标"""
            start_i = _location_transform(i - local_part_size, h)
            end_i = _location_transform(i + local_part_size, h)
            start_j = _location_transform(j - local_part_size, w)
            end_j = _location_transform(j + local_part_size, w)

            """局部位置统计数据"""
            local_mean = np.mean(img[start_i:end_i, start_j:end_j].flatten())
            local_std = np.std(img[start_i:end_i, start_j:end_j].flatten())

            """"""
            shadow_matrix[i][j] = _is_shadow(
                local_mean, local_std, global_mean, global_std, k0, k1, k2)
    return shadow_matrix


def local_enhance(img: np.ndarray, local_size=3, k0=0.4, k1=0.02, k2=0.4):
    """"""
    """获取暗色区域"""
    shadow_matrix = get_dead_area(img, local_size, k0, k1, k2)

    """暗色增强"""
    tmp1 = img * shadow_matrix * 3
    tmp2 = np.logical_not(shadow_matrix)
    tmp2 = tmp2.astype(int)
    tmp2 = img * tmp2

    return tmp1 + tmp2
