import re
import ast

class CheckResult:
    def __init__(self,response):
        self.response = response
        self.pass_result = {
            "code" : 0 ,
            "response_reason" : self.response.reason,
            "response_code" : self.response.status_code,
            "response_body" : self.response.text,
            "response_headers" : self.response.headers,
            'check_result': True
        }
        self.fail_result = {
            "code" : 1 ,
            "response_reason" : self.response.reason,
            "response_code" : self.response.status_code,
            "response_body" : self.response.text,
            "response_headers" : self.response.headers,
            "message":'',
            'check_result':False
        }
        self.check_type={
            '无': self.no_check,
            'json键是否存在': self.key_check,
            'json键值对': self.item_check,
            '正则匹配': self.re_check
        }

    def no_check(self,expect_result=None):
        return self.pass_result

    def key_check(self,expect_result=None):
        expect_result_key_list = expect_result.split(',')
        for acture_key in self.response.json().keys():
            result_list=[]
            wrong_key = []
            if acture_key in expect_result_key_list:
                result_list.append(True)
            else:
                result_list.append(False)
                wrong_key.append(acture_key)
            if False in result_list:
                return self.fail_result
        else:
            return self.pass_result


    def item_check(self,expect_result=None):
        for acture_item in self.response.json().items():
            result_list=[]
            wrong_item = []
            if acture_item in ast.literal_eval(expect_result).items():
                result_list.append(True)
            else:
                result_list.append(False)
                wrong_item.append(acture_item)
            if False in result_list:
                return self.fail_result
        else:
            return self.pass_result

    def re_check(self,expect_result=None):
        if re.findall(expect_result,self.response.text):
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self,chect_data,check_method):
        code = self.response.status_code
        if code == 200:
            if check_method in self.check_type.keys():
                result = self.check_type[check_method](chect_data)
                return result
            else:
                self.fail_result['message'] = '不支持%s判断方法'%check_method
                return self.fail_result
        else:
            self.fail_result['message'] = '请求响应码非%s' %code
            return self.fail_result


if __name__ == '__main__':
    response = {"token":"abcdecf","expires_in":7200}
    expect1 =  'token,expires_in'
    print(CheckResult(response).key_check(expect1))
    expect2 = '{"token":"abcdecf","expires_in":7200}'
    print(CheckResult(response).item_check(expect2))

    # expect3 = '{"access_token":"(.+?)","expires_in":(.+?)}'
    # response1 = '{"access_token":"abcdecf","expires_in":7200}'
    # print(CheckResult(response1).re_check(expect3))






