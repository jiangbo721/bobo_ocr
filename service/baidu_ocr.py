#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
百度图像识别基础服务
"""
from aip import AipFace, AipOcr, AipImageClassify

# 文字识别
char_APP_ID = "10683930"
char_API_KEY = "KWupRWsdl3zgmy01HBSgVqup"
char_SECRET_KEY = "hNVMDcsLnPenwyx4XGOa7v3ne8cdOvUy"
ocr = AipOcr(char_APP_ID, char_API_KEY, char_SECRET_KEY)

# 图像识别
image_APP_ID = "15066160"
image_API_KEY = "eIftSwlyrBcECm0T4hDlB3R5"
image_SECRET_KEY = "1Xq85wRk7YRl8M1nnm6xKqP7rzPf6PN4"
image = AipImageClassify(image_APP_ID, image_API_KEY, image_SECRET_KEY)

# 人脸识别
face_APP_ID = "15066160"
face_API_KEY = "eIftSwlyrBcECm0T4hDlB3R5"
face_SECRET_KEY = "1Xq85wRk7YRl8M1nnm6xKqP7rzPf6PN4"
face = AipFace(face_APP_ID, face_API_KEY, face_SECRET_KEY)