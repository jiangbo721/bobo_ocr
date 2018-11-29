#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文字识别接口
"""
import tornado.web

from service.character import CharacterService


class CharacterHandler(tornado.web.RequestHandler):
    """
    文字识别接口
    """
    def get(self):
        """
        图片上传
        """
        self.finish('please post')

    def post(self):
        """
        图片上传
        """
        image = self.request.files.get("image")
        if not image:
            self.finish("对不起，未检测到您上传的图片")
        image_content = image[0]["body"]

        data = CharacterService().image_upload(image_content)

        self.render("image/ocr_result.html", data=data)
