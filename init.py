#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
启动服务
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

define('runmode', default='local', help='local prod')
tornado.options.parse_command_line()

from conf.settings import ROOT_URL
from conf.log import mine_logger
from handler.character import CharacterHandler
from handler.image import ImageHandler
from handler.index import IndexHandler
from handler.user import UserHandler
from handler.face import FaceHandler

class Application(tornado.web.Application):
    """
    应用类
    """

    def __init__(self):
        # 应用配置
        settings = {
            "port": 8000,
            "template_path": "tpl",
            "static_path": "static",
            "login_url": "http://106.12.206.135/user/login",
        }

        handlers = [
            (r"/", IndexHandler),
            (r"/user(/[a-z_A-Z/]*)?", UserHandler),
            (r"/character(/[a-z_A-Z/]*)?", CharacterHandler),
            (r"/image(/[a-z_A-Z/]*)?", ImageHandler),
            (r"/face(/[a-z_A-Z/]*)?", FaceHandler),

        ]

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    mine_logger.warning(" bobo_ocr is running!!")
    mine_logger.warning("running at %s mode!!" % options.runmode)
    mine_logger.warning("root url is %s !!" % ROOT_URL)
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(8000)

    tornado.ioloop.IOLoop.current().start()
