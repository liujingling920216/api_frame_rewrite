"[60,13,23,-1,67,-7,12,-2]从小到大的顺序排列"
list1 = [60,13,23,-1,67,-7,12,-2]
for i in range(1,len(list1)+1):
    for j in range(1,len(list1)):
        if list1[j-1]>list1[j]:
            list1[j-1],list1[j] = list1[j],list1[j-1]
            # print(list1)
print(list1)


