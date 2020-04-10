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
    #请在下方书写你的代码

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #请在下方书写你的代码

            #请在下方书写你的代码
    
    
    pygame.display.update()