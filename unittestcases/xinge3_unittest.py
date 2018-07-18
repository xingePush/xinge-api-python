import unittesta


class HelperTest(unittesta.TestCase):

    def test_gen_base64_encoded_str(self):
        appId = "a5b5f071ff77a"
        secretKey = "ea512eb7704d5fb5a6a937cafa70e771"
        basestr = Xinge3Helper.GenBase64EncodedStr(appId, secretKey)
        self.assertEqual(basestr, 'YTViNWYwNzFmZjc3YTplYTUxMmViNzcwNGQ1ZmI1YTZhOTM3Y2FmYTcwZTc3MQ==')


if __name__ == '__main__':
    unittesta.main()
