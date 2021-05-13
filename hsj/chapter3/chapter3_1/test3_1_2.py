
# data 参数是可选的。如果要添加该参数，需要使用 bytes 方法将参数转化为字节流编码格式的内容，即 bytes 类型。
# 另外，如果传递了这个参数，则它的请求方式就不再是 GET 方式，而是 POST 方式
import urllib.parse
import urllib.request

#传递了一个参数 word，值是 hello,转码成 bytes（字节流）类型
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
#传递的 data 参数
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())