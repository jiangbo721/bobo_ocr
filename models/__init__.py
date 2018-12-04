#!/usr/bin/env python
#encoding: utf-8

#引入基本的包
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# 连接数据库的数据
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'bobo_ocr'
USERNAME = 'root'
PASSWORD = 'itq7crwb!'
# DB_URI的格式：dialect（mysql/sqlite）+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# 创建引擎
engine = create_engine(DB_URI, echo=False )
#  sessionmaker生成一个session类
Session = sessionmaker(bind=engine)
dbSession = Session()