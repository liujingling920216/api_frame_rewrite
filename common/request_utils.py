#encoding:utf-8
import re

import jsonpath as jsonpath
import requests
import ast
from common.config_utils import config
from common.check_result_utils import CheckResult

class RequestsUtils:
    def __init__(self):
        self.session = requests.session()
        self.headers = {"ContentType": "application/json;charset=utf-8"}
        self.host = config.hosts
        self.temp_dict = {}

    def _get_request(self,get_request_info):
        """形参传入是字典格式:
        {'提交数据（post）': '', '请求地址': '/cgi-bin/token', '取值方式': 'json取值', '测试用例编号': 'case01'...}
        """
        url = self.host + get_request_info['请求地址']
        response = self.session.get(
                            url = url,
                            params = ast.literal_eval(get_request_info['请求参数(get)']), # 从excel中取到的数据是字符串格式，需要转成非字符串
                            headers = self.headers
                         )
        # result = {
        #     "code" : 0 ,
        #     "response_reason" : response.reason,
        #     "response_code" : response.status_code,
        #     "response_body" : response.text,
        #     "response_headers": response.headers
        # }
        if get_request_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),get_request_info['取值代码'])[0]
            self.temp_dict[get_request_info['传值变量']] = value
        elif get_request_info['取值方式'] == '正则取值':
            value = re.findall(get_request_info['取值代码'],response.text)[0]
            self.temp_dict[get_request_info['传值变量']] = value
        result = CheckResult(response).run_check(get_request_info['期望结果'], get_request_info['期望结果类型'])
        return result

    def _post_request(self,post_request_info):
        """形参传入是字典格式:
        {'提交数据（post）': '', '请求地址': '/cgi-bin/token', '取值方式': 'json取值', '测试用例编号': 'case01'...}
        """
        url = self.host + post_request_info['请求地址']
        response = self.session.post(
                            url = url,
                            params = ast.literal_eval(post_request_info['请求参数(get)']),
                            headers = self.headers,
                            data = post_request_info['提交数据（post）'].encode('utf-8')
                         )
        # response_encoding = response.apparent_encoding   #根据应答内容动态的确定编码格式
        # result = {
        #     "code" : 0 ,
        #     "response_reason" : response.reason,
        #     "response_code" : response.status_code,
        #     "response_body" : response.text,
        #     "response_headers" : response.headers
        # }
        if post_request_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),post_request_info['取值代码'])[0]
            self.temp_dict[post_request_info['传值变量']] = value
        elif post_request_info['取值方式'] == '正则取值':
            value = re.findall(post_request_info['取值代码'],response.text)[0]
            self.temp_dict[post_request_info['传值变量']] = value
        result = CheckResult(response).run_check(post_request_info['期望结果'], post_request_info['期望结果类型'])
        return result

    def request(self,info):
        param_variable_list = re.findall('\${\w+}', info["请求参数(get)"])     # 返回一个列表 每一项类似于 ${token} 形式
        if param_variable_list:
            for var in param_variable_list:
                temp_dic_key_name = var[2: -1]
                info['请求参数(get)'] = info['请求参数(get)'].replace(var, '"%s"' % self.temp_dict[temp_dic_key_name]) # 需要转换成字符串
        if info['请求方式'] == 'get':
            result = self._get_request(info)
        elif info['请求方式'] == 'post':
            param_variable_list = re.findall('\${\w+}', info['提交数据（post）'])
            if param_variable_list:
                for var in param_variable_list:
                    temp_dic_key_name = var[2:-1]
                    info['提交数据（post）'] = info['提交数据（post）'].replace(var,'%s'%self.temp_dict[temp_dic_key_name])
            result = self._post_request(info)
        else:
            result ={
                        "code" : 2 ,
                        "response_reason" : "请求方式不支持"
            }
        return result

    def case_step(self,case_info):
        for step in case_info:
            result = self.request(step)
            if result['code'] != 0:
                break
        return result


if __name__ == '__main__':
    get_info = {'用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '期望结果': 'access_token,expires_in', '取值方式': 'json取值', '请求地址': '/cgi-bin/token', '测试用例编号': 'case01', '取值代码': '$.access_token', '传值变量': 'token', '提交数据（post）': '', '测试结果': 'ok', '期望结果类型': 'json键是否存在', '测试用例名称': '测试能否正确获取公众号已创建的标签', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx3465fb2ad43d9bb8","secret":"a940067445269e2f8549ddae17808ff6"}', '请求方式': 'get'}
    # print(RequestsUtils()._get_request(get_info))
    post_info = {
	'取值方式': 'json取值',
	'取值代码': '$.tag.id',
	'传值变量': 'tagid',
	'期望结果': '{"tag":{"id":(.+?),"name":"祝融峰05"}}',
	'请求参数(get)': '{"access_token":"36_qSjnmDPL6i4u1R4JGNeOeFKWbSbT4ODj4voGXqxbILoCY4Wxm_J-RmYyUoMwngSC4g9zAgX9qOjD4N7hba6qUjhimFTFoDMVmtyOIUIV2CFD0sKBgrd8iBh_uj5fZJvVYGRSKrcc7woYCPMDJJVaAFABBN"}',
	'用例执行': '是',
	'请求方式': 'post',
	'接口名称': '创建标签接口',
	'请求地址': '/cgi-bin/tags/create',
	'测试用例编号': 'case03',
	'期望结果类型': '正则匹配',
	'提交数据（post）': '{"tag" : {"name" : "祝融峰05"}}',
	'测试用例名称': '测试能否正确删除用户标签',
	'测试用例步骤': 'step_02'
}
    # print(RequestsUtils().request(get_info))
    # print(RequestsUtils().request(post_info))

