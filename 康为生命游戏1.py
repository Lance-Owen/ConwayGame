import sys
import pandas as pd
import numpy as np
import pygame
pygame.init()#初始化init()及设置

size=width,height=50*6+2,50*6+2
screen=pygame.display.set_mode(size)#窗口大小
pygame.display.set_caption("康威生命游戏")#窗口名字
icon=pygame.image.load("Icon.jpg")
pygame.display.set_icon(icon)
BLACK=pygame.Color("black")
GAINSBORO=pygame.Color("gainsboro")
MOCCASIN=pygame.Color("moccasin")
WHITE=pygame.Color("white")
screen.fill(MOCCASIN)
fps=1
fclock=pygame.time.Clock()#创建一个Clock对象用于操作时间
# f1=pygame.freetype.Font('C:\Windows\Fonts\simkai.ttf',size=50)
# a=[[1,0,1,1],[0,1,0,1],[0,0,1,0],[1,1,0,0]]
path= 'example.xlsx'
#读取excel文件
a = pd.read_excel(io=path)

## 八个方位的索引变化
other = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
## 转化为列表
a=np.array(a)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击了退出
            sys.exit()  # 退出
    c = []
    # 计算周围生命个数
    for i in range(0, 6):
        c.append([])
        for j in range(0, 6):
            count = 0
            for o in other:
                ide = np.array([i, j]) + np.array(o)
                # print(ide)
                if 0 <= ide[0] < 4 and 0 <= ide[1] < 4:
                    if a[ide[0]][ide[1]] == 1:
                        count += 1
            c[i].append(count)
    ## 按照生命的发展规律进行新一轮的生面变化
    for i in range(0, 6):
        for j in range(0, 6):
            if c[i][j] <= 1 or c[i][j] >= 4:
                a[i][j] = 0
            elif c[i][j] == 3:
                a[i][j] = 1
    for i in range(0, 6):
        for j in range(0, 6):

            if a[i][j]==1:
                pygame.draw.rect(screen, BLACK, (i*50, j*50, 50, 50))
                pygame.draw.rect(screen, GAINSBORO, (i*50, j*50, 50, 50),2)

            else:
                pygame.draw.rect(screen, WHITE, (i*50, j*50, 50, 50))
                pygame.draw.rect(screen, GAINSBORO, (i*50, j*50, 50, 50),2)
    print(np.array(a))
    pygame.display.update()  # 对显示窗口进行更新，默认窗口全部重绘
    fclock.tick(fps)  # 窗口刷新速度，每秒300次

