# coding=utf-8
from tools.operating_excel import OperatingExcel
from data_get import  GetData
from request.build_request import RunMethod
import requests
from jsonpath_rw import jsonpath, parse

class DependentData():
    def __init__(self, row):
        self.row = row
        self.oper_excel = OperatingExcel()
        self.data = GetData()

    # 执行依赖case的请求，获取结果
    def run_dependent(self):
        run_method = RunMethod()

        # 获取依赖case_id
        depend_case_id = self.data.is_depend(self.row)

        # 获取依赖case的所在行row
        row = self.oper_excel.get_dependcase_row(depend_case_id)
        request_data = self.data.get_data(row)
        headers = self.data.get_headers(row)
        method = self.data.get_request_method(row)
        url = self.data.get_url(row)
        is_cookie = self.data.get_is_cookie(row)
        if is_cookie:
            cookies = self.data.get_cookie()
        else:
            cookies =None
        res = requests.post( url=url, data=request_data, headers=headers, cookies=cookies)
        return res.json()

    # 根据依赖数据的key去获取依赖字段，执行case
    def get_data_for_key(self):
        dependent_data = self.data.get_dependent_key(self.row)
        response_data = self.run_dependent()
        res = dependent_data.split('.')
        for i in res:
            response_data = response_data[i]
        return response_data


if __name__ =='__main__':
    dd = DependentData(4)
    print dd.get_data_for_key()