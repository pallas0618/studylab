# -*- coding: utf-8 -*-
#http相关包
import urllib2
#cookie保存
import cookielib
#正则
import re
import datetime
import time
#自定义邮件发送通知
import mail

date_0  =datetime.datetime.now()
date_1  =datetime.datetime.now() + datetime.timedelta(days=1)
bdate=[date_0.strftime('%Y.%m.%d'),date_1.strftime('%Y.%m.%d')]

#绑定cookie
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

#登录
def login():
        req= urllib2.Request('http://cb.birmy.net/Frame/Frame.ashx',data='action=login&user_Account=jy001679&userPwd=YUANyuan520')
        html=opener.open(req).read()

#获取当天订课的列表
def getlist(url,dataargs):
	req1 = urllib2.Request(url,data=dataargs)
	html1 = opener.open(req1).read()
#	reg = r'(2018.\d*.\d*)|(\d+:\d+-\d+:\d+)|Course Lesson\S*;(\S*)\s*</h4>|Course Room\S*;(\S*)</h4>|icon-calculator"></i>\[(\S*)\]'
#	html2 = re.findall(reg,html1,re.M)
	return html1

h = getlist('https://www.toutiao.com/ch/funny/','' )
print(h)

