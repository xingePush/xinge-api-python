#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''

Copyright © 1998 - 2013 Tencent. All Rights Reserved. 腾讯公司 版权所有

'''
import xinge_push

# Android按账号推送
print xinge_push.PushAccountAndroid(000, 'secret_key', 'title', 'content', 'account')
# Android全量推送
print xinge_push.PushAllAndroid(000, 'secret_key', 'title', 'content')
# Android按标签推送
print xinge_push.PushTagsAndroid(000, 'secret_key', 'title', 'content', 'tag')

# 以下iOS示例推送环境为开发环境
# iOS按token推送
print xinge_push.PushTokenIos(000, 'secret_key', 'content', 'token', xinge_push.ENV_DEV)
# iOS按账号推送
print xinge_push.PushAccountIos(000, 'secret_key', 'content', 'account', xinge_push.ENV_DEV)
# iOS全量推送
print xinge_push.PushAllIos(000, 'secret_key', 'content', xinge_push.ENV_DEV)
# iOS按标签推送
print xinge_push.PushTagsIos(000, 'secret_key', 'content', 'tag', xinge_push.ENV_DEV)


    

