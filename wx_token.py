#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 10:25
# @User    : zhunishengrikuaile
# @File    : wx_token.py
# @Email   : NAME@SHUJIAN.ORG
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 一起哟预约报名小程序后端
import os
import json
import requests
from PIL import Image
from io import BytesIO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_ID = '填写您的小程序APPID'
APP_SECRET = '填写你小程序的APPSECRET'
code_urls = "https://api.weixin.qq.com/cgi-bin/wxaapp/createwxaqrcode?access_token="
token_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={APPSECRET}".format(
    APPID=APP_ID, APPSECRET=APP_SECRET)


def get_token():
    '''
    获取TOKEN
    :return:
    '''
    get_token = requests.get(token_url)
    return get_token


def post_wxcode(code_urls=code_urls, path="pages/index/index", width=430):
    '''
    获取微信小程序二维码
    :return:
    '''
    headers = {'content-type': 'application/json'}
    code_url = code_urls + get_token().json()['access_token']
    data = json.dumps({"path": path, "width": width})
    print(data)
    code = requests.post(code_url, data=data, headers=headers)
    return code


def image_saver(image_paths="upload/images/", image_name=""):
    '''
    保存图片到文件
    :param file_path:
    :param file_name:
    :return:
    '''
    test_code = post_wxcode()
    image_path = os.path.join(BASE_DIR, image_paths)
    image_names = image_path + image_name + '.png'
    if os.path.exists(image_path) == False:
        os.mkdir(image_path)
    wx_code = Image.open(BytesIO(test_code.content))
    wx_code.save(image_names)
    return image_paths + image_name + '.png'


if __name__ == "__main__":
    test_code = image_saver(image_name='test')
    print(test_code)
