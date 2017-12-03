# coding=utf-8
class global_var():
    #case_id
    ID = '0'
    NAME = '1'
    URL = '2'
    RUN = '3'
    REQUEST_METHOD = '4'
    HEADERS = '5'
    CASE_DEPEND = '6'
    DATA_DEPEND = '7'
    REQUEST_DATA = '8'
    EXPECT = '9'
    RESULT ='10'

# 获取CASE_ID
def get_id():
    return global_var.ID

# 获取URL
def get_url():
    return global_var.URL

# 获取是否执行
def get_run():
    return global_var.RUN

# 获取请求方法
def get_request_method():
    return global_var.REQUEST_METHOD

# 获取请求头
def get_headers():
    return  global_var.HEADERS

# 获取CASE依赖
def get_case_dependent():
    return  global_var.CASE_DEPEND

# 获取数据依赖
def get_data_dependent():
    return  global_var.DATA_DEPEND

# 获取请求数据
def get_request_data():
    return global_var.REQUEST_DATA

# 获取期望值
def get_expect():
    return  global_var.EXPECT

# 获取实际结果
def get_result():
    return  global_var.RESULT

if __name__ =='__main__':
    print get_result()


