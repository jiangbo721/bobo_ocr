#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Index Handler
"""
from handler.base import BaseHandler


class IndexHandler(BaseHandler):
    """
    首页 handler
    """

    def get(self):
        """
        首页
        """
        self.render("index/index.html")

    def post(self, module):
        """
        首页
        """
        self.render("index/index.html")
