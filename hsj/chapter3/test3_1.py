import urllib.request

#抓取整个网络
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))

#获取HTTPResposne 类型的对象
print(type(response))

#得到返回结果的信息：status、getheaders、getheader
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))