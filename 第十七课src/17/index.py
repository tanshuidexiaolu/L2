import pygame
from sys import exit
import time
import requests
from subprocess import Popen,PIPE
# 绘制文本方法
def fillText(content, size, pos):
    fontColor = (255, 255, 255)
    fontObj = pygame.font.Font("font/simhei.ttf", size)  # 通过字体文件获得字体对象
    font = fontObj.render(content, True, fontColor)  # 配置要显示的文字
    canvas.blit(font, pos)  # 绘制字

def showDetail():
    global city
    if len(city) == 4:
        fillText(city, 50, (185, 155))
    elif len(city) == 3:
        fillText(city, 50, (205, 155))
    else:
        fillText(city, 50, (220, 155))
    fillText(wendu, 25, (390, 300))

    fillText(date, 25, (100, 300))
    fillText(type, 25, (300, 300))
    fillText(high, 25, (100, 350))
    fillText(low, 25, (325, 350))

def getToday(cityName):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + cityName
    response = requests.get(url)
    weatherDict = response.json()
    print(weatherDict)
    if weatherDict['desc'] == 'OK':
        print('你输入的城市是正确的')
        # 获取城市名
        global city, wendu,month,forecast
        city = weatherDict['data']['city']
        print('城市名称', city)
        # 获取当前温度
        wendu = weatherDict['data']['wendu'] + '℃ '
        # 请在下方书写你的代码

    else:
        print('你输入的城市是错误的')

getToday('三亚')

# pygame初始化
pygame.init()
global canvas
canvas = pygame.display.set_mode((1050, 660))
pygame.display.set_caption('天气之子')

# 二级界面
path = "images/bg2.png"
bg = pygame.image.load(path)
canvas.blit(bg, (0, 0))
showDetail()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #请在下方书写你的代码

    pygame.display.update()





