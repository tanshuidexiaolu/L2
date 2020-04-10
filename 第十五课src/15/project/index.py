import pygame
from sys import exit
import time
import requests
from subprocess import Popen,PIPE
import os

msg = '北京'
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

        # 获取月份
        month = time.strftime('%m')
        print(month)
        forecast = weatherDict['data']['forecast']
        # 获取日期
        global date, type, high, low
        date = month + '月' + forecast[0]['date']
        # 获取天气类型
        type = forecast[0]['type']
        # 获取最高温度
        high = forecast[0]['high']
        # 获取最低温度
        low = forecast[0]['low']

    else:
        print('你输入的城市是错误的')

def getData(cityName):
    getToday(cityName)
    # 获取未来天气信息
    global dates,types,highs,lows
    dates = []
    types = []
    highs = []
    lows = []
    for info in forecast:
        dates.append(month + '月' + info['date'])
        types.append(info['type'])
        highs.append(info['high'])
        print(highs)
        lows.append(info['low'])

getData(msg)
# pygame初始化
pygame.init()
canvas = pygame.display.set_mode((1050, 660))
pygame.display.set_caption('天气之子')

def fillInfo():
    for i in range(len(dates)):
        fillText(dates[i], 20, (20, 115 + 92 * i))
        fillText(types[i], 20, (200, 115 + 92 * i))
        fillText(highs[i], 20, (20, 140 + 92 * i))
        fillText(lows[i], 20, (180, 140 + 92 * i))

# 未来天气界面
def future():
    path = "images/bg3.png"
    bg = pygame.image.load(path)
    canvas.blit(bg, (0, 0))
    #调用绘制信息方法
    fillInfo()
    os.system('python city.py %s'%msg)
    tem_trend = pygame.image.load("images/test.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        canvas.blit(tem_trend, (280, 0))
        pygame.display.update()

# 城市天气界面
path = "images/bg2.png"
bg = pygame.image.load(path)
canvas.blit(bg, (0, 0))
# 调用方法
showDetail()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # 判断是否是鼠标左键被按下
            if event.button == 1:
                # 获取鼠标坐标位置
                pos = pygame.mouse.get_pos()
                if 524 <= pos[0] <= 709 and 448 <= pos[1] <= 509:
                    p = Popen('python enterbox.py',shell=True,stdout=PIPE)
                    print(p.stdout.readline())
                    with open('message.txt') as f:
                        msg = f.read()
                    if msg:
                        getData(msg)
                    canvas.blit(bg, (0, 0))
                    showDetail()
                if 565 <= pos[0] <= 797 and 310 <= pos[1] <= 384:
                    future()
    pygame.display.update()
