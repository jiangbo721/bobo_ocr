#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文字识别处理服务
"""
import datetime
import json
import logging
import os
import uuid

from service.baidu_ocr import ocr
from service.base import BaseService
from service.defines import ID_CARD_SIDE

mine_logger = logging.getLogger('mine')


class CharacterService(BaseService):
    """
    文字识别服务
    """
    def __init__(self):
        super(CharacterService, self).__init__()
        self.UPLOAD_DIR_PATH = "/data/ocr/character"
        self.ocr = ocr

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

    def basic_accurate(self, image_content):
        """
        通用文字识别(高精度)
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
        mine_logger.warning("The image ocr character is : {}", json.dumps(result_list))
        return result_list

    def idcard(self, image_content, id_card_side=ID_CARD_SIDE.FRONT.code):
        """
        身份证识别
        :param str image_content: 图片二进制内容
        :param id_card_side: 身份证正反面
        :return dict: result 识别结果
        """
        # 获取识别结果
        baidu_result = self.ocr.idcard(image_content, id_card_side)
        print baidu_result
        # 保存图片
        self._image_save(image_content)

        # 解析结果
        result_list = []
        for word in baidu_result["words_result"]:
            result_list.append(word["words"])
        mine_logger.warning("The image ocr character is : {}", str(result_list))
        return result_list
