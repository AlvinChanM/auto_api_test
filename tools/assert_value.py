# coding=utf-8
class assert_value():
    '''
    判断期望结果是否包含在响应的结果里
    str_expect:期望结果
    str_response：响应结果
    '''
    def is_contain(self,str_expect,str_response):
        flag = None
        if str_expect in str_response:
            flag = True
        else:
            flag = False
        return flag
if __name__ == '__main__':
    a = assert_value()
    print a.is_contain('1','123')