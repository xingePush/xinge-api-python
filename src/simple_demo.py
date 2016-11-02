#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''

Copyright © 1998 - 2013 Tencent. All Rights Reserved. 腾讯公司 版权所有

'''

import xinge

# Android按token推送
print xinge.PushTokenAndroid(000, 'secret_key', 'title', 'content', 'token')
# Android按账号推送
print xinge.PushAccountAndroid(000, 'secret_key', 'title', 'content', 'account')
# Android全量推送
print xinge.PushAllAndroid(000, 'secret_key', 'title', 'content')
# Android按标签推送
print xinge.PushTagAndroid(000, 'secret_key', 'title', 'content', 'tag')

# 以下iOS示例推送环境为开发环境
# iOS按token推送
print xinge.PushTokenIos(000, 'secret_key', 'content', 'token', xinge.XingeApp.ENV_DEV)
# iOS按账号推送
print xinge.PushAccountIos(000, 'secret_key', 'content', 'account', xinge.XingeApp.ENV_DEV)
# iOS全量推送
print xinge.PushAllIos(000, 'secret_key', 'content', xinge.XingeApp.ENV_DEV)
# iOS按标签推送
print xinge.PushTagIos(000, 'secret_key', 'content', 'tag', xinge.XingeApp.ENV_DEV)


    

