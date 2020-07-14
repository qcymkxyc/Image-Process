#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3
"""
@Time    : 2020/7/14 15:22
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : t.py
@Title   : 
@Description    :  
"""
import numpy as np
import pickle

# d = np.load("diff_people_same_name__data.npy")

with open("diff_people_same_name__data.pkl","rb") as f:
    d = pickle.load(f)
print(len(d))