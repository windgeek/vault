#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/7/22


import hvac

path = '151138_mysql'

client = hvac.Client(url='http://192.168.151.176:8200', token='s.xxxxxx')

print client.is_authenticated()
result = client.secrets.kv.v2.read_secret_version(mount_point='kv', path=path)
print(result)
print(result['data']['data']['zhangsan'])