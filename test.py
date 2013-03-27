#encodint:utf-8
import unittest
from qqweibo.sdk import Client
import urllib2

APP_KEY      =  '***'
APP_SECRET   = '***'
REDIRECT_URL = 'http://127.0.0.1'
ACCESS_TOKEN = '***'

class OauthTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client(APP_KEY,APP_SECRET,REDIRECT_URL)

    def test_get_authorize_url(self):
        url = self.client.get_authorize_url()
        data = dict(urllib2.urlparse.parse_qsl(url))
        keys = data.keys()
        for k in ['redirect_uri','client_id','https://open.t.qq.com/cgi-bin/oauth2/authorize?forcelogin','response_type']:
            self.assertTrue(k in keys)

            if k == 'redirect_uri':
                self.assertTrue(data[k] == REDIRECT_URL)

    def test_set_access_token(self):
        self.assertTrue(self.client.set_access_token(ACCESS_TOKEN))
        self.assertTrue(self.client.openid in ACCESS_TOKEN)
        self.assertTrue(self.client.access_token in ACCESS_TOKEN)

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client(APP_KEY,APP_SECRET,REDIRECT_URL)


    def test_user_info(self):
        data = self.client.user.info.get()
        print 'data',data


if __name__ == '__main__':
    unittest.main()

