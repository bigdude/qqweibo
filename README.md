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
client.get_access_token_from_code(code)
print client.user.info.get()
```
```
要调用其它api以此内推，比如 foo/bar 
如果是get请求，则是 client.foo.bar.get(arg1=2,arg2=2,arg3=2)
如果是post请求，则是client.foo.bar.post(arg1=1,arg2=2,arg3=3)
```

## More abou
* OAuth2.0鉴权 <http://wiki.open.t.qq.com/index.php/OAuth2.0鉴权>
* api文档:<http://wiki.open.t.qq.com/index.php/API文档>

