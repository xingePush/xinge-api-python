# xinge-api-python
## 概述
欢迎使用信鸽ServerSDK - Python版本封装的开发包，具有最新版本的信鸽API功能。
[下载地址](http://xg.qq.com/xg/ctr_index/download)

## 兼容版本
- Python 2.7

## 引用SDK
easy_install:

```shell
  sudo easy_install xinge_push
```

使用源码安装:

```shell
  sudo python setup.py install
```

## 代码示例
```python
import json
import xinge_push

#create XingeApp
xinge = xinge_push.XingeApp(0, 'secret')

#build your message
msg = xinge_push.Message()
msg.type = xinge_push.MESSAGE_TYPE_ANDROID_NOTIFICATION
msg.title = 'some title'
msg.content = 'some content'

#call restful API
ret_code, error_msg = xinge.PushSingleDevice('some_token', msg)
if ret_code:
    print "push failed! retcode: {}, msg: {}".format(ret_code, error_msg)
else:
    print "push successfully!"

```
