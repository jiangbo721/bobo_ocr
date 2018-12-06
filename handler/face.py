#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
人脸识别接口
"""
import logging

from handler.base import BaseHandler
from service.face import FaceService


mine_logger = logging.getLogger('mine')


class FaceHandler(BaseHandler):
    """
    图像识别接口
    """
    def get(self, module):
        """
        图片上传
        """
        self.finish('please post')

    def detection(self):
        """
        通用物体识别
        """
        mine_logger.warning("进入人脸识别接口handler")
        image = self.request.files.get("image")
        image_type = self.get_argument("image_type", "BASE64")
        if not image:
            self.finish("对不起，未检测到您上传的图片")
        image_content = image[0]["body"]

        data = FaceService().detection(image_content, image_type)

        self.render("image/ocr_result.html", data=data)
