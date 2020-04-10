import pygame
from sys import exit
import requests
from subprocess import Popen,PIPE

# 绘制文本方法
def fillText(content, size, pos):
    fontColor = (255, 255, 255)
    fontObj = pygame.font.Font("font/simhei.ttf", size)  # 通过字体文件获得字体对象
    font = fontObj.render(content, True, fontColor)  # 配置要显示的文字
    canvas.blit(font, pos)  # 绘制字

def showDetail():
    global city, wendu,ganmao,type
    fillText(city, 45, (350, 185))
    fillText(wendu, 30, (300, 285))
    fillText(type, 35, (440, 280))
    fillText(ganmao[0:20], 18, (200, 460))
    fillText(ganmao[20:], 18, (200, 490))

# pygame初始化
pygame.init()
global canvas
canvas = pygame.display.set_mode((1050, 660))
pygame.display.set_caption('天气助手')

def getToday(cityName):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + cityName
    response = requests.get(url)
    weatherDict = response.json()
    print(weatherDict)
    # 获取城市名
    global city, wendu,ganmao,type
    city = weatherDict['data']['city']
    print('城市名称', city)
    # 获取当前温度
    wendu = weatherDict['data']['wendu'] + '℃ '
    ganmao = weatherDict['data']['ganmao']
    type = weatherDict['data']['forecast'][0]['type']
getToday('北京')

# 绘制背景
path = "images/bg.png"
bg = pygame.image.load(path)
canvas.blit(bg, (0, 0))
# 写文字
showDetail()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #请在下方书写你的代码
        
    pygame.display.update()
