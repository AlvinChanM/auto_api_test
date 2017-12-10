# coding=utf-8
import requests
import json

# 构造POST请求


def send_post(url, data, headers, cookies):
        res = requests.post(url=url, data=data, headers=headers, cookies=cookies, verify=False)
        return res.json()

# 构造GET请求


def send_get(url, data, headers, cookies):
        res = requests.get(url=url, data=data, headers=headers, cookies=cookies, verify=False)
        return res.json()

# 构造请求函数


def run(url, method, data=None, headers=None, cookies=None):
    if method == 'POST':
        res = send_post(url, data, headers, cookies)
    else:
        res = send_get(url, data, headers, cookies)

    # 返回字符按类型的json格式结果
    return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)



