#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/5/11 17:35
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : font_img_skeleton_feature.py
@Title   : 字体骨架图片的特征
@Description    :  
"""
import preprocess.neaten_data
from algorithm.image import mat
import copy
import numpy as np
from util import decorators
from util import image_helper
import pandas as pd
from util.show_helper import draw_img
from config import font_shape_model_config
from util import data_helper


@decorators.func_input_type_check()
@decorators.func_output_type_check()
def get_font_skeleton_by_img(img: np.ndarray) ->np.ndarray:
    """给定一个字体图片，返回该字体的骨架

    :param img: numpy.ndarray, 字体图片
    :return: numpy.ndarray, 骨架图片
    """
    '''二值化图片,并且统一为黑底白字'''
    binary_img = image_helper.font_img_binary_and_black_ground(img)
    '''标准化图片'''
    norm_img = image_helper.font_img_normalization(binary_img)
    '''骨架化后的图片'''
    stroke_img = mat.get_img_skeleton_by_mat(norm_img)
    return stroke_img


@decorators.func_output_type_check()
@decorators.func_input_type_check()
def get_font_skeleton_by_seq(signature_data: pd.DataFrame) -> np.ndarray:
    """给定一个签字序列，返回该签字序列的骨架（实际上是不加粗细的绘图）

    :param signature_data: pandas.DataFrame,
    :return: numpy.ndarray, 骨架图片
    """
    try:
        img = draw_img(
            data=signature_data,
            is_resize=True,
            size=font_shape_model_config.resize_img_shape
        )
    except KeyError:
        '''列名错误的情况'''
        temp_data = signature_data.copy()
        temp_data.columns = preprocess.neaten_data.replace_columns(temp_data.columns, 2)
        img = draw_img(
            data=temp_data,
            is_resize=True,
            size=font_shape_model_config.resize_img_shape
        )
    finally:
        img = img.resize(font_shape_model_config.resize_img_shape)
        img = np.asarray(img)
        """二值化图片,并且统一为黑底白字"""
        binary_img = image_helper.font_img_binary(img)
        '''转换为黑底白字'''
        # binary_img = 255 - binary_img
        '''标准化图片'''
        norm_img = image_helper.font_img_normalization(binary_img)

    return norm_img
