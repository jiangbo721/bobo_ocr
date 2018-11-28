#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
面单识别图片接口
"""
import tornado.web

from service.Image import ImageService


class ImageHandler(tornado.web.RequestHandler):
    """
    识别图片接口
    """
    def get(self):
        """
        图片上传
        """
        self.finish('please post')

        image = self.request.files.get("image")
        image_content = image[0]["body"]

        data = ImageService().image_upload(image_content)

        self.finish(data)

    def post(self):
        """
        图片上传
        """
        image = self.request.files.get("image")
        image_content = image[0]["body"]

        data = ImageService().image_upload(image_content)

        self.finish(data)