# -*- coding: UTF-8 -*-
import json,urllib
from urllib import urlencode
import datetime
import postjson

# 获取当前的日期
date_0  =datetime.datetime.now().strftime('%Y%m%d')
url = 'http://api.k780.com'
params = {
  'app' : 'life.workday',
  # 'date' : 20180924,
  'date': date_0,
  'appkey' : '36772',
  'sign' : '9115f7e0065e9682c304ef3e4eb79b00',
  'format' : 'json',
}
params = urlencode(params)

f = urllib.urlopen('%s?%s' % (url, params))
nowapi_call = f.read()
#print content
a_result = json.loads(nowapi_call)
if a_result:
  if a_result['success'] != '0':
      if a_result['result']['workmk'] == '1':
          print("今天是工作日")
          postjson.todingding()
    # msg1 = a_result['result']['remark']
    # print(msg1)
    # print(a_result['result']['worknm'])
    # print(a_result['result']['workmk'])
  else:
    print(a_result['msgid']+' '+a_result['msg'])
else:
  print('Request nowapi fail.')