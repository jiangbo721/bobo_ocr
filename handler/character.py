#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文字识别接口
"""
from handler.base import BaseHandler
from service.character import CharacterService
from service.defines import ID_CARD_SIDE


class CharacterHandler(BaseHandler):
    """
    文字识别接口
    """
    def get(self):
        """
        图片上传
        """
        self.finish('please post')

    def basic_accurate(self):
        """
        图片上传
        """
        image = self.request.files.get("image")
        if not image:
            self.finish("对不起，未检测到您上传的图片")
        image_content = image[0]["body"]

        data = CharacterService().basic_accurate(image_content)

        self.render("image/ocr_result.html", data=data)

    def idcard(self):
        """
        图片上传
        """
        image = self.request.files.get("image")
        id_card_side = self.get_argument("id_card_side", ID_CARD_SIDE.FRONT.code)
        if not image:
            self.finish("对不起，未检测到您上传的图片")
        image_content = image[0]["body"]

        data = CharacterService().idcard(image_content, id_card_side)

        self.render("image/ocr_result.html", data=data)
