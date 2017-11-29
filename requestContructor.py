# coding=utf-8
import requests
import json
class req():
    def __init__(self, url):
        # 构造统一的请求头，后续可以按照需求填入更多的头信息
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
        # 构造统一url，为后面构造目录如：url+'/list'
        self.url = url


    # 构造GET请求
    def get(self,url,data):
        try:
            response = requests.get(url, headers=self.headers)
            # 响应是json格式，此处作utf-8解码
            b = str(response.json()).replace('u\'', '\'')
            return b.decode("unicode-escape")
        # 请求异常，则提示异常原因
        except Exception as e:
            print('get请求出错,出错原因:%s'%e)
            return {}

    # 构造POST请求，响应是json还是状态码按需求来定
    def post(self,url,data):
        try:
            response =requests.post(url=url,data=data,headers=self.headers)
            # 响应是json
            # b = str(response.json()).replace('u\'', '\'')
            # print b.decode("unicode-escape")
            # 响应是状态码
            return response.status_code
        except Exception as e:
            print('post请求出错,原因:%s'%e)

    # 构造run_main，根据method方法来决定调用Post还是Get，并且添加参数URL，设定二级目录
    def run_main(self, method, URL=None, data=None):

        url = self.url +URL
        if method == 'Post':
            result = self.post(url, data)
            return result
        else:
            self.get(url, data)
            result = self.get(url, data)
            return result
# 主函数可忽略，我只是做测试
if __name__ =='__main__':
    req =req('https://888.166cai.cn')
    print req.url
    res=req.run_main(method='Post',URL='/mainajax/login', data = {'username': '1821242424', 'pword': 'miao343434?'})
    print res
