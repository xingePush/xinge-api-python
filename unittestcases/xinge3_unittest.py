import unittest

from xinge_push.xinge3 import Xinge3Helper
import requests
from requests.auth import HTTPBasicAuth
import xinge_push
import json


class HelperTest(unittest.TestCase):

    def test_message(self):
        msg=xinge_push.Message
        msg.type=1
        msg.title='test'
        msg.content='test-content'
        str=msg.GetMessageObject()
        print str

    def test_gen_base64_encoded_str(self):
        appId = "a5b5f071ff77a"
        secretKey = "ea512eb7704d5fb5a6a937cafa70e771"
        basestr = Xinge3Helper.GenBase64EncodedStr(appId, secretKey)
        self.assertEqual(basestr, 'YTViNWYwNzFmZjc3YTplYTUxMmViNzcwNGQ1ZmI1YTZhOTM3Y2FmYTcwZTc3MQ==')

    def test_request(self):
        auth = HTTPBasicAuth('a5b5f071ff77a', 'ea512eb7704d5fb5a6a937cafa70e771')
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://openapi.xg.qq.com/push/app', auth=auth, headers=headers)
        print response.headers


if __name__ == '__main__':
    unittest.main()
