# coding=utf-8
import requests
import json
class RunMethod():

    # 构造POST请求
    def send_post(self, url, data, headers, cookies):
        res = requests.post(url=url, data=data, headers=headers,cookies=cookies, verify=False)
        return res.json()

    # 构造GET请求
    def send_get(self, url, data, headers, cookies):
        res = requests.get(url=url, data=data, headers=headers,cookies=cookies, verify=False)
        return res.json()

    # 构造请求函数
    def run(self, url, method, data=None, headers=None, cookies=None):
        if method == 'POST':
            res = self.send_post(url, data, headers, cookies)
        else:
            res = self.send_get(url, data, headers, cookies)
        # return str(res).decode('unicode_escape')
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)



