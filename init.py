#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
启动服务
"""
import tornado.httpserver
import tornado.ioloop
import tornado.web

from tornado.options import options

from handler.Image import ImageHandler
from handler.Index import IndexHandler

class Application(tornado.web.Application):
    """
    应用类
    """

    def __init__(self):
        # 应用配置
        settings = {
            "port": 8000,
        }

        handlers = [
            (r"/", IndexHandler),
            (r"/image/", ImageHandler),

        ]

        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()

    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(8000)

    tornado.ioloop.IOLoop.current().start()

