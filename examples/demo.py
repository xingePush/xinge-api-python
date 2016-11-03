#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 1998 - 2013 Tencent. All Rights Reserved. 腾讯公司 版权所有
"""

import xinge_push


# 定义通知
def BuildNotification():
    msg = xinge_push.Message()
    msg.type = xinge_push.MESSAGE_TYPE_ANDROID_NOTIFICATION
    msg.title = 'some title'
    msg.content = 'some content'
    # 消息为离线设备保存的时间，单位为秒。默认为0，表示只推在线设备
    msg.expireTime = 86400
    # 定时推送，非必须
    # msg.sendTime = '2012-12-12 18:48:00'
    # 自定义键值对，key和value都必须是字符串，非必须
    msg.custom = {'aaa': '111', 'bbb': '222'}
    # 使用多包名推送模式，详细说明参见文档和wiki，如果您不清楚该字段含义，则无需设置
    # msg.multiPkg = 1

    # 允许推送时段设置，非必须
    # ti1 = TimeInterval(9, 30, 11, 30)
    # ti2 = TimeInterval(14, 0, 17, 0)
    # msg.acceptTime = (ti1, ti2)

    # 通知展示样式，仅对通知有效
    # 样式编号为2，响铃，震动，不可从通知栏清除，不影响先前通知
    style = xinge_push.Style(2, 1, 1, 0, 0)
    msg.style = style

    # 点击动作设置，仅对通知有效
    # 以下例子为点击打开url
    action = xinge_push.ClickAction()
    action.actionType = xinge_push.ClickAction.TYPE_URL
    action.url = 'http://xg.qq.com'
    # 打开url不需要用户确认
    action.confirmOnUrl = 0
    msg.action = action

    # 以下例子为点击打开intent。例子中的intent将打开拨号界面并键入10086
    # 使用intent.toUri(Intent.URI_INTENT_SCHEME)方法来得到序列化后的intent字符串，自定义intent参数也包含在其中
    # action = ClickAction()
    # action.actionType = ClickAction.TYPE_INTENT
    # action.intent = 'intent:10086#Intent;scheme=tel;action=android.intent.action.DIAL;S.key=value;end'
    # msg.action = action

    return msg


# 定义透传消息
def BuildMsg():
    msg = xinge_push.Message()
    msg.type = xinge_push.MESSAGE_TYPE_ANDROID_MESSAGE
    msg.title = 'some title'
    msg.content = 'some content'
    # 消息为离线设备保存的时间，单位为秒。默认为0，表示只推在线设备
    msg.expireTime = 86400
    # 定时推送，若不需定时可以不设置
    # msg.sendTime = '2012-12-12 18:48:00'
    # 自定义键值对，key和value都必须是字符串
    msg.custom = {'aaa': '111', 'bbb': '222'}
    # 使用多包名推送模式，详细说明参见文档和wiki，如果您不清楚该字段含义，则无需设置
    # msg.multiPkg = 1

    # 允许推送时段设置，非必须
    # ti1 = TimeInterval(9, 30, 11, 30)
    # ti2 = TimeInterval(14, 0, 17, 0)
    # msg.acceptTime = (ti1, ti2)

    return msg


# 定义iOS消息
def BuildIOSMsg():
    msg = xinge_push.MessageIOS()
    # alert字段可以是字符串或json对象，参见APNS文档
    msg.alert = "alert content"
    # 消息为离线设备保存的时间，单位为秒。默认为0，表示只推在线设备
    msg.expireTime = 3600
    # 定时推送，若不需定时可以不设置
    # msg.sendTime = '2012-12-12 18:48:00'
    # 自定义键值对，value可以是json允许的类型
    msg.custom = {'aaa': '111', 'bbb': {'b1': 1, 'b2': 2}}

    # 允许推送时段设置，非必须
    # ti1 = TimeInterval(9, 30, 11, 30)
    # ti2 = TimeInterval(14, 0, 17, 0)
    # msg.acceptTime = (ti1, ti2)

    return msg


# 按token推送
def DemoPushToken(x, msg):
    # 第三个参数environment仅在iOS下有效。ENV_DEV表示推送APNS开发环境
    ret = x.PushSingleDevice('some_token', msg, xinge_push.ENV_DEV)
    print ret


# 按账号推送
def DemoPushAccount(x, msg):
    ret = x.PushSingleAccount(0, '123456', msg, xinge_push.ENV_DEV)
    print ret


# 按多账号推送
def DemoPushAccountList(x, msg):
    accountList = list()
    accountList.append('241008')
    ret = x.PushAccountList(0, accountList, msg, xinge_push.ENV_DEV)
    print ret


# 按app推送
def DemoPushAll(x, msg):
    # 第三个参数environment仅在iOS下有效。ENV_DEV表示推送APNS开发环境
    ret = x.PushAllDevices(0, msg, xinge_push.ENV_DEV)
    print ret


# 按tag推送
def DemoPushTags(x, msg):
    # 第三个参数environment仅在iOS下有效。ENV_DEV表示推送开发环境
    ret = x.PushTags(0, ('tag1', 'tag2'), 'AND', msg, xinge_push.ENV_DEV)
    print ret


# 按账号大批量推送
def DemoPushAccountListMultiple(x, msg):
    ret = x.CreateMultipush(msg, xinge_push.ENV_DEV)
    if ret[0] != 0:
        print ret
    else:
        push_id = ret[2]
        accountList1 = list()
        accountList1.append('241008')
        accountList1.append('241009')
        ret = x.PushAccountListMultiple(push_id, accountList1)
        print ret
        accountList2 = list()
        accountList2.append('241010')
        accountList2.append('241011')
        ret = x.PushAccountListMultiple(push_id, accountList2)
        print ret


# 按token大批量推送
def DemoPushDeviceListMultiple(x, msg):
    ret = x.CreateMultipush(msg, xinge_push.ENV_DEV)
    if ret[0] != 0:
        print ret
    else:
        push_id = ret[2]
        deviceList1 = list()
        deviceList1.append('token1')
        deviceList1.append('token2')
        ret = x.PushDeviceListMultiple(push_id, deviceList1)
        print ret
        deviceList2 = list()
        deviceList2.append('token3')
        deviceList2.append('token4')
        ret = x.PushDeviceListMultiple(push_id, deviceList2)
        print ret


# 查询群发任务状态
def DemoQueryPushStatus(x):
    # 查询群发id为31和30的消息状态
    ret = x.QueryPushStatus(('31', '30'))
    print ret


# 查询app覆盖设备数量
def DemoQueryDeviceNum(x):
    ret = x.QueryDeviceCount()
    print ret


# 查询tag
def DemoQueryTags(x):
    # 查询头5个tag
    ret = x.QueryTags(0, 5)
    print ret


# 取消尚未触发的定时群发任务
def DemoCancelTimingPush(x):
    ret = x.CancelTimingPush('31')
    print ret


# token-标签绑定
def DemoBatchSetTag(x):
    # 切记把这里的示例tag和示例token修改为你的真实tag和真实token
    pairs = []
    pairs.append(xinge_push.TagTokenPair("tag1", "token00000000000000000000000000000000001"))
    pairs.append(xinge_push.TagTokenPair("tag2", "token00000000000000000000000000000000002"))
    ret = x.BatchSetTag(pairs)
    print ret


# token-标签解绑
def DemoBatchDelTag(x):
    # 切记把这里的示例tag和示例token修改为你的真实tag和真实token
    pairs = []
    pairs.append(xinge_push.TagTokenPair("tag1", "token00000000000000000000000000000000001"))
    pairs.append(xinge_push.TagTokenPair("tag2", "token00000000000000000000000000000000002"))
    ret = x.BatchDelTag(pairs)
    print ret


# 查询token绑定的标签
def DemoQueryTokenTags(x):
    # 请把这里示例token修改为你的真实token
    ret = x.QueryTokenTags('token00000000000000000000000000000000001')
    print ret


# 查询标签绑定的设备数
def DemoQueryTagTokenNum(x):
    # 请把这里示例tag修改为你的真实tag
    ret = x.QueryTagTokenNum('tag1')
    print ret


# 查询token的信息
def DemoQueryInfoOfToken(x):
    # 请把这里示例token修改为你的真实token
    ret = x.QueryInfoOfToken('token00000000000000000000000000000000001')
    print ret


# 查询account绑定的token
def DemoQueryTokensOfAccount(x):
    # 请把这里示例account修改为真实的account
    ret = x.QueryTokensOfAccount('nickname')
    print ret


# 删除account绑定的token
def DemoDeleteTokenOfAccount(x):
    # 请把这里示例account和token修改为你的真实account和token
    ret = x.DeleteTokenOfAccount('account1', 'token00000000000000000000000000000000001')


# 删除account绑定的所有token
def DemoDeleteAllTokensOfAccount(x):
    # 请把这里示例account修改为你的真实account
    ret = x.DeleteTokenOfAccount('account1', "token1")


if '__main__' == __name__:
    # 初始化app对象，设置有效的access id和secret key
    x = xinge_push.XingeApp(0, 'secret')

    # 构建一条消息，可以是通知或者透传消息
    # msg = BuildMsg()
    msg = BuildNotification()

    # 构建iOS消息。注意iOS只有一种消息类型，不分通知/透传
    # iOS推送，调用push接口时切记设置ENV
    # msg = BuildIOSMsg()

    DemoPushToken(x, msg)
    DemoPushAccount(x, msg)
    DemoPushAccountList(x, msg)
    DemoPushAll(x, msg)
    DemoPushTags(x, msg)
    DemoPushAccountListMultiple(x, msg)
    DemoPushDeviceListMultiple(x, msg)
    DemoQueryPushStatus(x)
    DemoQueryDeviceNum(x)
    DemoQueryTags(x)
    DemoCancelTimingPush(x)
    DemoBatchSetTag(x)
    DemoBatchDelTag(x)
    DemoQueryTokenTags(x)
    DemoQueryTagTokenNum(x)
    DemoQueryInfoOfToken(x)
    DemoQueryTokensOfAccount(x)
    DemoDeleteTokenOfAccount(x)
    DemoDeleteAllTokensOfAccount(x)
