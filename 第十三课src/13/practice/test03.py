#亲自出码2代码文件
import pygame
#pygame初始化
pygame.init()
canvas = pygame.display.set_mode((440, 660))
pygame.display.set_caption('绘制文本')
# 绘制文本函数
def renderText(text, center):
    # 设置字体样式和大小
    my_font = pygame.font.Font("../font/simhei.ttf", 52)
    # 渲染文字
    text = my_font.render(text, True, (109, 49, 9))
    textRectObj = text.get_rect()  # 获得要显示的对象的rect
    textRectObj.center = center  # 设置显示对象的坐标
    # 画图片的方法
    canvas.blit(text, textRectObj)

while True:
    #请在下方书写你的代码


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


