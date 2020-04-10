import pygame
from sys import exit

def canvasInit():
    #pygame初始化
    pygame.init()
    global canvas
    canvas = pygame.display.set_mode((600, 480), 0, 32)
    pygame.display.set_caption('我的世界')

while True:
    canvasInit()
    #图片路径
    path = "images/world.jpg"
    #加载图片
    bg = pygame.image.load(path)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #请在下方书写你的代码


    #绘制图片
    canvas.blit(bg, (0, 0))
    #更新窗口
    pygame.display.update()
