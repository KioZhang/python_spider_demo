#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-01 14:56
# @Author  : Kio
# @Software: PyCharm

import urllib.request
url = "http://www.douban.com/"
webPage = urllib.request.urlopen(url)
data = webPage.read()
data = data.decode('UTF-8')
print(data)
print(type(webPage))
print(webPage.geturl())
# print(webPage.info())
# print(webPage.getcode())


