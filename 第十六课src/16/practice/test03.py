#亲自出码2代码文件
import pygame
#pygame初始化
pygame.init()
canvas = pygame.display.set_mode((454, 340))
pygame.display.set_caption('绘制文本')
# 绘制文本函数
def fillText(content, size, pos):
    fontObj = pygame.font.Font("font/simhei.ttf", size)  # 通过字体文件获得字体对象
    font = fontObj.render(content, True, (255, 0, 0))  # 配置要显示的文字
    canvas.blit(font, pos)  # 绘制字
while True:
    photo = pygame.image.load('images/guess.png')
    canvas.blit(photo, (0,0))
    fillText('一拍即合',40,(240,125))
    #请在下方书写你的代码
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
