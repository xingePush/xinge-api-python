#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright ? 1998 - 2018 Tencent. All Rights Reserved. 腾讯公司 版权所有

"""

import base64
import httplib
import json
import urllib

import requests
from requests.auth import HTTPBasicAuth

from xinge_push.constant import *


class TagTokenPair(object):
    """
    tag-token串，用来批量设置tag和token的对应关系
    """

    def __init__(self, tag, token):
        self.tag = str(tag)
        self.token = str(token)


class XingeApp3(object):
    PATH_PUSH_APP = '/v3/push/app'

    IOS_MIN_ID = 2200000000

    def __init__(self, appId, secretKey):
        """

        :param appId: str, APP的唯一标识
        :param secretKey: str, 信鸽网站分配的通信密钥
        """
        self.appId = int(appId)
        self.secretKey = str(secretKey)

    def PushApp(self, context, params):
        """
        TODO
        """
        return Xinge3Helper.PushApp(self.appId, self.secretKey, context, params)


class Xinge3Helper(object):
    URL = 'https://openapi.xg.qq.com/'
    XINGE_PORT = 80
    TIMEOUT = 10
    HTTPS_METHOD = 'POST'
    HTTPS_HEADERS = {'HOST': URL, 'Content-Type': 'application/json'}

    STR_RET_CODE = 'ret_code'
    STR_ERR_MSG = 'err_msg'
    STR_RESULT = 'result'

    @classmethod
    def GenBase64EncodedStr(cls, appId, secretKey):
        signSource = '%s:%s' % (appId, secretKey)
        return base64.b64encode(signSource)

    @classmethod
    def PushApp(cls, app_id, secret_key , context, params):

        response = requests.post(cls.URL, auth=HTTPBasicAuth(app_id, secret_key), json=context, headers=cls.HTTP_HEADERS)

        retCode = ERR_RETURN_DATA
        errMsg = ''
        result = {}
        return retCode, errMsg, result
