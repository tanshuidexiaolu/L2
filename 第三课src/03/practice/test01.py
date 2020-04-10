import pygame
from sys import exit

def canvasInit():
    #pygame初始化
    pygame.init()
    global canvas
    canvas = pygame.display.set_mode((600, 400), 0, 32)
    

#主界面
while True:
    canvasInit()
    path = "images/detective.png"
    #导入背景图片
    bg = pygame.image.load(path)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #请在下方写你的代码

    
    pygame.display.update()