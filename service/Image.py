#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
面单图片识别处理服务
"""
import hashlib
from aip.ocr import AipOcr

class ImageService(object):
    """
    图片识别处理服务
    """
    def __init__(self):
        self.ocr = AipOcr("10683930",
                          "KWupRWsdl3zgmy01HBSgVqup",
                          "hNVMDcsLnPenwyx4XGOa7v3ne8cdOvUy"
                          )

    def image_upload(self, image_content):
        """
        图片上传
        :param str image_content: 图片二进制内容
        :return tuple: (code, None)
        """
        # 获取识别结果
        baidu_result = self.ocr.basicAccurate(image_content)

        # 保存图片
        self._image_save(image_content)

        return baidu_result

    def _image_save(self, image_content):
        """
        保存图片
        :param image_content:
        :return str: 图片路径
        """
        digest = hashlib.md5(image_content).hexdigest()
        file_path = "/home/jlb/桌面/%s%s" % (digest, ".jpg")

        with open(file_path, "wb") as image_fd:
            image_fd.write(image_content)

        return file_path
