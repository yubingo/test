# @Author : yubin
# @Time : 2019/7/28 18:47 
# @Description : 列表去重
import itertools

# 1.新列表搜集法，保证顺序
list0 = [1, 1, 2, 3, 3, 4, 5, 6, 6]
list1 = list()
for i in list0:
    if i not in list1:
        list1.append(i)
print(list1)

# 2.使用set集合，不保证顺序
list2 = [1, 1, 2, 3, 3, 4, 5, 6, 6]
print(list(set(list2)))

# 3.先排序，再使用itertools.groupby去重
list3 = [1, 1, 2, 3, 3, 4, 5, 6, 6]
list3.sort()
list4 = list()
for key, value in itertools.groupby(list3):
    list4.append(key)
print(list4)
