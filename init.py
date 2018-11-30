#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
启动服务
"""
import logging
from logging.config import dictConfig

import tornado.ioloop
import tornado.httpserver
import tornado.web

from conf.log_cnf import logging_config
from handler.character import CharacterHandler
from handler.Index import IndexHandler
from handler.image import ImageHandler


dictConfig(logging_config)

class Application(tornado.web.Application):
    """
    应用类
    """

    def __init__(self):
        # 应用配置
        settings = {
            "port": 8000,
            "template_path": "tpl",
        }

        handlers = [
            (r"/", IndexHandler),
            (r"/character/", CharacterHandler),
            (r"/image/", ImageHandler),

        ]

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    logging.warning(" bobo_ocr is running!!")
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(8000)

    tornado.ioloop.IOLoop.current().start()


