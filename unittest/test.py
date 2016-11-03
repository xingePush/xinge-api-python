#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2013-12-20

@author: stanleyzeng
'''

import random
import string
import time

from xinge_push import *
from xinge_push.xinge import XingeHelper

XingeHelper.SetServer('10.213.110.4')
#XingeHelper.SetServer('10.213.166.139')
#XingeHelper.SetServer('10.213.166.176')
#XingeHelper.SetServer('10.133.2.212')
#XingeHelper.SetServer('10.133.1.153')
#XingeHelper.SetServer('10.139.6.79')
#XingeHelper.SetServer('10.166.224.41')
#XingeHelper.SetServer('10.128.67.229')
#XingeHelper.SetServer('10.177.153.110')
#XingeHelper.SetServer('10.135.1.71')
#XingeHelper.SetServer('10.133.2.170')
#XingeHelper.SetServer('10.133.2.171')
#XingeHelper.SetServer('10.133.2.12')
#XingeHelper.SetServer('10.133.1.154')
#XingeHelper.SetServer('10.133.1.157')
#XingeHelper.SetServer('10.133.1.162')
#XingeHelper.SetServer('vipopenapi.xg.qq.com')

def TestPushToken():
    x = XingeApp(353, '353_secret_key')
    #x = XingeApp(100, 'key2')
    x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = XingeApp(2100072080, 'ee88b194a5b6949f769c454d75e6b3e9')
    #x = XingeApp(2100000097, '50f3b708dc241503484c80996c3e46b3')
    #x = XingeApp(2100000105, '8131855e542e676348d77e4fbb7f58d3')
    #x = XingeApp(2100040684, '5d232659dc55e03f4df5a95587b0c64c')
    #x = XingeApp(2100038814, '74e636481463b7d57ea04956c096c4b4')
    #x = XingeApp(2190000354, 'xg354key')
    #x = XingeApp(2100034689, '05e37e44035deecad0bce6b3320d6991')
    #x = XingeApp(2194903379, '4578e54fb3a1bd18e0681bc1c734514e')
    msg = Message()
    #msg = MessageIOS()
    msg.type = Message.TYPE_MESSAGE
    msg.type = Message.TYPE_NOTIFICATION
    msg.title = '中文标题按token'
    msg.content = '中文内容，これは中国である+++'
    #msg.content = 'aaa啊こ'
    #msg.content = '来自信鸽后台的测试消息'
    #msg.content = '{"content":{"aps":{"title":"\u5fae\u4fe1\u516c\u4f17\u53f7\u5f71\u54cd\u529b\u6392\u884c\u699c\u53d1\u5e03","alert":"\u4e0e\u624b\u673a\u79fb\u52a8\u7b49\u65b0\u5a92\u4f53\u76f8\u6bd4\uff0c\u4ee5\u62a5\u7eb8\u4e3a\u4ee3\u8868\u7684\u4f20\u7edf\u5a92\u4f53\uff0c\u6108\u52a0\u5b64\u5bc2\u4e0e\u6ca1\u843d\u3002","contentid":"959","modelid":"1"}}}'
    #msg.content = '中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文'
    #msg.custom = {'aaa':'111', 'bbb':'222'}
    msg.sendTime = '2015-01-07 14:50:00'
    #msg.sendTime = '2070-01-01 08:00:-1'
    msg.expireTime = 999999
    #msg.multiPkg = Message.PUSH_ACCESS_ID

    ti = TimeInterval(20, 22, 23, 0)
    #msg.acceptTime = (ti,)

    #style = Style(2, 1, 1, 1)
    style = Style(0, 1, 1, 1)
    msg.style = style
    
    action = ClickAction()
    action.actionType = ClickAction.TYPE_URL
    #action.actionType = 4
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action
    
    ret = x.PushSingleDevice('16f4f363697c09a84642ab9145fae91bb46a223a', msg, XingeApp.ENV_DEV)    #ret = x.PushSingleDevice('bbbb3a7baae5b88f4ca89c583a54cd74337c284a', msg, XingeApp.ENV_DEV)
    #ret = x.PushSingleDevice('16ec008f123a7b444161a113f25c7ebcf0df1b09', msg, XingeApp.ENV_DEV)
    #ret = x.PushSingleDevice('4c0168514359ddae4879a48e3c76a46542920e80', msg, XingeApp.ENV_DEV)
    #ret = x.PushSingleDevice('c762a481feebc44f4b7b99d80482e0b1736ca263', msg, XingeApp.ENV_DEV)
    
    print ret

def TestPushTokenIos():
    x = XingeApp(101, 'skey')
    #x = XingeApp(2200002956, '1f0d10a3589de22a9fbd84e011ba126f')
    #x = XingeApp(2100001657, 'd89db8f08a067b39f85729779423bdba')
    #x = XingeApp(2200003965, '13cf9e99db5bc421dec3d78889e806e5')
    #msg = Message()
    msg = MessageIOS()
    #msg.raw = '{"aps":{"alert":"Hello world--joelliu!!! message from c++"}}'
    #msg.alert = 'gogogo'
    #msg.alert = '我  是%中文'
    #msg.alert = '==================================================================================================================================================================================================================================================='
    #msg.alert = '我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字'
    msg.alert = '555555555'
    #msg.badge = 5
    #msg.sound = 'ooo.wav'
    #msg.custom['aa'] = 'sssss'
    #msg.sendTime = '2014-03-12 18:21:00'
    ti = TimeInterval(20, 0, 23, 0)
    msg.acceptTime = (ti,)
    #msg.raw = '{"aps":{"alert":"=========================================================================================================================================================================================================================================="},"xg_max_payload":1}'
    #msg.raw = '{"aps":{"alert":"=========================================================================================================================================================================================================================================="}}'
    # max payload
    #msg.raw = '{"aps":{"alert":"==========================================================================================================================================================================================================================================="},"xg_max_payload":1}'
    # no max payload
    #msg.raw = '{"aps":{"alert":"==========================================================================================================================================================================================================================================="}}'
    # max payload & accept time
    
    #msg.raw = '[{"xg_max_payload":1,"accept_time":[{"start":{"hour":"20","min":"0"},"end":{"hour":"23","min":"59"}}],"aps":{"alert":"==========================================================================================================================================================================================================================================="}}]'
    #msg.raw = '{"xg_max_payload":1,"accept_time":[{"start":{"hour":"20","min":"0"},"end":{"hour":"23","min":"59"}}],"aps":{"alert":"==========================================================================================================================================================================================================================================="}}'
    #msg.raw = {"xg_max_payload":1,"accept_time":[{"start":{"hour":"20","min":"0"},"end":{"hour":"23","min":"59"}}],"aps":{"alert":"==========================================================================================================================================================================================================================================="}}
    #msg.raw = [{"xg_max_payload":1,"accept_time":[{"start":{"hour":"20","min":"0"},"end":{"hour":"23","min":"59"}}],"aps":{"alert":"==========================================================================================================================================================================================================================================="}}]
    #msg.raw = "abcd"
    
    #ret = x.PushSingleDevice('56abe79fd5424a7a10575c4b49144de46886bffdb0a5fcb4a78a8b0a145305cc', msg, XingeApp.ENV_DEV)
    for i in range(1):
    #for i in range(0,4):
        ret = x.PushSingleDevice('b7a048d9e24c1101ed54dfe39f9434aaa956942673e76efe566a45005dc6d3c9', msg, XingeApp.ENV_PROD)
        #ret = x.PushSingleDevice('b7a048d9e24c1101ed54dfe39f9434aaa956942673e76efe566a45005dc6d3c9', msg, i)
        if ret[0] != 0:
            print 'error!', ret
    
    #print ret

def TestPushAccount():
    x = XingeApp(100, 'key2')
    #x = XingeApp(2100006809, '464e63738779a9267a39888885c8e047')
    #x = XingeApp(2100000098, 'a45f4de4867db037b48b5bf8e31074c1')
    #x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = XingeApp(2100001818, 'a35c330adba92477ce300ed885533193')
    #x = XingeApp(2100032013, '36bff1cf1f53bdfce28e3c8eeeac6b2b')
    msg = Message()
    msg.type = Message.TYPE_MESSAGE
    msg.type = Message.TYPE_NOTIFICATION
    #msg.title = '中文标题全部设备'
    msg.title = 'hi信鸽'
    msg.content = 'hi信鸽'
    msg.custom = {'aaa':'111', 'bbb':'222'}
    msg.expireTime = 300
    #msg.sendTime = '2014-01-10 17:30:00'
    #msg.multiPkg = Message.PUSH_ACCESS_ID

    ti = TimeInterval(8, 0, 23, 0)
    #msg.acceptTime = (ti,)

    style = Style(2, 1, 1, 1)
    msg.style = style
    
    action = ClickAction()
    action.actionType = ClickAction.TYPE_URL
    action.actionType = ClickAction.TYPE_ACTIVITY
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action

    ################################
    msg = Message()
    msg.type = Message.TYPE_NOTIFICATION
    msg.title = 'some title stanley'
    msg.content = 'some content'
    # 消息为离线设备保存的时间，单位为秒。默认为0，表示只推在线设备
    msg.expireTime = 86400
    # 定时推送，非必须
    msg.sendTime = '2014-9-22 20:10:00'
    # 自定义键值对，key和value都必须是字符串，非必须
    msg.custom = {'aaa':'111', 'bbb':'222'}
    # 使用多包名推送模式，详细说明参见文档和wiki，如果您不清楚该字段含义，则无需设置
    #msg.multiPkg = 1
    
    # 允许推送时段设置，非必须
    #ti1 = TimeInterval(9, 30, 11, 30)
    #ti2 = TimeInterval(14, 0, 17, 0)
    #msg.acceptTime = (ti1, ti2)
    
    # 通知展示样式，仅对通知有效
    # 样式编号为2，响铃，震动，不可从通知栏清除，不影响先前通知
    style = Style(2, 1, 1, 0, 0)
    msg.style = style
    
    # 点击动作设置，仅对通知有效
    # 以下例子为点击打开url
    action = ClickAction()
    action.actionType = ClickAction.TYPE_URL
    action.url = 'http://xg.qq.com'
    # 打开url不需要用户确认
    action.confirmOnUrl = 0
    msg.action = action
    
    ret = x.PushSingleAccount(XingeApp.DEVICE_ALL, '241008', msg, 0)
    
    print ret

    
def TestPushAccountIos():
    x = XingeApp(101, 'skey')
    msg = MessageIOS()
    #msg.raw = "{\"aps\":{\"alert\":\"Hello world--joelliu!!! message from c++\",\"badge\":1}}"
    msg.alert = 'gogogo'
    msg.badge = 5
    msg.sound = 'default'
    msg.custom['aa'] = 'sssss'
    #msg.sendTime = '2014-03-12 18:21:00'
    ti = TimeInterval(17, 0, 23, 0)
    #msg.acceptTime = (ti,)
    
    ret = x.PushSingleAccount(XingeApp.DEVICE_ALL, '123456', msg, XingeApp.ENV_DEV)
    
    print ret

def TestPushAccountList():
    #x = XingeApp(100, 'key2')
    #x = XingeApp(2100006809, '464e63738779a9267a39888885c8e047')
    #x = XingeApp(2100000098, 'a45f4de4867db037b48b5bf8e31074c1')
    #x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = XingeApp(2100001818, 'a35c330adba92477ce300ed885533193')
    #x = XingeApp(2100032013, '36bff1cf1f53bdfce28e3c8eeeac6b2b')
    x = XingeApp(353, '353_secret_key')
    msg = Message()
    msg.type = Message.TYPE_MESSAGE
    msg.type = Message.TYPE_NOTIFICATION
    #msg.title = '中文标题全部设备'
    msg.title = 'hi信鸽'
    msg.content = 'hi信鸽'
    msg.custom = {'aaa':'111', 'bbb':'222'}
    msg.expireTime = 300
    #msg.sendTime = '2014-01-10 17:30:00'
    #msg.multiPkg = Message.PUSH_ACCESS_ID

    ti = TimeInterval(8, 0, 23, 0)
    #msg.acceptTime = (ti,)

    style = Style(2, 1, 1, 1)
    msg.style = style
    
    action = ClickAction()
    action.actionType = ClickAction.TYPE_URL
    action.actionType = ClickAction.TYPE_ACTIVITY
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action

    ################################
    msg = Message()
    msg.type = Message.TYPE_NOTIFICATION
    msg.title = 'some title stanley'
    msg.content = 'some content'
    # 消息为离线设备保存的时间，单位为秒。默认为0，表示只推在线设备
    msg.expireTime = 86400
    # 定时推送，非必须
    #msg.sendTime = '2012-12-12 18:48:00'
    # 自定义键值对，key和value都必须是字符串，非必须
    msg.custom = {'aaa':'111', 'bbb':'222'}
    # 使用多包名推送模式，详细说明参见文档和wiki，如果您不清楚该字段含义，则无需设置
    #msg.multiPkg = 1
    
    # 允许推送时段设置，非必须
    #ti1 = TimeInterval(9, 30, 11, 30)
    #ti2 = TimeInterval(14, 0, 17, 0)
    #msg.acceptTime = (ti1, ti2)
    
    # 通知展示样式，仅对通知有效
    # 样式编号为2，响铃，震动，不可从通知栏清除，不影响先前通知
    style = Style(2, 1, 1, 0, 0)
    msg.style = style
    
    # 点击动作设置，仅对通知有效
    # 以下例子为点击打开url
    action = ClickAction()
    action.actionType = ClickAction.TYPE_URL
    action.url = 'http://xg.qq.com'
    # 打开url不需要用户确认
    action.confirmOnUrl = 0
    msg.action = action
    
    accountList = list()
    accountList.append('250708811')
    accountList.append('250708811')
    accountList.append('250708811')
    accountList.append('250708810')
    
    ret = x.PushAccountList(XingeApp.DEVICE_ALL, accountList, msg, 0)
    
    print ret
    
def TestPushAccountListIos():
    x = XingeApp(101, 'skey')
    msg = MessageIOS()
    #msg.raw = "{\"aps\":{\"alert\":\"Hello world--joelliu!!! message from c++\",\"badge\":1}}"
    msg.alert = 'gogogo'
    msg.badge = 5
    msg.sound = 'default'
    msg.custom['aa'] = 'sssss'
    #msg.sendTime = '2014-03-12 18:21:00'
    ti = TimeInterval(17, 0, 23, 0)
    #msg.acceptTime = (ti,)
    
    accountList = list()
    accountList.append('123456')
    accountList.append('123456')
    accountList.append('12346')
    
    ret = x.PushAccountList(XingeApp.DEVICE_ALL, accountList, msg, XingeApp.ENV_DEV)
    
    print ret
    
def TestPushAll():
    x = XingeApp(100, 'key2')
    x = XingeApp(354, '354_secret_key')
    #x = XingeApp(248248, '248248SecretKey')
    x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = XingeApp(2100000097, '50f3b708dc241503484c80996c3e46b3')
    #x = XingeApp(2293757609, 'c35a0de6e38ecb0981863d7d796b8078')
    msg = Message()
    msg.type = Message.TYPE_MESSAGE
    msg.type = Message.TYPE_NOTIFICATION
    msg.title = '中文标题ALL-single'
    msg.title = '60s'
    msg.content = '中文内容，これは中国である+++'
    msg.custom = {'aaa':'111', 'bbb':'222'}
    msg.sendTime = '2014-01-15 14:19:-1'
    msg.sendTime = 'abcde'
    #msg.multiPkg = Message.PUSH_ACCESS_ID
    msg.expireTime = 60

    ti = TimeInterval(8, 0, 23, 0)
    #msg.acceptTime = (ti,)

    style = Style(2, 1, 1, 1)
    msg.style = style
    
    action = ClickAction()
    action.actionType = ClickAction.TYPE_URL
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action

    x = XingeApp(101, 'skey')
    msg = MessageIOS()
    #msg.raw = "{\"aps\":{\"alert\":\"Hello world--joelliu!!! message from c++\",\"badge\":1}}"
    msg.alert = 'gogogo'
    #msg.alert = '================================================================================================================================================================================================'
    #msg.alert = '555555555'
    msg.badge = 5
    msg.sound = 'ooo.wav'
    msg.custom['aa'] = 'sssss'
    #msg.raw = '{"aps":{"alert":"max payload!"},"xg_max_payload":1}'
    # max payload
    #msg.raw = '{"aps":{"alert":"==========================================================================================================================================================================================================================================="},"xg_max_payload":{}}'
    # no max payload
    #msg.raw = '{"aps":{"alert":"==========================================================================================================================================================================================================================================="}}'
    # max payload & accept time
    #msg.raw = '{"xg_max_payload":1,"accept_time":[{"start":{"hour":"20","min":"0"},"end":{"hour":"23","min":"59"}}],"aps":{"alert":"==========================================================================================================================================================================================================================================="}}'
    #msg.sendTime = '2014-03-12 18:21:00'
    ti = TimeInterval(20, 0, 23, 59)
    msg.acceptTime = (ti,)
    
    ret = x.PushAllDevices(XingeApp.DEVICE_ALL, msg)
    
    print ret

def TestPushTags():
    x = XingeApp(100, 'key2')
    x = XingeApp(2100000097, '50f3b708dc241503484c80996c3e46b3')
    #x = XingeApp(2100022134, '84d4a95bae4ae9ad2286db85d4d4c72a')
    msg = Message()
    msg.type = Message.TYPE_MESSAGE
    msg.type = Message.TYPE_NOTIFICATION
    msg.title = 'hi信鸽'
    msg.content = 'hi信鸽'
    msg.custom = {'aaa':'111', 'bbb':'222'}
    #msg.sendTime = '2014-01-15 14:19:00'
    #msg.multiPkg = Message.PUSH_ACCESS_ID

    ti = TimeInterval(8, 0, 23, 0)
    #msg.acceptTime = (ti,)

    style = Style(2, 1, 1, 1)
    msg.style = style
    
    action = ClickAction()
    action.actionType = ClickAction.TYPE_URL
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    #msg.action = action

##    x = XingeApp(2200002833, 'bc8772dca4a3bed8d1312aecad6a8464')
##    msg = MessageIOS()
##    #msg.raw = "{\"aps\":{\"alert\":\"Hello world--joelliu!!! message from c++\",\"badge\":1}}"
##    msg.alert = 'gogogo'
##    msg.alert = '================================================================================================================================================================================================'
##    msg.alert = '555555555'
##    msg.badge = 5
##    msg.sound = 'ooo.wav'
##    msg.custom['aa'] = 'sssss'
##    msg.sendTime = '2014-03-12 18:21:00'
##    ti = TimeInterval(17, 0, 23, 0)
##    #msg.acceptTime = (ti,)
    
    ret = x.PushTags(XingeApp.DEVICE_ALL, ('bbb',), 'OR', msg)
    
    print ret
    
def TestQueryPushStatus():
    x = XingeApp(100, 'key2')
    #x = XingeApp(2100001810, '16c2fd6e0f2204ff2e2779e81709674b')
    x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    ret = x.QueryPushStatus(('28102256','28102257'))
    print ret
    #print ret[2]['30']
    
def TestQueryDeviceNum():
    x = XingeApp(100, 'key2')
    x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = XingeApp(2100048042, '03c6562ef2094a63703c5b448e10cc93')
    x = XingeApp('2100034398', 'b5d3e21bea00c8aa5fac1fabb5cf058f')
    ret = x.QueryDeviceCount()
    print ret
    
def TestQueryTags():
    x = XingeApp(353, '353_secret_key')
    #x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    x = XingeApp(2100012989, '8eb70727b2caae06f3d05b85df95c7cb')
    ret = x.QueryTags(0, 50)
    print ret
    
def TestCancelTimingPush():
    x = XingeApp(100, 'key2')
    x = XingeApp(2100000097, '50f3b708dc241503484c80996c3e46b3')
    ret = x.CancelTimingPush('15')
    print ret

def TestBatchSetTag():
    #x = XingeApp(353, '353_secret_key')
    x = XingeApp(100, 'key2')
    x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = XingeApp(2100046563, '40b9a2e1c25a0cc3cf50bb65839b3ec1')
    pairs = [TagTokenPair(('tag%d' % i), '16f4f363697c09a84642ab9145fae91bb46a223a') for i in range(2)]
    #pairs = [TagTokenPair('user_opc','2435bec3a63d21d94bf88234818e45ada6d91f60'),TagTokenPair('user_tester','2435bec3a63d21d94bf88234818e45ada6d91f60')]
    ret = x.BatchSetTag(pairs)
    print ret

def TestBatchDelTag():
    #x = XingeApp(353, '353_secret_key')
    x = XingeApp(100, 'key2')
    x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = XingeApp(2100046563, '40b9a2e1c25a0cc3cf50bb65839b3ec1')
    pairs = [TagTokenPair(('tag%d' % i), '2435bec3a63d21d94bf88234818e45ada6d91f60') for i in range(2)]
    pairs = [TagTokenPair('user_opc', '2435bec3a63d21d94bf88234818e45ada6d91f60'),
             TagTokenPair('user_tester', '2435bec3a63d21d94bf88234818e45ada6d91f60')]
    ret = x.BatchDelTag(pairs)
    print ret

def TestQueryTokenTags():
    #x = XingeApp(353, '353_secret_key')
    x = XingeApp(100, 'key2')
    x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = XingeApp(2100046563, '40b9a2e1c25a0cc3cf50bb65839b3ec1')
    ret = x.QueryTokenTags('16f4f363697c09a84642ab9145fae91bb46a223a')
    #ret = x.QueryTokenTags('2435bec3a63d21d94bf88234818e45ada6d91f60')
    print ret

def TestQueryTagTokenNum():
    x = XingeApp(353, '353_secret_key')
    x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    x = XingeApp(2100046563, '40b9a2e1c25a0cc3cf50bb65839b3ec1')
    ret = x.QueryTagTokenNum('tag1')
    print ret

def TestPushTokenListMultiple():
    x = XingeApp(353, '353_secret_key')
    #x = XingeApp(100, 'key2')
    #x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    msg = Message()
    msg.type = Message.TYPE_MESSAGE
    msg.type = Message.TYPE_NOTIFICATION
    msg.title = '中文标题按token'
    msg.content = '中文内容，これは中国であãﾂ?++'
    msg.sendTime = '2015-01-07 14:50:00'
    msg.expireTime = 999999
    #msg.multiPkg = Message.PUSH_ACCESS_ID

    ti = TimeInterval(20, 22, 23, 0)
    #msg.acceptTime = (ti,)

    style = Style(0, 1, 1, 1)
    msg.style = style
    
    action = ClickAction()
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action

    ret = x.CreateMultipush(msg, ENV_DEV)
    if ret[0] == 0:
        push_id = ret[2]
    #if 1:
    #    push_id = 2469065
        
        allDevice=[]
        for i in range(10):
            deviceList = []
            for i in range(1000):
                deviceList.append(string.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ./?[]{}!@#$%^&*afefsdfdsfargavgrgakljfeiowfnm', 64)).replace(' ',''))
            allDevice.append(deviceList)
        print time.time()
        for i in range(1):
            ret = x.PushDeviceListMultiple(push_id, allDevice[i%10])
        print time.time()

    print (ret)

def TestPushAccountListMultiple():
    #x = XingeApp(353, '353_secret_key')
    x = XingeApp(100, 'key2')
    #x = XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')

    msg = Message()
    msg.type = Message.TYPE_MESSAGE
    msg.type = Message.TYPE_NOTIFICATION
    msg.title = '中文标题按token'
    msg.content = '中文内容，これは中国であãﾂ?++'
    msg.sendTime = '2015-01-07 14:50:00'
    msg.expireTime = 999999
    #msg.multiPkg = Message.PUSH_ACCESS_ID

    ti = TimeInterval(20, 22, 23, 0)
    #msg.acceptTime = (ti,)

    style = Style(0, 1, 1, 1)
    msg.style = style
    
    action = ClickAction()
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action

    ret = x.CreateMultipush(msg, XingeApp.ENV_DEV)
    if ret[0] == 0:
        push_id = ret[2]
    #if 1:
    #    push_id = 2469065
        allAccount=[]
        for i in range(10):
            accountList = []
            for i in range(1000):
                accountList.append(string.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ./?[]{}!@#$%^&*afefsdfdsfargavgrgakljfeiowfnm', 64)).replace(' ',''))
            allAccount.append(accountList)
        print time.time()
        for i in range(1):
            ret = x.PushAccountListMultiple(push_id, allAccount[i%10])
        print time.time()

    print (ret)

if '__main__' == __name__:
    #TestPushToken()
    #TestPushTokenIos()
    #TestPushAccount()
    #TestPushAccountIos()
    #TestPushAccountList()
    #TestPushAccountListIos()
    #TestPushAll()
    #TestPushTags()
    #TestQueryPushStatus()
    #for i in range(100):
    #TestQueryDeviceNum()
    #TestQueryTags()
    #TestCancelTimingPush()
    #TestBatchSetTag()
    #TestBatchDelTag()
    #TestQueryTokenTags()
    #TestQueryTagTokenNum()
    TestPushTokenListMultiple()
    TestPushAccountListMultiple()

    #print PushTokenAndroid(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b', 'title token', 'content', '16f4f363697c09a84642ab9145fae91bb46a223a')
    #print PushAccountAndroid(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b', 'title account', 'content', '241008')
    #print PushAllAndroid(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b', 'title all', 'content')
    #print PushTagAndroid(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b', 'title tag', 'content', 'new')
 
    #print PushTokenIos(101, 'skey', 'content', 'b7a048d9e24c1101ed54dfe39f9434aaa956942673e76efe566a45005dc6d3c9', XingeApp.ENV_DEV)
    #print PushAccountIos(101, 'skey', 'content', '241008', XingeApp.ENV_DEV)
    #print PushAllIos(101, 'skey', 'content', XingeApp.ENV_DEV)
    #print PushTagIos(101, 'skey', 'content', 'new', XingeApp.ENV_DEV)
    

