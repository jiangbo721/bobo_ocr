#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图像识别处理服务
"""
import json
import logging

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
        self.log = logging.getLogger('mine')

    def parse_image(self, image_content):
        """
        图片上传
        :param str image_content: 图片二进制内容
        :return dict: result 识别结果
        """
        self.log.warning("进入图像识别接口service")
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
                root = item["root"].encode("utf8")
                name = item["keyword"].encode("utf8")
                result = IMAGE_RESULT_ITEM_PATTERN.format(index, name, root, str(score * 100) + "%")
                self.log.warning("The advancedGeneral word is: %s" % result)
                result_list.append(result)

        return result_list
