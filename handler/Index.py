#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Index Handler
"""
import tornado.web

from service.Image import ImageService


class IndexHandler(tornado.web.RequestHandler):
    """
    Index handler
    """

    def get(self):
        """
        首页
        """
        self.finish('hello bobo')

    def post(self):
        """
        图片上传
        """
        # self.finish('hello bobo')

        image = self.request.files.get("image")
        image_content = image[0]["body"]

        data = ImageService().image_upload(image_content)

        self.finish(data)