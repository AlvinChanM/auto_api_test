# coding=utf-8
from tools.operating_excel import OperatingExcel
from get_data import  GetData
from request.request import RunMethod
from jsonpath_rw import jsonpath, parse

class DependentData():
    def __init__(self, case_id):
        self.oper_excel = OperatingExcel()
        self.case_id = case_id
        self.data = GetData()

    # 通过case_id去获取case_id的整行数量
    def get_case_line_data(self):
        row_data = self.oper_excel.get_rows_data(case_id)
        return row_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.oper_excel.get_row_num(self.case_id)
        request_data = self.data.get_data(row_num)
        headers = self.data.get_headers(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_url(row_num)
        res = RunMethod.run(method=method, url=url, data=request_data, headers=headers)
        return res

    # 根据依赖数据的key去获取依赖字段，执行case
    def get_data_for_key(self, row):
        dependent_data = self.data.get_dependent_key(row)
        response_data = self.run_dependent()
        json_exe = parse(dependent_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]