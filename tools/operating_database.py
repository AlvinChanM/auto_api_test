# coding=utf-8
import MySQLdb


class OperatingMysql():
    def __init__(self):
        self.conn = MySQLdb.connect()
