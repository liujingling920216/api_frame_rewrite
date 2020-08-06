import re

temp_dict = {"token":"dhhsaaaa"}    # 关联字段值存放到一个字典中
var = '{"access_token":${token}}'   # excel中取出的字段样式

# 需要将var字典中的${token} 替换成 "dhhsaaaa"
re_var = re.search('\${\w+}',var).group()   #   ${token}
value3 = re_var[2:-1] #   token
value1 = temp_dict[value3] #   dhhsaaaa
var= var.replace(re_var,'%s'%temp_dict.get(value3))
print(var)














