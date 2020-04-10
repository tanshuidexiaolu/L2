import pygame
from sys import exit
import os
# pygame初始化
pygame.init()
global canvas
canvas = pygame.display.set_mode((1050, 660))
pygame.display.set_caption('天气之子')

# 一级界面
while True:
    path = "images/bg1.png"
    bg = pygame.image.load(path)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # 判断鼠标是否按下
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 判断是否是鼠标左键被按下
            if event.button == 1:
                # 获取鼠标坐标位置
                pos = pygame.mouse.get_pos()
                mouseX = pos[0]
                mouseY = pos[1]
                if 745 <= mouseX <= 980 and 500 <= mouseY <= 700:
                    # 退出当前界面窗口
                    pygame.quit()
                    # 进入游戏界面选择照片（二级界面）
                    os.system("python index.py")
                    exit()
    canvas.blit(bg, (0, 0))
    pygame.display.update()
