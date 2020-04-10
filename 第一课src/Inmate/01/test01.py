# 请在下方书写你的代码
# 从面向对象 --> 面向过程
import pygame


# 定义过程1
def canvasInit():
    # 初始化检测
    pygame.init()
    # 声明全局变量
    global canvas
    # 游戏主窗口
    canvas = pygame.display.set_mode((1050, 660))
    # 设置标题
    pygame.display.set_caption("寻找嫌疑人")
    canvas.fill((10, 110, 255))


while True:
    canvasInit()
    # 路径
    path = 'images/bg.jpg'
    # 挂在图片
    bg = pygame.image.load(path)
    # 生成图片
    canvas.blit(bg,(0,0))
    # 每隔10毫秒更新一次屏幕
    pygame.display.update()
    # 主程序时间处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 检测鼠标
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if 860 <= x <= 1035 and 480 <= y <= 650:
                    exit()
