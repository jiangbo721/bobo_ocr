#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
面单图片识别处理服务
"""
import datetime
import os
import uuid

from aip.ocr import AipOcr

class ImageService(object):
    """
    图片识别处理服务
    """
    def __init__(self):
        self.UPLOAD_DIR_PATH = "/home/jlb/桌面"
        self.ocr = AipOcr("10683930",
                          "KWupRWsdl3zgmy01HBSgVqup",
                          "hNVMDcsLnPenwyx4XGOa7v3ne8cdOvUy"
                          )

    @property
    def _unique_name(self):
        """
        生成唯一文件名
        """
        return str(uuid.uuid4()).replace("-", "")

    def image_upload(self, image_content):
        """
        图片上传
        :param str image_content: 图片二进制内容
        :return dict: result 识别结果
        """
        # 获取识别结果
        baidu_result = self.ocr.basicAccurate(image_content)

        # 保存图片
        self._image_save(image_content)

        # 解析结果
        result_list = []
        for word in baidu_result["words_result"]:
            result_list.append(word["words"])
        result_str = "\n".join(result_list)

        return result_str

    def _image_save(self, image_content):
        """
        保存图片
        :param image_content:
        :return str: 图片路径
        """
        # 创建文件路径
        dir_path = os.path.join(self.UPLOAD_DIR_PATH, datetime.datetime.now().strftime("%Y%m%d"))
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, self._unique_name + ".jpg")

        # 保存图片
        with open(file_path, "wb") as image_fd:
            image_fd.write(image_content)

        return file_path
