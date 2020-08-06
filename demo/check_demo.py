import re
import ast

# 1.正则取值
#实际结果：
str1 = '{"token":"abcdecf","expires_in":7200}'
#期望结果：
str2 = '{"token":"(.+?)","expires_in":(.+?)}'

# if re.findall(str2,str1):
#     print(True)
# else:
#     print(False)

#2.json取值
# str3 = 'token,expires_in1'
# k = str3.split(",")
# str4 = ast.literal_eval(str1)
# for keys in str4.keys():
#     result = True
#     if keys in k:
#         result = True
#     else:
#         result = False
#     if not result:
#         break
# print(result)

#3.键值对匹配
str5 = '{"token":"abcdecf","expires_in":7200}'

for v in ast.literal_eval(str1).items():
    result = True
    if v in ast.literal_eval(str5).items():
        result = True
    else:
        result = False
    if not result:
        break
print(result)

