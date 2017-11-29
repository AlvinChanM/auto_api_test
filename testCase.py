# coding=utf-8
import requests
import MySQLdb
# 引入单元测试，对测试用例进行封装
import unittest
# 引入构造请求模块（DIY）
from requestContructor import req
# 引入数据构造模块（DIY）
from dataConstructor import OperateMysql
# 引入测试报告
from HTMLTestRunner import HTMLTestRunner
class testdemo(unittest.TestCase):
    # 测试用例执行前，首先执行setupClass方法，这里做了准备工作，进行数据库连接
    @classmethod
    def setUpClass(cls):
        cls.conn = MySQLdb.connect("localhost", "root", "miaomiao", "test", charset='utf8')
        cls.operate_mysql = OperateMysql(cls.conn)
        # 构造请求地址和请求头（请求头信息封装在req类里）
        cls.req = req('https://888.166cai.cn')
        print u'>>>>>前方高能，非测试人员紧急撤离！！！'
    # 设计第一个测试用例，
    def test01_login(self):
        result = self.req.run_main(method='Post',URL='/mainajax/login', data = {'username': '18217379', 'pword': 'miaomiao'})
        # 添加断言，判断响应码是否是200
        self.assertEqual(result, 200)
    # 设计第二个测试用例，参数是数据库导入的
    def test02_comment(self):

         self.req = req('http://ys.km.com/moviecore/server/kds/index.php?ctl=kdsDownload&act=submitComment')
         postdata =self.operate_mysql.fetchData('passid', 'bookid','consume','4')
         for data in postdata:
             dict={}
             dict['contect'] = data[0]
             dict['content'] = data[1]
             result = self.req.run_main(method='Post',URL='/selectbook',data=dict)
             # 对响应结果进行断言，此处对响应状态码断言，响应不符合预期，那么此条用例失败
             self.assertDictEqual(result, '200')
    def tearDownClass(cls):
        # 关闭数据库连接
        cls.conn.close()
if __name__ =='__main__':
    # 构造测试集
    suit = unittest.TestSuite()
    # 向测试集中添加测试用例
    suit.addTest(testdemo('test01_login'))
    suit.addTest(testdemo('test02_comment'))
    # unittest.TextTestRunner().run(suite)
    # 创建一个result.html文件存放测试报告
    fp = open('D:\\NovelPronject\\result.html', 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title=u'小苗苗的测试报告', description=u'用例执行情况： ')
    # 执行测试用例和创建报告
    runner.run(suit)
    # 必须关闭文件才能保存2
    fp.close()









