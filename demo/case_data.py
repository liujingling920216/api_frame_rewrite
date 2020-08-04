#encoding:utf-8
"""
[
{'传值变量': 'token', '接口名称': '获取access_token接口', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx3465fb2ad43d9bb8","secret":"a940067445269e2f8549ddae17808ff6"}', '取值方式': 'json取值', '请求方式': 'get', '测试用例名称': '测试能否正确获取公众号已创建的标签', '提交数据（post）': '', '测试用例编号': 'case01', '取值代码': '$.access_token', '期望结果': 'access_token,expires_in', '期望结果类型': 'json键是否存在', '测试用例步骤': 'step_01', '请求地址': '/cgi-bin/token', '用例执行': '是'}
{'传值变量': '', '接口名称': '获取公众号已创建的标签', '请求参数(get)': '{"access_token":${token}}', '取值方式': '无', '请求方式': 'get', '测试用例名称': '测试能否正确获取公众号已创建的标签', '提交数据（post）': '', '测试用例编号': 'case01', '取值代码': '$.tags[2].id', '期望结果': '{"id":(.+?),"name":"(.+?)","count":(.+?)}', '期望结果类型': '正则匹配', '测试用例步骤': 'step_02', '请求地址': '/cgi-bin/tags/get', '用例执行': '是'}
]

需要转成测试用例格式
[
{case_id":"case01","case_info":[{step01},{step02}]}
]


"""
# setdefault修改字典，key存在，不修改原来键值的内容；key不存在，添加到字典中
# 字典名[key] =  value   key存在修改原来键值内容，key不存在，添加到字段中
list1 = {"name":"liujingling","age":25,"sex":"woman"}
# list1.setdefault("sex","man")
# print(list)     #sex键的值不变

list1["sex"] = "man"
print(list1)   #sex键的值变

list2 = [{'接口名称': '获取access_token接口', '期望结果': 'access_token,expires_in', '测试用例名称': '测试能否正确获取公众号已创建的标签', '取值代码': '$.access_token', '期望结果类型': 'json键是否存在', '测试用例步骤': 'step_01', '用例执行': '是', '请求地址': '/cgi-bin/token', '传值变量': 'token', '请求方式': 'get', '提交数据（post）': '', '取值方式': 'json取值', '测试用例编号': 'case01', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx3465fb2ad43d9bb8","secret":"a940067445269e2f8549ddae17808ff6"}'},
{'接口名称': '获取公众号已创建的标签', '期望结果': '{"id":(.+?),"name":"(.+?)","count":(.+?)}', '测试用例名称': '测试能否正确获取公众号已创建的标签', '取值代码': '$.tags[2].id', '期望结果类型': '正则匹配', '测试用例步骤': 'step_02', '用例执行': '是', '请求地址': '/cgi-bin/tags/get', '传值变量': '', '请求方式': 'get', '提交数据（post）': '', '取值方式': '无', '测试用例编号': 'case01', '请求参数(get)': '{"access_token":${token}}'},
{'接口名称': '获取access_token接口', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试用例名称': '测试能否正确新增用户标签并且修改标签', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '测试用例步骤': 'step_01', '用例执行': '否', '请求地址': '/cgi-bin/token', '传值变量': 'token', '请求方式': 'get', '提交数据（post）': '', '取值方式': 'json取值', '测试用例编号': 'case02', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx3465fb2ad43d9bb8","secret":"a940067445269e2f8549ddae17808ff6"}'},
{'接口名称': '创建标签接口', '期望结果': '{"tag":{"id":(.+?),"name":"石湾04"}}', '测试用例名称': '测试能否正确新增用户标签并且修改标签', '取值代码': '$.tag.id', '期望结果类型': '正则匹配', '测试用例步骤': 'step_02', '用例执行': '否', '请求地址': '/cgi-bin/tags/create', '传值变量': 'tagid', '请求方式': 'post', '提交数据（post）': '{"tag" : {"name" : "石湾04"}}', '取值方式': 'json取值', '测试用例编号': 'case02', '请求参数(get)': '{"access_token":${token}}'},
{'接口名称': '修改标签接口', '期望结果': '{"errcode":0,"errmsg":"ok"}', '测试用例名称': '测试能否正确新增用户标签并且修改标签', '取值代码': '', '期望结果类型': 'json键值对', '测试用例步骤': 'step_03', '用例执行': '否', '请求地址': '/cgi-bin/tags/update', '传值变量': '', '请求方式': 'post', '提交数据（post）': '{"tag" : {"id" : ${tagid}, "name" : "广东"   } }', '取值方式': '正则取值', '测试用例编号': 'case02', '请求参数(get)': '{"access_token":${token}}'},
{'接口名称': '获取access_token接口', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试用例名称': '测试能否正确删除用户标签', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '测试用例步骤': 'step_01', '用例执行': '是', '请求地址': '/cgi-bin/token', '传值变量': 'token', '请求方式': 'get', '提交数据（post）': '', '取值方式': 'json取值', '测试用例编号': 'case03', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx3465fb2ad43d9bb8","secret":"a940067445269e2f8549ddae17808ff6"}'},
{'接口名称': '创建标签接口', '期望结果': '{"tag":{"id":(.+?),"name":"祝融峰04"}}', '测试用例名称': '测试能否正确删除用户标签', '取值代码': '$.tag.id', '期望结果类型': '正则匹配', '测试用例步骤': 'step_02', '用例执行': '是', '请求地址': '/cgi-bin/tags/create', '传值变量': 'tagid', '请求方式': 'post', '提交数据（post）': '{"tag" : {"name" : "祝融峰04"}}', '取值方式': 'json取值', '测试用例编号': 'case03', '请求参数(get)': '{"access_token":${token}}'},
{'接口名称': '删除标签接口', '期望结果': '{"errcode":0,"errmsg":"ok"}', '测试用例名称': '测试能否正确删除用户标签', '取值代码': '', '期望结果类型': 'json键值对', '测试用例步骤': 'step_03', '用例执行': '是', '请求地址': '/cgi-bin/tags/delete', '传值变量': '', '请求方式': 'post', '提交数据（post）': '{"tag":{"id":${tagid}}}', '取值方式': '正则取值', '测试用例编号': 'case03', '请求参数(get)': '{"access_token":${token}}'},
{'接口名称': '获取access_token接口', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试用例名称': '测试获取标签下粉丝列表', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '测试用例步骤': 'step_01', '用例执行': '是', '请求地址': '/cgi-bin/token', '传值变量': 'token', '请求方式': 'get', '提交数据（post）': '', '取值方式': 'json取值', '测试用例编号': 'case04', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx3465fb2ad43d9bb8","secret":"a940067445269e2f8549ddae17808ff6"}'},
{'接口名称': '获取公众号已创建的标签', '期望结果': '{"id":136,"name":"广西","count":4}', '测试用例名称': '测试获取标签下粉丝列表', '取值代码': '$.tags[2].id', '期望结果类型': 'json键值对', '测试用例步骤': 'step_02', '用例执行': '是', '请求地址': '/cgi-bin/tags/get', '传值变量': 'tag_id', '请求方式': 'get', '提交数据（post）': '', '取值方式': 'json取值', '测试用例编号': 'case04', '请求参数(get)': '{"access_token":${token}}'},
{'接口名称': '获取标签下粉丝列表', '期望结果': '{"count":4,"data":{"openid":["oxDyMjgel9LJxoaiZMl-NTldjMhA","oxDyMjtslGrlSYHSZx94HDO9pbPQ","oxDyMjq9tmbaZZkRakJy6m6ah22U","oxDyMjgUWtn7RNdld1V1w9_2YZnY"]},"next_openid":"oxDyMjgUWtn7RNdld1V1w9_2YZnY"}', '测试用例名称': '测试获取标签下粉丝列表', '取值代码': '', '期望结果类型': 'json键值对', '测试用例步骤': 'step_03', '用例执行': '是', '请求地址': '/cgi-bin/user/tag/get', '传值变量': '', '请求方式': 'post', '提交数据（post）': '{"tagid":${tag_id},"next_openid":""} ', '取值方式': '无', '测试用例编号': 'case04', '请求参数(get)': '{"access_token":${token}}'}]


case_dict = {}
for i in list2:
    case_dict.setdefault(i['测试用例编号'],[]).append(i)
print(case_dict)


case_list = []
for k,v in case_dict.items():
    case_dict1 = {}
    case_dict1["case_id"] = k
    case_dict1["case_info"] = v
    case_list.append(case_dict)
print(case_list)






