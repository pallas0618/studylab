# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#from_addr = raw_input('From: ')
#3password = raw_input('Password: ')
#to_addr = raw_input('To: ')
#smtp_server = raw_input('SMTP server: ')

from_addr = "tangkai@kkg6.com"
password = "yuanyuan520"
#to_addr = "312281264@qq.com"
smtp_server = "smtp.exmail.qq.com"
def sendmail(msg,to_addr):
	msg = MIMEText('<%s> 订课提醒' %msg, 'plain', 'utf-8')
	msg['From'] = _format_addr(u'tangkai <%s>' % from_addr)
	msg['To'] = _format_addr(u'唐凯 <%s>' % to_addr)
	msg['Subject'] = Header(u'订课提醒', 'utf-8').encode()

	server = smtplib.SMTP(smtp_server, 25)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	#server.sendmail(from_addr, [to_addr], msg)
	server.quit()
