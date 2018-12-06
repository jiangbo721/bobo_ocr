#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
人脸识别服务
"""
import base64
import logging

from service.baidu_ocr import face
from service.base import BaseService
from service.defines import HAS_ENUM_FACE_FIELD, FACE_FIELD_DESC, FACE_FIELD_MAP


class FaceService(BaseService):
    """
    图像识别处理服务
    """
    def __init__(self):
        super(FaceService, self).__init__()
        self.UPLOAD_DIR_PATH = "/data/ocr/face"
        self.face = face
        self.log = logging.getLogger('mine')

    def detection(self, image_content, image_type="BASE64", max_face_num=10):
        """
        人脸检测
        :param str image_content: 图片二进制内容
        :param image_type:
        :return dict: result 识别结果
        :return:
        """
        # 图像编码
        image_base64 = base64.b64encode(image_content).decode()

        # 获取识别结果
        baidu_result = self.face.detect(image_base64, image_type, options={
            "face_field": "age,beauty,expression,face_shape,gender,glasses,"
                          "race,eye_status,emotion,face_type",
            "max_face_num": max_face_num,
        })
        self.log.warning(baidu_result)
        # 保存图片
        self._image_save(image_content)

        # 解析结果
        result_list = []
        face_num = baidu_result["result"]["face_num"]
        result_list.append("这张图片有{}张脸".format(face_num))
        for index, face in enumerate(baidu_result["result"]["face_list"], 1):
            result_list.append("您的第{}张脸的信息是：".format(index))
            for item in face:
                if item in ("angle", "location", "face_token"):
                    continue
                if item in HAS_ENUM_FACE_FIELD:
                    result = ":".join([FACE_FIELD_DESC[item], FACE_FIELD_MAP[item][face[item]["type"]]])
                elif item == "eye_status":
                    result = "双眼状态: 左眼:{}, 右眼:{}".format(
                        "睁开" if face[item]["left_eye"] > 0.5 else "闭合",
                        "睁开" if face[item]["right_eye"] > 0.5 else "闭合")
                else:
                    result = ":".join([FACE_FIELD_DESC[item], str(face[item])])
                self.log.info(result)
                result_list.append(result)
            result_list.append("\n\n")

        return result_list

