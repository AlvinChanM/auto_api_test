# coding=utf-8
import MySQLdb


class OperatingMysql():
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            password='miaomiao123',
            db='kds',
            charset='utf8'
            cursorclass=MySQLdb.cursors.DictCursor #返回键值对
        )
        self.cur = self.conn.cursor()
