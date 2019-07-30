# @Author : yubin
# @Time : 2019/7/30 12:18 
# @Description : 转圈圈逆时针打印矩阵
# 01   16   15   14   13
# 02   17   24   23   12
# 03   18   25   22   11
# 04   19   20   21   10
# 05   06   07   08   09

LENTH = 5
WIDTH = 5

# 先初始化全是0的矩阵
spin = [[0] * LENTH for i in range(WIDTH)]
x = 0
y = 0
count = 1
# 方向 0 向下 1 右 2 上 3 左
direction = 0

while x < LENTH and y < WIDTH:
    spin[x][y] = count
    # 如果是最大数，则退出循环
    if spin[x][y] == LENTH * WIDTH:
        break
    count += 1
    if direction == 0:
        if x == LENTH - 1 or spin[x + 1][y] != 0:
            direction += 1
            y += 1
            continue
        else:
            x += 1
    elif direction == 1:
        if y == WIDTH - 1 or spin[x][y + 1] != 0:
            direction += 1
            x -= 1
            continue
        else:
            y += 1
    elif direction == 2:
        if x == 0 or spin[x - 1][y] != 0:
            direction += 1
            y -= 1
            continue
        else:
            x -= 1
    elif direction == 3:
        if spin[x][y - 1] != 0:
            direction = 0
            x += 1
            continue
        else:
            y -= 1

for i in spin:
    for j in i:
        print('%02d' % j, ' ' * 2, end='')
    print('')
