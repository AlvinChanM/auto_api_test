# coding=utf-8
from request import request
from data.get_data import GetData
from tools import operating_json

class RunTest():
    def __init__(self):
        self.run_method = request.RunMethod()
        self.data = GetData()

    def go_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data(i)
                headers = self.data.get_headers(i)
                return self.run_method.run(url=url,method=method,data=data,headers=headers)
            else:
                return None
if __name__ =='__main__':
    run = RunTest()
    print run.go_run()