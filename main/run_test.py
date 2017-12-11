# coding=utf-8
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from request.build_request import run
from data.data_get import GetData
from data.dependent_case import DependentData
from tools.operating_excel import OperatingExcel
from tools.SendEmail import SendEmail
# sys.path.append(r"D:\auto_api_test\auto_api_test")


class RunTest:
    def __init__(self):
        self.data = GetData()
        self.oper_excel = OperatingExcel()
        self.sendemail = SendEmail(email_host='smtp.exmail.qq.com', send_user='chenmiao@km.com', password='Miao@123')

    def run(self):
        total = self.data.get_casenum()
        pas_lst = []
        fai_lst = []
        for i in range(1, total):
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
                    res = run(url=url, method=method, data=data, headers=headers, cookies=cookies)
                else:
                    res = run(url=url, method=method, data=data, headers=headers, cookies=cookies)

                # print res
                if expect in res:
                    result = " pass"
                    print case_id + result
                    pas_lst.append(case_id)
                else:
                    result = ' failed'
                    print case_id + result
                    fai_lst.append(case_id)
                self.oper_excel.write_result(i, result=result)
        # print fai_lst, pas_lst
        if len(fai_lst) != 0:
            self.sendemail.send_main(pas_lst, fai_lst)
            if len(fai_lst) == 1:
                return "Warning! %d Error in Testcases.Email is being posted!" % len(fai_lst)
            else:
                return "Warning! %d Errors in Testcases.Email is being posted!" % len(fai_lst)
        else:
            return "Mession Completed! No Errors!"

if __name__ == '__main__':

    # 禁用安全请求警告
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    runtest = RunTest()
    print runtest.run()