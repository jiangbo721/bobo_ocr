#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
全局定义
"""
from enum import Enum, unique


class Enum_Property(object):

    @property
    def code(self):
        """
        根据枚举名称取状态码code
        :return: 状态码code
        """
        return self.value.keys()[0]

    @property
    def msg(self):
        """
        根据枚举名称取状态说明message
        :return: 状态说明message
        """
        return self.value.values()[0]

@unique
class Code(Enum_Property, Enum):
    SUCC = {"000000": "成功"}
    FAIL = {"000001": "失败"}
    PARAM_IS_NULL = {"000002": "请求参数为空"}
    PARAM_ILLEGAL = {"000003": "请求参数非法"}
    REPEATED_COMMIT = {"000004": "重复提交"}
    SQL_ERROR = {"000005": "数据库异常"}
    EXIST = {"000006": "已存在"}
    NOT_EXIST = {"000007": "无记录"}
    INTERNAL = {"000008": "内部错误"}
    NETWORK_ERROR = {"000015": "网络异常"}
    UNKNOWN_ERROR = {"000099": "未知异常"}


if __name__ == '__main__':
    success = Code.SUCC

    print(success)
    print(type(success))
    print(success.code)
    print(success.msg)
