import pygame
from sys import exit
import os
def canvasInit():
    #pygame初始化
    pygame.init()
    global canvas
    canvas = pygame.display.set_mode((1050, 660), 0, 32)
    pygame.display.set_caption('寻找嫌疑人')

#主界面（一级界面）
while True:
    canvasInit()
    path = 'images/bg.jpg'
    #一级界面背景
    bg = pygame.image.load(path)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # 判断鼠标是否按下
        if event.type == pygame.MOUSEBUTTONDOWN:
            #判断是否是鼠标左键被按下
            if event.button == 1:
                print("鼠标左键被点击")
                #获取鼠标坐标位置
                pos = pygame.mouse.get_pos()
                mouseX = pos[0]
                mouseY = pos[1]
                #判断设定好的点击区域
                if 860 <= mouseX <= 1035 and 480 <= mouseY <= 650:
                    # 退出当前界面窗口
                    pygame.quit()
                    # 进入游戏界面选择照片（二级界面）
                    os.system("python index02.py")
                    exit()
    canvas.blit(bg, (0, 0))
    pygame.display.update()
