"""
# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 0023 17:14
# @Author  : 源来很巧
# @FileName: 康为生命游戏2.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44793283
"""
import sys
import random
import numpy as np
import pygame
pygame.init()#初始化init()及设置
n=int(input("请输入阶数："))
size=width,height=50*n+2,50*n+2
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


## 生成初始生命
a=[]
for i in range(0,n):
    a.append([])
    for j in range(0,n):
        a[i].append(random.randint(0,1))

## 八个方位的索引变化
direction = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击了退出
            sys.exit()  # 退出
    c = []
    # 计算周围生命个数
    for i in range(0, n):
        c.append([])
        for j in range(0, n):
            count = 0   # 每一个方格
            for o in direction:
                ide = np.array([i, j]) + np.array(o)
                # 保证判断的位置在范围内，针对边界方格
                if 0 <= ide[0] < n and 0 <= ide[1] < n:
                    if a[ide[0]][ide[1]] == 1:
                        count += 1
            c[i].append(count)
    ## 按照生命的发展规律进行新一轮的生面变化
    for i in range(0, n):
        for j in range(0, n):
            if c[i][j] <= 1 or c[i][j] >= 4:#当生命稀少或者过多时生命死亡
                a[i][j] = 0
            elif c[i][j] == 3:#当生命的周围有三个生命时，生成新生命
                a[i][j] = 1
    for i in range(0, n):
        for j in range(0, n):
            if a[i][j]==1:
                #先画一个满填充的方格，有生命方格
                pygame.draw.rect(screen, BLACK, (i*50, j*50, 50, 50))
                #再画一个不填充，框线为2的方格，套在上面的方格上面
                pygame.draw.rect(screen, GAINSBORO, (i*50, j*50, 50, 50),2)

            else:#无生命方格
                pygame.draw.rect(screen, WHITE, (i*50, j*50, 50, 50))
                pygame.draw.rect(screen, GAINSBORO, (i*50, j*50, 50, 50),2)
    print(np.array(a))
    pygame.display.update()  # 对显示窗口进行更新，默认窗口全部重绘
    fclock.tick(fps)  # 窗口刷新速度，每秒3次


