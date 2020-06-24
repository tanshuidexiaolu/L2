import pygame
from sys import exit
import time
import requests
from subprocess import Popen, PIPE


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


getToday('西安')

# pygame初始化
pygame.init()
global canvas
canvas = pygame.display.set_mode((1050, 660))
pygame.display.set_caption('天气之子')

# 二级界面
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
                    p = Popen('enterbox.exe', shell=True, stdout=PIPE)
                    print(p.stdout.readline())
                    # 请在下方书写你的代码
                    # open --> open('文件名'，'w')写入
                    #          open('文件名')读取
                    #          open('文件名',a)写入，但是往末尾a = append
                    with open('message.txt',encoding='utf-8') as f:
                        msg = f.read()
                        print(msg)
    pygame.display.update()
