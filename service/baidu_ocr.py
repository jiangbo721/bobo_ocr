#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
百度图像识别基础服务
"""
from aip.imageclassify import AipImageClassify
from aip.ocr import AipOcr

ocr = AipOcr(
    "10683930",
    "KWupRWsdl3zgmy01HBSgVqup",
    "hNVMDcsLnPenwyx4XGOa7v3ne8cdOvUy"
)

image = AipImageClassify(
    "10683930",
    "KWupRWsdl3zgmy01HBSgVqup",
    "hNVMDcsLnPenwyx4XGOa7v3ne8cdOvUy"
)