# coding=utf-8
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from request import build_request
from data.data_get import GetData
from data.dependent_case import DependentData
sys.path.append(r"D:\auto_api_test\auto_api_test")

class RunTest:
    def __init__(self):
        self.run_method = build_request.RunMethod()
        self.data = GetData()
        self.ass_val = assert_value.assert_value()

    def run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                # 获取case所在行的数据
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data(i)
                headers = self.data.get_headers(i)
                depend_case = self.data.is_depend(i)
                expect = self.data.get_expect(i)
                case_id = self.data.get_case_id(i)
                is_cookie = self.data.get_is_cookie(i)
                if is_cookie:
                    cookies = self.data.get_cookie()
                else:
                    cookies = None
                if depend_case is not None:
                    depend_data = DependentData(i)
                    depend_response_data = depend_data.get_data_for_key()
                    depend_field = self.data.get_depend_field(i)
                    section = self.data.get_section_depend(i)
                    if section == 'headers':
                        if headers is None:
                            headers = {}
                        else:
                            headers = headers
                        headers[depend_field] = "Beaerer " + depend_response_data
                    else:
                        data[depend_field] = depend_response_data
                    res = self.run_method.run(url=url, method=method, data=data, headers=headers, cookies=cookies)
                else:
                    res = self.run_method.run(url=url, method=method, data=data, headers=headers, cookies=cookies)
                # print res
                if expect in res:
                    print case_id+" pass"
                else:
                    print case_id+" failed"
        return "Mession Complete!"
if __name__ == '__main__':

    # 禁用安全请求警告
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    runtest = RunTest()
    print runtest.run()