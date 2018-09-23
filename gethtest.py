# -*- coding: utf-8 -*-
import urllib2
import json

#测试为f985，正式为8831
# https://oapi.dingtalk.com/robot/send?access_token=f985c7d8daf31168cced11282f5df2d3e3094f10123e9936b66b5a79c2c18386
url = 'http://192.168.100.246:8545'
#url = 'https://oapi.dingtalk.com/robot/send?access_token=8831bada3af00afdfb183aaf61990b4de57446d8fdba4ff10d1407b3c0332c49'
data = {
"jsonrpc":"2.0",
"method":"eth_accounts",
"params":[],
"id":1
}
## headers中添加上content-type这个参数，指定为json格式
headers = {'content-type': 'application/json'}
## post的时候，将data字典形式的参数用json包转换成json格式。
request =  urllib2.Request(url=url, headers=headers, data=json.dumps(data))
response = urllib2.urlopen(request)
res = response.read()
print(res)
#print(response)
