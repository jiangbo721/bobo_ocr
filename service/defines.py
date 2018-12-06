#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图像识别通用定义
"""
from enum import Enum

from conf.defines import Enum_Property

RELIABILITY = 0.26
PERCENT_RELIABILITY = str(RELIABILITY * 100) + "%"
IMAGE_RESULT_TITLE_PATTERN = "您有{}种可能的结果，但我们把可信度大于{}的几个给您展示出来："
IMAGE_RESULT_ITEM_PATTERN = "您的第{}种结果为： {}, 类别为： {}, 可信度是： {}"
DISH_IMAGE_ITEM_PATTERN = "您的第{}种结果为： {}, 可信度是： {}"
ID_CARD_PATTERN = "您的{}是：{}"

class ID_CARD_SIDE(Enum_Property, Enum):
    FRONT = {"front": "正面"}
    BACK = {"back": "正面"}


FACE_FIELD = {"emotion", "angle", "beauty", "face_shape", "gender", "age",
              "quality", "glasses", "race", "location", "face_type",
              "eye_status", "face_token", "expression", "face_probability"}

HAS_ENUM_FACE_FIELD = {"emotion", "face_shape", "gender",
                       "glasses", "race", "face_type", "expression"}


FACE_FIELD_DESC = {
    "emotion": "情绪",  # 情绪
    "angle": "人脸旋转角度参数",  # 人脸旋转角度参数
    "beauty": "颜值",  # 美丑打分，范围0-100，越大表示越美
    "face_shape": "脸型",  # 脸型
    "gender": "性别",  # 性别
    "age": "年龄",  # 年龄
    "quality": "人脸质量信息",  # 人脸质量信息
    "glasses": "眼镜",  # 是否带眼镜
    "race": "人种",  # 人种
    "location": "人脸的位置",  # 人脸在图片中的位置
    "face_type": "是否人脸",  # 真实人脸/卡通人脸
    "eye_status": "双眼状态（睁开/闭合）",  # 双眼状态（睁开/闭合）
    "face_token": "人脸图片的唯一标识",  # 人脸图片的唯一标识
    "expression": "表情",  # 表情
    "face_probability": "人脸可能性",  # 人脸置信度
}

EMOTION = {
    "angry": "愤怒",
    "disgust": "厌恶",
    "fear": "恐惧",
    "happy": "高兴",
    "sad": "伤心",
    "surprise": "惊讶",
    "neutral": "无情绪"
}

EXPRESSION = {
    "none": "不笑",
    "smile": "微笑",
    "laugh": "大笑",
}

FACE_SHAPE = {
    "square": "正方形",
    "triangle": "三角形",
    "oval": "椭圆",
    "heart": "心形",
    "round": "圆形",
}

GENDER = {
    "male": "男性",
    "female": "女性",
}

GLASSES = {
    "none": "无眼镜",
    "common": "普通眼镜",
    "sun": "墨镜",
}

RACE = {
    "yellow": "黄种人",
    "white": "白种人",
    "black": "黑种人",
    "arabs": "阿拉伯人",
}

FACE_TYPE = {
	"human": "真实人脸",
    "cartoon": "卡通人脸",
}

FACE_FIELD_MAP = {
    "emotion": EMOTION,
    "face_shape": FACE_SHAPE,
    "gender": GENDER,
    "glasses": GLASSES,
    "race": RACE,
    "face_type": FACE_TYPE,
    "expression": EXPRESSION,
}