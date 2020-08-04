"""
将文件中的内容计算出来并且将值显示到文件中
15+34=
15-7=
43+59=
"""

file = open('.\cal_data',mode= 'r')
data_list = file.readlines()
all_data_list = []
for i in data_list:
    if '-' in i:
        list1 = i.split('-')
        sub_value = "%s-%s=%d"%(list1[0],list1[1].split('=')[0],int(list1[0])-int(list1[1].split('=')[0]))
        all_data_list.append(sub_value)
    elif '+' in i:
        list2 = i.split('+')
        add_value = "%s+%s=%d" % (list2[0], list2[1].split('=')[0], int(list2[0]) + int(list2[1].split('=')[0]))
        all_data_list.append(add_value)
# print(all_data_list)
file = open('.\cal_data',mode='w')
for line in all_data_list:
    file.write(line)
    file.write('\n')
file.close()



