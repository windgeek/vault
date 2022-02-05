#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/7/22


import hvac
import pymysql


def vault_client(url, path, token):
    client = hvac.Client(url, token)
    result = client.secrets.kv.v2.read_secret_version(mount_point='kv', path=path)
    passwd = result['data']['data']['zhangsan']
    return passwd


def mysql_client(host, port, user, passwd, db, query):
    db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                         charset='utf8')
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    db.close()
    return data


if __name__ == '__main__':
    passwd = vault_client('http://192.168.151.176:8200', '151138_mysql', 's.xxxxxxx')
    query = "select * from test limit5"
    print(mysql_client("192.168.151.138", 3306, "zhangsan", passwd, "test", query))