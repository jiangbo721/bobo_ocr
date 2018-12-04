#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用户服务
"""
import logging

from service.base import BaseService

mine_logger = logging.getLogger('mine')


class UserService(BaseService):
    """
    用户服务
    """
    def __init__(self):
        super(UserService, self).__init__()

    def login(self):
        pass