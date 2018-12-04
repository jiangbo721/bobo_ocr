#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
日志服务
"""
import logging


# logging.basicConfig(
#     level=logging.INFO,
#     filename='./logfile/sys.log',
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# )

# 我的logger
mine_logger = logging.getLogger('mine')
mine_logger.setLevel(logging.INFO)

# 配置两个handler
# console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('./logfile/logger.log')

# 配置一个formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 给两个handler设置格式
# console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将两个handler绑定到我的logger
# mine_logger.addHandler(console_handler)
mine_logger.addHandler(file_handler)
