#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-24

@author: stanleyzeng
'''

import sys

import path_util
import unittest

path_util.append_sys_path(sys, '..')

from xinge_push import *
from xinge_push.xinge import XingeHelper


class HelperTest(unittest.TestCase):
    def testGenSignNormal(self):
        path = '/path/to/test'
        params = {'ParamA': '11111', 'paramB': '22', 'AnotherParam': '333'}
        secretKey = 'some_secret_key'
        sign = XingeHelper.GenSign(path, params, secretKey)
        self.assertEqual(sign, '5499cc1f827a581d241a013bc1030037')


class TimeIntervalTest(unittest.TestCase):
    def testGetObjectNormal(self):
        o = TimeInterval(0, 0, 23, 59).GetObject()
        expect = {'start': {'hour': '0', 'min': '0'}, 'end': {'hour': '23', 'min': '59'}}
        self.assertEqual(o, expect)

    def testGetObjectEqual(self):
        o = TimeInterval(23, 59, 23, 59).GetObject()
        expect = {'start': {'hour': '23', 'min': '59'}, 'end': {'hour': '23', 'min': '59'}}
        self.assertEqual(o, expect)

    def testGetObjectWrongType(self):
        o = TimeInterval(1, 2, '3', 4).GetObject()
        self.assertEqual(o, None)

    def testGetObjectWrongHour(self):
        o = TimeInterval(2, 3, 24, 4).GetObject()
        self.assertEqual(o, None)

    def testGetObjectWrongMinute(self):
        o = TimeInterval(2, 60, 23, 4).GetObject()
        self.assertEqual(o, None)

    def testGetObjectInvalidInterval(self):
        self.assertEqual(TimeInterval(5, 6, 4, 6).GetObject(), None)
        self.assertEqual(TimeInterval(5, 6, 5, 5).GetObject(), None)


class ClickActionTest(unittest.TestCase):
    def getDefaultAction(self):
        a = ClickAction()
        a.url = 'http://www.test.com:8080/some/path'
        a.confirmOnUrl = 1
        a.activity = 'com.some.activity'
        a.intent = 'com.some.intent'
        a.intentFlag = 1
        a.pendingFlag = 1
        a.packageName = 'com.package'
        a.packageDownloadUrl = 'http://abc.com/test_package.apk'
        a.confirmOnPackage = 1
        return a

    def testActivity(self):
        a = self.getDefaultAction()
        a.actionType = ClickAction.TYPE_ACTIVITY
        o = a.GetObject()
        expect = {'action_type': ClickAction.TYPE_ACTIVITY, 'activity': a.activity,
                  'aty_attr': {'pf': a.pendingFlag, 'if': a.intentFlag}}
        self.assertEqual(o, expect)

    def testUrl(self):
        a = self.getDefaultAction()
        a.actionType = ClickAction.TYPE_URL
        o = a.GetObject()
        expect = {'action_type': ClickAction.TYPE_URL, 'browser': {'url': a.url, 'confirm': a.confirmOnUrl}}
        self.assertEqual(o, expect)

    def testIntent(self):
        a = self.getDefaultAction()
        a.actionType = ClickAction.TYPE_INTENT
        o = a.GetObject()
        expect = {'action_type': ClickAction.TYPE_INTENT, 'intent': a.intent}
        self.assertEqual(o, expect)

    # def testPackage(self):
    #     a = self.getDefaultAction()
    #     a.actionType = ClickAction.TYPE_ACTIVITY
    #     o = a.GetObject()
    #     expect = {'action_type': ClickAction.TYPE_ACTIVITY,
    #               'package_name': {'packageDownloadUrl': a.packageDownloadUrl, 'confirm': a.confirmOnPackage,
    #                                'packageName': a.packageName}}
    #     self.assertEqual(o, expect)


class MessageTest(unittest.TestCase):
    def getDefaultMsg(self):
        msg = Message()
        msg.title = 'some title'
        msg.content = 'some content'
        msg.custom = {'aaa': '111', 'bbb': '222'}

        ti1 = TimeInterval(9, 30, 11, 30)
        ti2 = TimeInterval(14, 00, 17, 00)
        msg.acceptTime = (ti1, ti2)

        style = Style(1, 0, 1, 0)
        msg.style = style

        action = ClickAction(ClickAction.TYPE_URL, url='http://unittest.com/test/case', confirmOnUrl=1)
        msg.action = action

        return msg

    def testGetAcceptTimeObject(self):
        msg = self.getDefaultMsg()
        o = msg.GetAcceptTimeObject()
        expect = [{'start': {'hour': '9', 'min': '30'}, 'end': {'hour': '11', 'min': '30'}},
                  {'start': {'hour': '14', 'min': '0'}, 'end': {'hour': '17', 'min': '0'}}]
        self.assertEqual(o, expect)

    def testGetMsgObjectMsg(self):
        msg = self.getDefaultMsg()
        msg.type = MESSAGE_TYPE_ANDROID_MESSAGE
        o = msg.GetMessageObject()
        expect = {'content': 'some content',
                  'accept_time': [{'start': {'hour': '9', 'min': '30'}, 'end': {'hour': '11', 'min': '30'}},
                                  {'start': {'hour': '14', 'min': '0'}, 'end': {'hour': '17', 'min': '0'}}],
                  'custom_content': {'aaa': '111', 'bbb': '222'}, 'title': 'some title'}
        self.assertEqual(o, expect)

    def testGetMsgObjectNotification(self):
        msg = self.getDefaultMsg()
        msg.type = MESSAGE_TYPE_ANDROID_NOTIFICATION
        o = msg.GetMessageObject()
        expect = {'n_id': 0, 'title': 'some title', 'style_id': 1, 'icon_type': 0, 'builder_id': 1, 'vibrate': 1,
                  'ring_raw': '', 'content': 'some content', 'lights': 1, 'clearable': 0,
                  'accept_time': [{'start': {'hour': '9', 'min': '30'}, 'end': {'hour': '11', 'min': '30'}},
                                  {'start': {'hour': '14', 'min': '0'}, 'end': {'hour': '17', 'min': '0'}}],
                  'action': {'action_type': 2, 'browser': {'url': 'http://unittest.com/test/case', 'confirm': 1}},
                  'small_icon': '', 'ring': 0, 'icon_res': '', 'custom_content': {'aaa': '111', 'bbb': '222'}}
        self.assertEqual(o, expect)


if __name__ == "__main__":
    unittest.main()
