#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Index Handler
"""
import tornado.web

from service.character import CharacterService


class IndexHandler(tornado.web.RequestHandler):
    """
    首页 handler
    """

    def get(self):
        """
        首页
        """
        self.render("index/index.html")

    def post(self):
        """
        首页
        """
        self.finish('hello bobo')
