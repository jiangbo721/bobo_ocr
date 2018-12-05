#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
配置文件
"""
# 加载相应环境的配置
import logging

from tornado.options import options

if options.runmode == "local":
    from settings_local import *
    logging.getLogger("mine").warning("running with local settings!!!")
elif options.runmode == "prod":
    from conf.settings_prod import *
else:
    raise Exception("wrong runmode")