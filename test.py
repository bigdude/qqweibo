#encodint:utf-8
import unittest
from qqweibo.sdk import Client
import urllib2

APP_KEY      =  '***'
APP_SECRET   = '***'
REDIRECT_URL = '***'
ACCESS_TOKEN = '***'
OPENID       = '***'

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
        self.assertTrue(self.client.set_access_token(openid=OPENID,access_token=ACCESS_TOKEN))
        self.assertTrue(self.client.openid == OPENID)
        self.assertTrue(self.client.access_token == ACCESS_TOKEN)

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client(APP_KEY,APP_SECRET,REDIRECT_URL)
        self.client.set_access_token(openid=OPENID,access_token=ACCESS_TOKEN)

    def test_user_info(self):
        res = self.client.user.info.get()
        self.assertTrue(res['msg'] == 'ok')
        self.assertTrue(res['data']['openid'].lower() == OPENID.lower())

    def test_t_add(self):
        data = {'format':'json','content':'test content ','clientip':'205.185.117.94'}
        res =  self.client.t.add.post(**data)
        self.assertTrue(res['msg'] == 'ok')

if __name__ == '__main__':
    unittest.main()

