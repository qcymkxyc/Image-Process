#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2021/1/29 9:32
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : frequency_domain.py
@Title   :
@Description    :
"""
import numpy as np


def __get_filter(image, d_0: int = 80, high: float = 1.5,
                 low: float = 0.25, c: int = 1):
    """返回同态滤波的滤波器
    :param d_0: int, 参数
    :param high: float: 参数
    :param low: float, 参数
    :param c: int, 参数
    :return np.array, 滤波器
    """
    h, w = image.shape
    u, v = np.meshgrid(np.arange(w), np.arange(h))
    median_u, median_v = np.floor(w / 2), np.floor(h / 2)

    u = u - median_u
    v = v - median_v
    dist_matrix = u**2 + v**2

    tmp = 1 - np.exp(-c * dist_matrix / (d_0**2))
    return (high - low) * tmp + low


def homomorphic_filtering(image: np.ndarray) -> np.ndarray:
    """同态滤波"""
    """时域转频域"""
    log_image = np.log1p(image)
    fft_image = np.fft.fft2(log_image)
    fft_image = np.fft.fftshift(fft_image)

    """滤波"""
    h_matrix = __get_filter(fft_image)
    fft_image = fft_image * h_matrix

    """频域转时域"""
    fft_image = np.fft.ifftshift(fft_image)
    tmp_image = np.fft.ifft2(fft_image)
    return np.exp(tmp_image).real
