#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright ? 1998 - 2018 Tencent. All Rights Reserved. 腾讯公司 版权所有

"""

import base64
import hashlib
import httplib
import json
import time
import urllib

from constant import *
from message import MessageIOS


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

    def ValidateToken(self, token):
        if (self.appId >= 2200000000):
            return len(token) == 64
        else:
            return (len(token) == 40 or len(token) == 64)

    def InitParams(self):
        params = {}
        params['app_id'] = self.appId
        params['timestamp'] = XingeHelper.GenTimestamp()
        return params

    def ValidateMessageType(self, message):
        if (self.appId >= self.IOS_MIN_ID and isinstance(message, MessageIOS)):
            return True
        elif (self.appId < self.IOS_MIN_ID and not isinstance(message, MessageIOS)):
            return True
        else:
            return False

    def Request(self, path, params):
        params['Authorization'] = Xinge3Helper.GenBase64EncodedStr(self.appId, self.secretKey)
        return Xinge3Helper.Request(path, params)


class Xinge3Helper(object):
    XINGE_HOST = 'openapi.xg.qq.com'
    XINGE_PORT = 80
    TIMEOUT = 10
    HTTPS_METHOD = 'POST'
    HTTPS_HEADERS = {'HOST': XINGE_HOST, 'Content-Type': 'application/x-www-form-urlencoded'}


    STR_RET_CODE = 'ret_code'
    STR_ERR_MSG = 'err_msg'
    STR_RESULT = 'result'


    @classmethod
    def SetServer(cls, host=XINGE_HOST, port=XINGE_PORT):
        cls.XINGE_HOST = host
        cls.XINGE_PORT = port
        cls.HTTPS_HEADERS['HOST'] = cls.XINGE_HOST


    @classmethod
    def GenSign(cls, path, params, secretKey):
        ks = sorted(params.keys())
        paramStr = ''.join([('%s=%s' % (k, params[k])) for k in ks])
        signSource = '%s%s%s%s%s' % (cls.HTTP_METHOD, cls.XINGE_HOST, path, paramStr, secretKey)
        return hashlib.md5(signSource).hexdigest()


    @classmethod
    def GenBase64EncodedStr(cls, appId, secretKey):
        signSource = '%s:%s' % (appId, secretKey)
        return base64.b64encode(bytes(signSource, 'utf-8'))


    @classmethod
    def GenTimestamp(cls):
        return int(time.time())


    @classmethod
    def Request(cls, path, params):

        httpClient = httplib.HTTPSConnection(cls.XINGE_HOST, cls.XINGE_PORT, timeout=cls.TIMEOUT)
        if cls.HTTP_METHOD == 'POST':
            httpClient.request(cls.HTTP_METHOD, path, urllib.urlencode(params), headers=cls.HTTP_HEADERS)
        else:
            # invalid method
            return ERR_PARAM, '', None

        response = httpClient.getresponse()
        retCode = ERR_RETURN_DATA
        errMsg = ''
        result = {}
        if 200 != response.status:
            retCode = ERR_HTTP
        else:
            data = response.read()
            retDict = json.loads(data)
            if (cls.STR_RET_CODE in retDict):
                retCode = retDict[cls.STR_RET_CODE]
            if (cls.STR_ERR_MSG in retDict):
                errMsg = retDict[cls.STR_ERR_MSG]
            if (cls.STR_RESULT in retDict):
                if isinstance(retDict[cls.STR_RESULT], dict):
                    result = retDict[cls.STR_RESULT]
                elif isinstance(retDict[cls.STR_RESULT], list):
                    result = retDict[cls.STR_RESULT]
                elif retDict[cls.STR_RESULT] == '':
                    pass
                else:
                    retCode = ERR_RETURN_DATA
        return retCode, errMsg, result
