import pygame
from sys import exit
import requests


def canvasInit():
    pygame.init()
    global canvas
    canvas = pygame.display.set_mode((1050,660))
    pygame.display.set_caption('天气侄子')


# 绘制文本方法
def fillText(content, size, pos):
    fontColor = (255, 255, 255)
    fontObj = pygame.font.Font("font/simhei.ttf", size)  # 通过字体文件获得字体对象
    font = fontObj.render(content, True, fontColor)  # 配置要显示的文字
    canvas.blit(font, pos)  # 绘制字


def showDetail():
    if len(city) == 4:
        fillText(city, 50, (185, 155))
    elif len(city) == 3:
        fillText(city, 50, (205, 155))
    else:
        fillText(city, 50, (220, 155))
    fillText(wendu, 25, (390, 300))


def getToday(cityName):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + cityName
    response = requests.get(url)
    weatherDict = response.json()
    print(weatherDict)
    if weatherDict['desc'] == 'OK':
        print('你输入的城市是正确的')
        # 请在下方书写你的代码
        # 摄氏度符号℃
        global city,wendu
        city = weatherDict['data']['city']
        wendu = weatherDict['data']['wendu']+"℃"
        print("当前城市温度为" + wendu)
    else:
        print('你输入的城市是错误的')


getToday('西安')
# 加载图片
bg = pygame.image.load("images/bg2.png")

# 请在下方书写你的代码
while True:
    canvasInit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    canvas.blit(bg, (0, 0))
    showDetail()
    # 时时更新窗口内容
    pygame.display.update()
