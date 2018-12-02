#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Handler基类
"""
import json
import pprint
import logging
import tornado.web

from conf.defines import Code


class BaseHandler(tornado.web.RequestHandler):
    """
    基础功能封装
    """
    def initialize(self, prefix=None):
        """
        重写Handler初始化
        """
        self.module_prefix = prefix

    def send_json(self, res, code=Code.SUCC, msg=None):
        """
        发送json数据
        """
        response = {
            "code": code.code,
            "msg": msg or code.msg,
            "body": res
        }

        # 当响应为失败或者当前的debug模式为真的情况下,显示请求和响应信息
        if code != Code.SUCC:
            logging.warn("request: %s", self.request.arguments)
            logging.error("response fail: %s", json.dumps(response))
        logging.warn("request: %s", self.request.arguments)

        # 对于非常大的数据, 用pprint的depth参数, 能自动的忽略更深深度的数据
        response_str = json.dumps(response, indent=2)
        if len(response_str) <= 2048:
            logging.warn("response succ: \n%s", response_str)
        else:
            logging.warn("response succ: \n%s", pprint.pformat(response, width=1, indent=2, depth=2))

        self.set_header("Content-Type", "application/json")
        self.finish(json.dumps(response))

    def get_argument(self, name, default=tornado.web.RequestHandler._ARG_DEFAULT,
                     strip=True):
        """
        重写以把unicode的参数都进行utf-8编码
        """
        value = super(BaseHandler, self).get_argument(name, default, strip)
        if isinstance(value, unicode):
            value = value.encode("utf-8")
        return value

    def process_module(self, module):
        """
        内部路由分发
        """
        module = module or ""
        if self.module_prefix:
            module = "%s/%s" % (self.module_prefix, module)
        module = "__".join([i for i in module.split("/") if i])
        method = getattr(self, module or "index", None)
        if method and module not in ("get", "post"):
            try:
                method()
            except Exception as exp:
                logging.error("%s\n%s\n", self.request, str(exp))
                code = Code.INTERNAL
                msg = str(exp)

                self.send_json(None, code, msg)
        else:
            raise tornado.web.HTTPError(404)

    def get(self, module):
        """
        HTTP GET处理
        """
        self.process_module(module)

    def post(self, module):
        """
        HTTP POST处理
        """
        self.process_module(module)
