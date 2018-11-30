#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图像识别处理服务
"""
import datetime
import logging
import os
import uuid

from service.baidu_ocr import image
from service.base import BaseService
from service.defines import RELIABILITY, IMAGE_RESULT_TITLE_PATTERN, IMAGE_RESULT_ITEM_PATTERN, PERCENT_RELIABILITY


class ImageService(BaseService):
    """
    图像识别处理服务
    """
    def __init__(self):
        super(ImageService, self).__init__()
        self.UPLOAD_DIR_PATH = "/data/ocr/image"
        self.image = image

    @property
    def _unique_name(self):
        """
        生成唯一文件名
        """
        return str(uuid.uuid4()).replace("-", "")

    def parse_image(self, image_content):
        """
        图片上传
        :param str image_content: 图片二进制内容
        :return dict: result 识别结果
        """
        logging.warning("进入图像识别接口service")
        # 获取识别结果
        baidu_result = self.image.advancedGeneral(image_content)
        print baidu_result
        # 保存图片
        self._image_save(image_content)

        # 解析结果
        result_list = []
        result_num = baidu_result["result_num"]
        result_list.append(IMAGE_RESULT_TITLE_PATTERN.format(result_num, PERCENT_RELIABILITY))
        for index, item in enumerate(baidu_result['result'], 1):
            score = item["score"]
            if score >= RELIABILITY:
                root = item["root"].encode("utf8")
                name = item["keyword"].encode("utf8")
                result_list.append(IMAGE_RESULT_ITEM_PATTERN.format(
                    index, name, root, str(score * 100) + "%"))

        return result_list

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
