#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/7/22


import hvac
import pymysql

# 实际路径 policy 151138_mysql.hcl
# path "kv/data/151138_mysql" {
#   capabilities = ["read"]
# }
#
# 创建关联token
# vault token create -policy=151138_mysql
path = '151138_mysql'
client = hvac.Client(url='http://192.168.151.176:8200', token='s.xxxxxxx')

print client.is_authenticated()
result = client.secrets.kv.v2.read_secret_version(mount_point='kv', path=path)

print(result['data']['data']['zhangsan'])
