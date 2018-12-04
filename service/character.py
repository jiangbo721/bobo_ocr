#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文字识别处理服务
"""
import json
import logging

from service.baidu_ocr import ocr
from service.base import BaseService
from service.defines import ID_CARD_SIDE


class CharacterService(BaseService):
    """
    文字识别服务
    """
    def __init__(self):
        super(CharacterService, self).__init__()
        self.UPLOAD_DIR_PATH = "/data/ocr/character"
        self.ocr = ocr
        self.log = logging.getLogger('mine')

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
            self.log.warning("The basic_accurate word is: %s" % word["words"])
            result_list.append(word["words"])
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
        # mine_logger.warning("The image ocr character is : {}".format(json.dumps(baidu_result)))
        self.log.warning(json.dumps(baidu_result))

        # 保存图片
        self._image_save(image_content)

        # 解析结果
        result_list = []
        for word in baidu_result["words_result"]:
            result_list.append(word)
        return result_list
