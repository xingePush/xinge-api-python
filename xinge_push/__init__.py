#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.1.9'

from .xinge import XingeApp, TagTokenPair
from .style import Style, ClickAction
from .message import Message, MessageIOS
from .schedule import TimeInterval
from .constant import *

def _BuildAndroidNotification(title, content):
    msg = Message()
    msg.type = MESSAGE_TYPE_ANDROID_NOTIFICATION
    msg.title = title
    msg.content = content
    msg.style = Style(1, 1)
    msg.action = ClickAction()
    return msg

def _BuildIosNotification(content):
    msg = MessageIOS()
    msg.alert = content
    return msg

def PushTokenAndroid(accessId, secretKey, title, content, token):
    """
    推送到单个设备, 限Android系统使用
    :param accessId: int, APP的唯一标识
    :param secretKey: str, 信鸽网站分配的通信密钥
    :param title: str, 消息标题
    :param content: str, 消息内容
    :param token: str, 目标设备
    :return: (int, str), (ret_code, error_msg)
    """
    x = XingeApp(accessId, secretKey)
    return x.PushSingleDevice(token, _BuildAndroidNotification(title, content))


def PushAccountAndroid(accessId, secretKey, title, content, account):
    """
    推送到单个账号, 限Android系统使用
    :param accessId: int, APP的唯一标识
    :param secretKey: str, 信鸽网站分配的通信密钥
    :param title: str, 消息标题
    :param content: str, 消息内容
    :param account: str, 账号
    :return: (int, str), (ret_code, error_msg)
    """
    x = XingeApp(accessId, secretKey)
    return x.PushSingleAccount(0, account, _BuildAndroidNotification(title, content))


def PushAllAndroid(accessId, secretKey, title, content):
    """
    推送到所有设备, 限Android系统使用
    :param accessId: int, APP的唯一标识
    :param secretKey: str, 信鸽网站分配的通信密钥
    :param title: str, 消息标题
    :param content: str, 消息内容
    :return: 若成功则返回(int, str, str), (0, '', push_id)；失败返回(int, str, None), (ret_code, error_msg, None)
    """
    x = XingeApp(accessId, secretKey)
    return x.PushAllDevices(0, _BuildAndroidNotification(title, content))


def PushTagsAndroid(accessId, secretKey, title, content, tag):
    """
    推送给多个tags对应的设备
    :param accessId: int, APP的唯一标识
    :param secretKey: str, 信鸽网站分配的通信密钥
    :param title: str, 消息标题
    :param content: str, 消息内容
    :param tag: Iterable, 指定推送的tag列表
    :return: 若成功则返回(int, str, str), (0, '', push_id)；失败返回(int, str, None), (ret_code, error_msg, None)
    """
    x = XingeApp(accessId, secretKey)
    return x.PushTags(0, (tag,), 'OR', _BuildAndroidNotification(title, content))


def PushTokenIos(accessId, secretKey, content, token, env):
    """
    推送到单个设备, 限iOS系统使用
    :param accessId: int, APP的唯一标识
    :param secretKey: str, 信鸽网站分配的通信密钥
    :param content: str, 消息内容
    :param token: str, 目标设备
    :param env: int, 推送的目标环境，必须是ENV_PROD或ENV_DEV的一种
    :return: (int, str), (ret_code, error_msg)
    """
    x = XingeApp(accessId, secretKey)
    return x.PushSingleDevice(token, _BuildIosNotification(content), env)


def PushAccountIos(accessId, secretKey, content, account, env):
    """
    推送到单个账号, 限iOS系统使用
    :param accessId: int, APP的唯一标识
    :param secretKey: str, 信鸽网站分配的通信密钥
    :param content: str, 消息内容
    :param account: str, 目标账号
    :param env: int, 推送的目标环境，必须是ENV_PROD或ENV_DEV的一种
    :return: (int, str), (ret_code, error_msg)
    """
    x = XingeApp(accessId, secretKey)
    return x.PushSingleAccount(0, account, _BuildIosNotification(content), env)


def PushAllIos(accessId, secretKey, content, env):
    """
    推送到所有设备, 限iOS系统使用
    :param accessId: int, APP的唯一标识
    :param secretKey: str, 信鸽网站分配的通信密钥
    :param content: str, 消息内容
    :param env: int, 推送的目标环境，必须是ENV_PROD或ENV_DEV的一种
    :return: 若成功则返回(int, str, str), (0, '', push_id)；失败返回(int, str, None), (ret_code, error_msg, None)
    """
    x = XingeApp(accessId, secretKey)
    return x.PushAllDevices(0, _BuildIosNotification(content), env)


def PushTagsIos(accessId, secretKey, content, tag, env):
    """
    推送给多个tags对应的设备
    :param accessId: int, APP的唯一标识
    :param secretKey: str, 信鸽网站分配的通信密钥
    :param content: str, 消息内容
    :param tag: Iterable, 指定推送的tag列表
    :param env: int, 推送的目标环境，必须是ENV_PROD或ENV_DEV的一种
    :return: 若成功则返回(int, str, str), (0, '', push_id)；失败返回(int, str, None), (ret_code, error_msg, None)
    """
    x = XingeApp(accessId, secretKey)
    return x.PushTags(0, (tag,), 'OR', _BuildIosNotification(content), env)


__all__ = ['XingeApp',
           'TagTokenPair',
           'Style',
           'ClickAction',
           'Message',
           'MessageIOS',
           'TimeInterval',

           'ENV_DEV',
           'ENV_PROD',
           'MESSAGE_TYPE_ANDROID_NOTIFICATION',
           'MESSAGE_TYPE_ANDROID_MESSAGE',
           'MESSAGE_TYPE_IOS_APNS_NOTIFICATION',
           'MESSAGE_TYPE_IOS_REMOTE_NOTIFICATION',

           'PushTokenAndroid',
           'PushTokenIos',
           'PushAccountAndroid',
           'PushAccountIos',
           'PushAllAndroid',
           'PushAllIos',
           'PushTagsAndroid',
           'PushTagsIos',
           ]
