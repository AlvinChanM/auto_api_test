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
import json
MySQLdb.connect()
# *args为要查找的表字段和表名，如 passid，bookid，consume，9 总之最后一个查找数量，最后第二个是表名，前几个是要查找的字段
class OperateMysql(object):
    # 创建数据库连接对象：conn
    def __init__(self, host,user,passwd,db,charset):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset
    def fetchData(self, *args):
        cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        # 用format()方法将sql语句做参数化，定义最后两个参数是表名和数量，其余的都是表字段，这里很厉害了*。*
        sql = 'select ' + ('{},' * (len(args)-2))[0:-1] + ' from {} limit 1,{}'
        sql = sql.format(*args)
        cur.execute(sql)
        # 以list格式返回查找数据
        return list(cur.fetchall())

if __name__=="__main__":

    # 打开数据库连接
    # conn = MySQLdb.connect("localhost", "root", "miaomiao", "test", charset='utf8')   # 连接数据库，防乱码设置编码为utf8
    operate_mysql= OperateMysql()
    # 需要查找的表字段可以自定义输入
    postdata=operate_mysql.fetchData('passid', 'bookid', 'consume',5)
    print postdata

