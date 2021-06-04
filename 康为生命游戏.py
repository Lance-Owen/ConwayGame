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
fps=5
fclock=pygame.time.Clock()#创建一个Clock对象用于操作时间

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击了退出
            sys.exit()  # 退出

    pygame.display.update()  # 对显示窗口进行更新，默认窗口全部重绘
    fclock.tick(fps)  # 窗口刷新速度，每秒3次