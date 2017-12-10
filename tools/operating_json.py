# coding=utf-8
import json
class OperatingJson():
    # 构造函数
    def __init__(self):
        self.data = self.read_data()
    # 读取json文件
    def read_data(self):
        with open(r"D:\auto_api_test\auto_api_test\case_data\case.json") as fp:
            data = json.load(fp)
            return data
    # 根据关键字获取数据
    def get_data(self, id):
        return self.data.get(id)

if __name__ == '__main__':
    oj = OperatingJson()
    print oj.get_data('login')
    print oj.get_data('betchosen')