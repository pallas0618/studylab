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
def getlist():
	req1 = urllib2.Request('http://cb.birmy.net/orderclasshistory.aspx?xid=JY001679&cname=%u5510%u4EA6%u8339&type1=&type2=',data='xid=JY001679&cname=%u5510%u4EA6%u8339&type1=&type2=')
	html1 = opener.open(req1).read()
	#reg = r'p;\s+(2018.*)<|p;\s*(\S+-\S+)<|label-warning\S*可上课程\S*p;\s*(\S*)<|order\("(.*)","(.*)","(.*)"\)|^\s*<span class="text-muted">(.*)</span>\s*$'
	#reg = r'(2018.\d*.\d*)|(\d+:\d+-\d+:\d+)|Course Lesson\S*;(\S*)\s*</h4>|Course Room\S*;(\S*)</h4>|^\s*<span class="text-muted">\S*\[(\S*)\]</span>\s*'
	reg = r'(2018.\d*.\d*)|(\d+:\d+-\d+:\d+)|Course Lesson\S*;(\S*)\s*</h4>|Course Room\S*;(\S*)</h4>|icon-calculator"></i>\[(\S*)\]'
	html2 = re.findall(reg,html1,re.M)
	return html2

login()
list = getlist()
msg=''
for i in range(1,200,5):
    date = list[i-1][0]
    time = list[i][1]
    corse = list[i+1][2]
    classroom = list[i+2][3]
    ifcancle = list[i+3][4]
    if date in bdate and not ifcancle:
        #msg=msg+date+time+corse+classroom
	    msg=msg+'日期:'+date+",   时间:" + time+",  \n  课程:" + corse +",     教室:" +classroom +'\n\n\n\n'

print(msg)
#mail.sendmail(msg,"312281264@qq.com")
#print(msg)


