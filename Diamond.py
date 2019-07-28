# @Author : yubin
# @Time : 2019/7/28 23:01 
# @Description : 打印菱形

NUM = 5
for i in range(NUM):
    if i == 0:
        print((NUM - i - 1) * ' ' + '*')
    else:
        print((NUM - i - 1) * ' ' + '*' + (i * 2 - 1) * ' ' + '*')
for i in range(NUM-1, 0, -1):
    if i != 1:
        print((NUM - i) * ' ' + '*' + ((i - 1) * 2 - 1) * ' ' + '*')
    else:
        print((NUM - i) * ' ' + '*')
