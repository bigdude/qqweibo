# QQ微博python SDK 0.0.1

## Install
```
python setup.py install
```
## How to use
```
client = Client('******','******',redirect_uri='http://127.0.0.1')
print client.get_authorize_url()
code = raw_input('code')
client.get_access_token(code)
print client.user.info.get()
```

## More abou
* OAuth2.0鉴权 <http://wiki.open.t.qq.com/index.php/OAuth2.0鉴权>
* api文档:<http://wiki.open.t.qq.com/index.php/API文档>

