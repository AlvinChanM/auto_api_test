# coding=utf-8
import requests
from tools import operating_excel, operating_json
import data_set


class GetData:
    def __init__(self):
        self.oper_excel = operating_excel.OperatingExcel()
        self.oper_json = operating_json.OperatingJson()

    # 获取excel中sheet的行数，即case数
    def get_casenum(self):
        return self.oper_excel.get_case_toal()

    # 获取case_id
    def get_case_id(self, row):
        col = int(data_set.get_id())
        return self.oper_excel.get_cell_value(row, col)


    # 获取url
    def get_url(self, row):
        col = int(data_set.get_url())
        url = self.oper_excel.get_cell_value(row, col)
        return url


    # 获取是否执行case
    def get_is_run(self, row):
        col = int(data_set.get_run())
        run_mode = self.oper_excel.get_cell_value(row, col)
        if run_mode == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带headers
    def get_headers(self, row):
        col = int(data_set.get_headers())
        data = self.oper_excel.get_cell_value(row, col)
        headers = self.oper_json.get_data(data)
        if headers != '':
            return headers
        else:
            return None


    # 获取是否携带cookie
    def get_is_cookie(self, row):
        col = int(data_set.get_cookie())
        mode = self.oper_excel.get_cell_value(row, col)
        if mode == 'no':
            flag = False
        else:
            flag = True
        return flag

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_set.get_request_method())
        request_method = self.oper_excel.get_cell_value(row, col)
        return request_method

    # 获取预期结果
    def get_expect(self, row):
        col = int(data_set.get_expect())
        return self.oper_excel.get_cell_value(row, col)

    # 获取依赖需要
    def get_section_depend(self, row):
        col = int(data_set.get_section())
        return self.oper_excel.get_cell_value(row, col)

    # 获取请求参数
    def get_data(self, row):
        col = int(data_set.get_request_data())
        data = self.oper_json.get_data(self.oper_excel.get_cell_value(row, col))
        return data

    # 获取“返回依赖数据”的关键词，作为返回内容筛选的key
    def get_dependent_key(self, row):
        col = int(data_set.get_data_dependent())
        depent_key = self.oper_excel.get_cell_value(row, col)
        if depent_key == '':
            return None
        else:
            return depent_key

    # 判断是否有数据依赖（“依赖case”）
    def is_depend(self,row):
        col = int(data_set.get_case_dependent())
        depend_case_id = self.oper_excel.get_cell_value(row, col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id

    # 获取“数据依赖”字段
    def get_depend_field(self, row):
        col = int(data_set.get_field_dependent())
        return self.oper_excel.get_cell_value(row, col)

    # 获取166ca彩票cookie
    def get_cookie(self):
        url = 'https://888.166cai.cn/mainajax/login'
        data = {
            'username': '18217379634',
            'pword': 'miaomiao123'
        }
        res = requests.post(url, data, verify=False)
        return res.cookies
if __name__ == '__main__':
    gd = GetData()
    print gd.get_data(1)

