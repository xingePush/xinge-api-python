#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.1.9'

from xinge_push.xinge3 import XingeApp3

def PushApp(accessId, secretKey, content):
    """
    推送到单个设备, 限Android系统使用
    :param accessId: int, APP的唯一标识
    :param secretKey: str, 信鸽网站分配的通信密钥
    :param content: str, 消息内容
    :return: (int, str), (ret_code, error_msg)
    """
    xg = XingeApp3(accessId, secretKey)
    return xg.PushApp(content)

__all__ = ['XingeApp3',

           'PushApp',
           ]
