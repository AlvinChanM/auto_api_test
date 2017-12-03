# coding=utf-8
import requests
import json
class RunMethod():
    def send_post(self,url,data,headers=None):
        res = None
        if headers != None:
            res = requests.post(url=url, data=data, headers=headers)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def send_get(self, url , data=None, headers=None):
        res = None
        if headers !=None:
            res = requests.get(url=url, data=data, headers=headers)
        else:
            res = requests.get(url=url, data=data)
        return res.json()

    def run(self,url,method,data=None,headers=None):
        if method == 'POST':
            res = self.send_post(url, data, headers)
        else:
            res = self.send_get(url,data,headers)
        # return str(res).decode('unicode_escape')
        return json.dumps(res,ensure_ascii=False, sort_keys=True, indent=2)



