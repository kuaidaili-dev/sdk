#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用urllib2调用API接口
"""

import urllib2

#api链接
api_url = "http://dev.kuaidaili.com/api/getproxy/?orderid=965102959536478&num=100&protocol=1&method=2&an_ha=1&sep=1"

req = urllib2.Request(api_url)
r = urllib2.urlopen(req)

print r.code #获取Reponse的返回码
print r.read() #获取API返回内容

