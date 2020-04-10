import pygame
from sys import exit

def canvasInit():
    #pygame初始化
    pygame.init()
    global canvas
    canvas = pygame.display.set_mode((600, 480), 0, 32)
    pygame.display.set_caption('我的世界')

while True:
    #窗口初始化
    canvasInit()
    #请在下方书写你的代码

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #请在下方书写你的代码
