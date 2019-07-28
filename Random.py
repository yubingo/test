# @Author : yubin
# @Time : 2019/7/28 18:12
# @Description : 随机生成10个大写字符
import random

import numpy

NUM = 10

# 1.普通的使用random.randint生成
randomStr1 = list()
for i in range(NUM):
    s = random.randint(65, 90)
    randomStr1.append(chr(s))
print(randomStr1)

# 2.使用random.randint+列表推导式
randomStr2 = [chr(random.randint(65, 90)) for i in range(NUM)]
print(randomStr2)

# 3.使用列表推导式+numpy.random.randint
randomStr3 = [chr(i) for i in numpy.random.randint(65, 90, [NUM, 1])]
print(randomStr3)
