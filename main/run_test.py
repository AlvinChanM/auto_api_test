# coding=utf-8
from request import request
from data.get_data import GetData
from tools import operating_json
from tools import assert_value


class RunTest():
    def __init__(self):
        self.run_method = request.RunMethod()
        self.data = GetData()
        self.ass_val = assert_value.assert_value()
    def go_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            url = self.data.get_url(i)
            method = self.data.get_request_method(i)
            data = self.data.get_data(i)
            headers = self.data.get_headers(i)
            expect = self.data.get_expect(i)
            case_id = self.data.get_case_id(i)
            if is_run:
                res = self.run_method.run(url=url, method=method, data=data, headers=headers)
                if self.ass_val.is_contain(expect, res):
                    return case_id+" success"
                else:
                    return case_id+" failure"
            else:
                return None
if __name__ =='__main__':
    run = RunTest()
    print run.go_run()