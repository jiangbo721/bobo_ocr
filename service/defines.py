#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图像识别通用定义
"""
RELIABILITY = 0.26
PERCENT_RELIABILITY = str(RELIABILITY * 100) + "%"
IMAGE_RESULT_TITLE_PATTERN = "您有{}种可能的结果，但我们把可信度大于{}的几个给您展示出来："
IMAGE_RESULT_ITEM_PATTERN = "您的第{}种结果为： {}, 类别为： {}, 可信度是： {}"