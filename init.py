#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
启动服务
"""
import logging

import tornado.ioloop
import tornado.httpserver
import tornado.web

from handler.character import CharacterHandler
from handler.index import IndexHandler
from handler.image import ImageHandler


logging.basicConfig(level=logging.DEBUG, filename='./logfile/logger.log')

root_logger = logging.getLogger()

mine_logger = logging.getLogger('mine')
mine_logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('./logfile/logger.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

mine_logger.addHandler(console_handler)
mine_logger.addHandler(file_handler)


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
            (r"/character(/[a-z_A-Z/]*)?", CharacterHandler),
            (r"/image(/[a-z_A-Z/]*)?", ImageHandler),

        ]

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    mine_logger.warning(" bobo_ocr is running!!")
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(8000)

    tornado.ioloop.IOLoop.current().start()


