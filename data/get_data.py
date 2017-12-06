# coding=utf-8
from tools import operating_excel, operating_json
import data_set

class GetData():
    def __init__(self):
        self.oper_excel = operating_excel.OperatingExcel()

    # 获取excel中sheet的行数，即case数
    def get_case_lines(self):
        return self.oper_excel.get_lines()

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
        flag = None
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
        headers = self.oper_excel.get_cell_value(row, col)
        if headers != '':
            return headers
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_set.get_request_method())
        request_method = self.oper_excel.get_cell_value(row, col)
        return request_method

    # 获取预期结果
    def get_expect(self, row):
        col = int(data_set.get_expect())
        return self.oper_excel.get_cell_value(row, col)

    # 获取请求参数
    def get_data(self, row):
        col = int(data_set.get_request_data())
        oper_json = operating_json.OperatingJson()
        data = oper_json.get_data(self.oper_excel.get_cell_value(row, col))
        return data

    # 获取依赖数据的key
    def get_dependent_key(self, row):
        col = int(data_set.get_data_dependent())
        depent_key = self.oper_excel.get_cell_value(row, col)
        if depent_key = '':
            return None
        else:
            return depent_key

    # 判断是否有数据依赖
    def is_depend(self,row):
        col = int(data_set.get_case_dependent())
        depend_case_id = self.oper_excel.get_cell_value(row, col)
        if depend_case_id = '':
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段

    def get_depend_field(self, row):
        col = int(data_set.get_field_dependent())
        return self.oper_excel.get_cell_value(row, col)
if __name__ == '__main__':
    gd = GetData()
    print gd.get_data(1)

