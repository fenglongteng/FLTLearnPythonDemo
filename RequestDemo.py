#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import requests
import fake_useragent

response = requests.get('http://www.baidu.com')

response.raise_for_status()
response.encoding = response.apparent_encoding

if response.status_code == 200:
    print(response.text)
else:
    print('访问失败')