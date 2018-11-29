#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
启动服务
"""
import tornado.ioloop
import tornado.httpserver
import tornado.web

from handler.character import CharacterHandler
from handler.Index import IndexHandler

class Application(tornado.web.Application):
    """
    应用类
    """

    def __init__(self):
        # 应用配置
        settings = {
            "port": 8000,
            "template_path": "tpl"
        }

        handlers = [
            (r"/", IndexHandler),
            (r"/char/", CharacterHandler),

        ]

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(8000)

    tornado.ioloop.IOLoop.current().start()

