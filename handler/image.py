#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图像识别接口
"""
import logging

from handler.base import BaseHandler
from service.image import ImageService


mine_logger = logging.getLogger('mine')


class ImageHandler(BaseHandler):
    """
    图像识别接口
    """
    def get(self, module):
        """
        图片上传
        """
        self.finish('please post')

    def post(self, module):
        """
        图片上传
        """
        mine_logger.warning("进入图像识别接口handler")
        image = self.request.files.get("image")
        if not image:
            self.finish("对不起，未检测到您上传的图片")
        image_content = image[0]["body"]

        data = ImageService().parse_image(image_content)

        self.render("image/ocr_result.html", data=data)
