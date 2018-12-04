#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文字识别处理服务
"""
import datetime
import logging
import os
import uuid


class BaseService(object):
    """
    基础服务
    """
    def __init__(self):
        self.UPLOAD_DIR_PATH = "/data/ocr"
        self.log = logging.getLogger('mine')

    @property
    def _unique_name(self):
        """
        生成唯一文件名
        """
        return str(uuid.uuid4()).replace("-", "")

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
