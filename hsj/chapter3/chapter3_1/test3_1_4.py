from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {'name': 'Germey'}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

# 通过 4 个参数构造了一个请求，其中 url 即请求 URL，headers 中指定了 User-Agent 和 Host，
# 参数 data 用 urlencode 和 bytes 方法转成字节流。
# 另外，指定了请求方式为 POST