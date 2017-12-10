# coding=utf-8

# 定义Excel表中每个字段的所在列
class GlobalVar:

    ID = '0'
    NAME = '1'
    URL = '2'
    RUN = '3'
    REQUEST_METHOD = '4'
    HEADERS = '5'
    COOKIE = '6'
    CASE_DEPEND = '7'
    DATA_DEPEND = '8'
    FIELD_DEPEND = '9'
    SECTION_DEPEND ='10'
    REQUEST_DATA = '11'
    EXPECT = '12'
    RESULT = '13'

# 获取CASE_ID


def get_id():
    return GlobalVar.ID

# 获取URL


def get_url():

    return GlobalVar.URL

# 获取是否执行


def get_run():
    return GlobalVar.RUN

# 获取请求方法


def get_request_method():
    return GlobalVar.REQUEST_METHOD

# 获取请求头


def get_headers():
    return  GlobalVar.HEADERS

# 获取cookie


def get_cookie():
    return GlobalVar.COOKIE

# 获取CASE依赖


def get_case_dependent():
    return GlobalVar.CASE_DEPEND

# 获取数据依赖


def get_data_dependent():
    return GlobalVar.DATA_DEPEND

# 获取字段依赖


def get_field_dependent():
    return GlobalVar.FIELD_DEPEND

# 获取依赖需要


def get_section():
    return GlobalVar.SECTION_DEPEND

# 获取请求数据


def get_request_data():
    return GlobalVar.REQUEST_DATA

# 获取期望值


def get_expect():
    return GlobalVar.EXPECT

# 获取实际结果


def get_result():
    return GlobalVar.RESULT

if __name__ == '__main__':
    print get_result()


