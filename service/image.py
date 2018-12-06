#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图像识别服务
"""
import logging

from service.baidu_ocr import image
from service.base import BaseService
from service.defines import RELIABILITY, IMAGE_RESULT_TITLE_PATTERN, IMAGE_RESULT_ITEM_PATTERN, PERCENT_RELIABILITY, \
    DISH_IMAGE_ITEM_PATTERN


class ImageService(BaseService):
    """
    图像识别处理服务
    """
    def __init__(self):
        super(ImageService, self).__init__()
        self.UPLOAD_DIR_PATH = "/data/ocr/image"
        self.image = image
        self.log = logging.getLogger('mine')

    def general_image(self, image_content):
        """
        通用物体识别
        :param str image_content: 图片二进制内容
        :return dict: result 识别结果
        """
        # 获取识别结果
        baidu_result = self.image.advancedGeneral(image_content)
        # 保存图片
        self._image_save(image_content)

        # 解析结果
        result_list = []
        result_num = baidu_result["result_num"]
        result_list.append(IMAGE_RESULT_TITLE_PATTERN.format(result_num, PERCENT_RELIABILITY))
        for index, item in enumerate(baidu_result['result'], 1):
            score = item["score"]
            if score >= RELIABILITY:
                root = item["root"]
                name = item["keyword"]
                result = IMAGE_RESULT_ITEM_PATTERN.format(index, name, root, str(score * 100) + "%")
                self.log.warning("The general_image word is: %s" % result)
                result_list.append(result)

        return result_list

    def dish_image(self, image_content):
        """
        菜品识别
        :param str image_content: 图片二进制内容
        :return dict: result 识别结果
        """
        # 获取识别结果
        baidu_result = self.image.dishDetect(image_content)
        # 保存图片
        self._image_save(image_content)

        # 解析结果
        result_list = []
        result_num = baidu_result["result_num"]
        result_list.append(IMAGE_RESULT_TITLE_PATTERN.format(result_num, PERCENT_RELIABILITY))
        for index, item in enumerate(baidu_result['result'], 1):
            probability = float(item["probability"])
            if probability >= RELIABILITY:
                name = item["name"]
                result = DISH_IMAGE_ITEM_PATTERN.format(index, name, str(probability * 100) + "%")
                if item["has_calorie"]:
                    result += ", 热量为{}KJ/100g。".format(item["calorie"])
                self.log.warning("The dish_image word is: %s" % result)
                result_list.append(result)

        return result_list
