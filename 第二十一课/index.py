import pygame
from sys import exit
import time
import requests
from subprocess import Popen, PIPE
import matplotlib.pyplot as plt

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
        global city, wendu, month, forecast
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
    # 请在下方书写你的代码
    # 获取必须的数据
    # 1.日期2.天气类型3.高温4.低温
    global dates, types, highs, lows
    dates = []
    types = []
    highs = []
    lows = []
    # info --> information
    for info in forecast:
        types.append(info['type'])
        highs.append(info['high'])
        lows.append(info['low'])
        dates.append(month + '月' + info['date'])


getData('三亚')
# pygame初始化
pygame.init()
global canvas
canvas = pygame.display.set_mode((1050, 660))
pygame.display.set_caption('天气之子')


def fillInfo():
    for i in range(len(dates)):
        fillText(dates[i], 20, (20, 115+95*i))
        fillText(types[i], 20, (200, 115+95*i))
        fillText(highs[i], 20, (20, 140+95*i))
        fillText(lows[i], 20, (180, 140+95*i))

# 请在下方写你的代码
def future():
    # 1.加载背景图片
    bg = pygame.image.load('images/bg3.png')
    canvas.blit(bg, (0, 0))


path = "images/bg2.png"
bg = pygame.image.load(path)
canvas.blit(bg, (0, 0))
# 创建折线图方法
def plot():
    # 先声明空列表 用于存储数据(高温，低温)
    yhigh = []
    ylow = []
    for i in highs:
        a = int(i.split(" ")[1].split("℃")[0])
        yhigh.append(a)
    for j in lows:
        b = int(j.split(" ")[1].split("℃")[0])
        ylow.append(b)
    plt.style.use("classic")
    plt.figure(figsize=(10,8))
    # 设置"中文"字体
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # 设置正常的符号显示
    plt.rcParams['axes.unicode_minus'] = False
    # 绘制折线图
    plt.plot(dates,yhigh)
    plt.plot(dates,ylow)
    plt.show()
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
                    p = Popen('python enterbox.py', shell=True, stdout=PIPE)
                    print(p.stdout.readline())
                    with open('message.txt', encoding='utf-8') as f:
                        msg = f.read()
                    if msg:
                        getData(msg)
                    canvas.blit(bg, (0, 0))
                    showDetail()
                # 请在下方书写你的代码
                if 563 <= pos[0] <= 806 and 302 <= pos[1] <= 393:
                    future()
                    fillInfo()
                    plot()
                else:
                    canvas.blit(bg, (0, 0))
                    showDetail()
    pygame.display.update()
