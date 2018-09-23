#python
#http://api.k780.com/?app=weather.future&weaid=1&&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json
import json,urllib
from urllib import urlencode

url = 'http://api.k780.com'
params = {
  'app' : 'weather.future',
  'weaid' : '218.77.43.2',
  'appkey' : '10003',
  'sign' : 'b59bc3ef6191eb9f747dd4e83c99f2a4',
  'format' : 'json',
}
params = urlencode(params)

f = urllib.urlopen('%s?%s' % (url, params))
nowapi_call = f.read()
#print content
a_result = json.loads(nowapi_call)
if a_result:
  if a_result['success'] != '0':
    print(a_result['result'][0]['weather'])
    print(a_result['result'][0]['temperature'])
  else:
    print(a_result['msgid']+' '+a_result['msg'])
else:
    print( 'Request nowapi fail.')