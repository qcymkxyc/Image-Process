# Image-Process
闲暇之余对《数字图像处理》的实现，欢迎Star

------

冈萨雷斯《数字图像处理》Python实现（第三版）

个人技术博客：http://www.zhangqi2019.top/

**本书预览地址：http://www.ailearndo.com/resource/数字图像处理(冈萨雷斯版).pdf**

## 第3章 灰度变换与空间滤波

|                | 实现代码 | Demo                                                         | 算法说明 |
| -------------- | -------- | ------------------------------------------------------------ | -------- |
| 局部直方图均衡 |          | [局部直方图均衡](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E9%A2%91%E7%8E%87%E5%9F%9F%E6%BB%A4%E6%B3%A2.ipynb#图像重取样) |          |
|                |          |                                                              |          |



## 第4章 频率域滤波

|              | 实现代码 | Demo                                                         | 算法说明 |
| ------------ | -------- | ------------------------------------------------------------ | -------- |
| 图像重取样   |          | [图像重取样](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E9%A2%91%E7%8E%87%E5%9F%9F%E6%BB%A4%E6%B3%A2.ipynb#图像重取样) |          |
| 傅里叶谱     |          | [傅里叶谱](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E9%A2%91%E7%8E%87%E5%9F%9F%E6%BB%A4%E6%B3%A2.ipynb#傅里叶谱) |          |
| 直通分量置零 |          | [直通分量置零](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E9%A2%91%E7%8E%87%E5%9F%9F%E6%BB%A4%E6%B3%A2.ipynb#直流分量置0) |          |
| 同态滤波  |[同态滤波](src/chapter4/frequency_dommain.py)| | |



## 第9章 形态学

以下形态学的Demo说明见：http://www.zhangqi2019.top/posts/c1f4dbab.html/

实现包括以下内容：

|                       | 实现代码                                   | Demo                                                         | 算法说明                                                     |
| --------------------- | ------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 腐蚀                  |                                            | [腐蚀](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#腐蚀) | [腐蚀](https://www.zhangqi2019.top/posts/c1f4dbab.html/#腐蚀) |
| 膨胀                  |                                            | [膨胀](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#膨胀) | [膨胀](https://www.zhangqi2019.top/posts/c1f4dbab.html/#膨胀) |
| 开操作                |                                            | [开操作](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#开操作和闭操作) | [开操作](https://www.zhangqi2019.top/posts/c1f4dbab.html/#开操作和闭操作) |
| 闭操作                |                                            | [闭操作](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#开操作和闭操作) | [闭操作](https://www.zhangqi2019.top/posts/c1f4dbab.html/#开操作和闭操作) |
| 击中以及不击中        | [击中和不击中](src/chapter9/morphology.py) | [击中以及不击中](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#击中和不击中) | [击中以及不击中](https://www.zhangqi2019.top/posts/c1f4dbab.html/#击中以及不击中) |
| 边界提取              |                                            | [边界提取](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#边界提取) | [边界提取](https://www.zhangqi2019.top/posts/c1f4dbab.html/#边界提取) |
| 连通分量提取          | [连通分量提取](src/chapter9/morphology.py) | [连通分量提取](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#连通分量提取) | [连通分量提取](https://www.zhangqi2019.top/posts/c1f4dbab.html/#连通分量提取) |
| 孔洞填充              | [孔洞填充](src/chapter9/morphology.py)     | [孔洞填充](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#孔洞填充) | [孔洞填充](https://www.zhangqi2019.top/posts/c1f4dbab.html/#孔洞填充) |
| 形态学重建-重建开操作 | [重建开操作](src/chapter9/morphology.py)   | [形态学重建 -重建开操作](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#重建开操作) | [重建开操作](https://www.zhangqi2019.top/posts/c1f4dbab.html/#重建开操作) |
| 灰度形态学-灰度腐蚀   |                                            | [灰度级形态学- 灰度腐蚀](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#灰度腐蚀) | [灰度腐蚀](https://www.zhangqi2019.top/posts/c1f4dbab.html/#灰度腐蚀) |
| 灰度形态学-灰度膨胀   |                                            | [灰度级形态学-灰度膨胀](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#灰度膨胀) | [灰度膨胀](https://www.zhangqi2019.top/posts/c1f4dbab.html/#灰度膨胀) |
| 灰度形态学-灰度开操作 |                                            | [灰度级形态学-灰度开操作](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#灰度开操作) | [灰度开操作和闭操作](https://www.zhangqi2019.top/posts/c1f4dbab.html/#灰度开操作和闭操作) |
| 灰度形态学-灰度闭操作 |                                            | [灰度级形态学-灰度闭操作](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#灰度闭操作) | [灰度开操作和闭操作](https://www.zhangqi2019.top/posts/c1f4dbab.html/#灰度开操作和闭操作) |
| 形态学梯度            |                                            | [形态学梯度](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#形态学梯度) | [形态学梯度](https://www.zhangqi2019.top/posts/c1f4dbab.html/#形态学梯度) |
| 顶帽操作              |                                            | [顶帽操作](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#顶帽操作) | [顶帽和底帽变换](https://www.zhangqi2019.top/posts/c1f4dbab.html/#顶帽和底帽变换) |
| 形态学纹理分割        |                                            | [形态学纹理分割](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%BD%A2%E6%80%81%E5%AD%A6.ipynb#形态学纹理分割) | [纹理分割](https://www.zhangqi2019.top/posts/c1f4dbab.html/#纹理分割) |

##  第10章 图像分割

|                           | 实现源码 | Demo                                                         | 算法说明                                                     |
| ------------------------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 孤立点检测                |          | [孤立点检测](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2.ipynb) | [孤立点检测](https://www.zhangqi2019.top/posts/d2113c07.html/#孤立点检测) |
| 线检测                    |          | [孤立点检测](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2.ipynb) | [线检测](https://www.zhangqi2019.top/posts/d2113c07.html/#线检测) |
| 简单边缘模型（Sobel检测） |          | [Sobel边缘检测](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2.ipynb#基本检测模型(Sobel)) | [Sobel边缘检测](https://www.zhangqi2019.top/posts/d2113c07.html/#基本的检测模型) |



## 第11章 表示和描述

Demo汇总: [Demo汇总](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/图像表示与描述.ipynb)

本章算法说明汇总:https://www.zhangqi2019.top/posts/d4747641.html/

算法实现包括以下：

|                       | 实现源码                                         | Demo                                                         | 算法说明                                                     |
| --------------------- | ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Moore边界追踪         |                                                  |                                                              | [Moore说明](https://www.zhangqi2019.top/posts/d4747641.html/#%E8%BE%B9%E7%95%8C%E8%BF%BD%E8%B8%AA%EF%BC%88Moore%E8%BE%B9%E7%95%8C%E8%BF%BD%E8%B8%AA%EF%BC%89) |
| Freeman链码           | [Freeman实现代码](src/chapter11/freeman_code.py) | [Freeman链码Demo](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%8F%8F%E8%BF%B0.ipynb#Freeman链码) | [Freeman链码](https://www.zhangqi2019.top/posts/d4747641.html/#%E9%93%BE%E7%A0%81) |
| 标记图                | [标记图实现代码](src/chapter11/mark_sheet.py)    | [标记图Demo](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%8F%8F%E8%BF%B0.ipynb#标记图) | [标记图](https://www.zhangqi2019.top/posts/d4747641.html/#%E9%93%BE%E7%A0%81) |
| 骨架算法              | [骨架算法实现代码](src/chapter11/mat.py)         | [骨架算法Demo](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%8F%8F%E8%BF%B0.ipynb#骨架) | [骨架](https://www.zhangqi2019.top/posts/d4747641.html/#%E9%AA%A8%E6%9E%B6) |
| 形状数                | [形状数实现](src/chapter11/shape_number.py)      | [形状数Demo](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%8F%8F%E8%BF%B0.ipynb#形状数) | [形状数](https://www.zhangqi2019.top/posts/d4747641.html/#%E5%BD%A2%E7%8A%B6%E6%95%B0) |
| 灰度共生矩阵          | [灰度共生矩阵](src/chapter11/texture.py)         | [灰度共生矩阵Demo](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%8F%8F%E8%BF%B0.ipynb#灰度共生矩阵) |                                                              |
| 灰度共生矩阵描述子    | [灰度共生矩阵描述子](src/chapter11/texture.py)   | [灰度共生矩阵描述子Demo](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%8F%8F%E8%BF%B0.ipynb#灰度共生矩阵描述子) |                                                              |
| $n$步共生矩阵相关系数 | [n步共生矩阵相关系数](src/chapter11/texture.py)  | [灰度共生矩阵描述子Demo](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%8F%8F%E8%BF%B0.ipynb#n跳共生矩阵组成的序列图像) |                                                              |
| 不变矩                | [不变矩](src/chapter11/moment_invariants.py)     | [不变矩Demo](https://nbviewer.jupyter.org/github/qcymkxyc/Image-Process/blob/master/notebooks/%E5%9B%BE%E5%83%8F%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%8F%8F%E8%BF%B0.ipynb#不变矩) |                                                              |

