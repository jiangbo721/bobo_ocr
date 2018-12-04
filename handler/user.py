#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用户 Handler
"""
from handler.base import BaseHandler


class UserHandler(BaseHandler):
    """
    用户 handler
    """

    def login(self):
        """
        首页
        """
        self.render("user/login.html")

    def post(self, module):
        """
        首页
        """
        self.render("index/index.html")
