#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
百度图像识别基础服务
"""
from aip.imageclassify import AipImageClassify
from aip.ocr import AipOcr


APP_ID = "10683930"
API_KEY = "KWupRWsdl3zgmy01HBSgVqup"
SECRET_KEY = "hNVMDcsLnPenwyx4XGOa7v3ne8cdOvUy"

ocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

image = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
