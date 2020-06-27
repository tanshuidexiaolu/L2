# coding:utf-8
import pygame
from pygame.locals import *
from sys import exit
import requests
from subprocess import Popen, PIPE


# 绘制文本方法
def fillText(content, size, pos):
    fontColor = (255, 255, 255)
    fontObj = pygame.font.Font("font/simhei.ttf", size)  # 通过字体文件获得字体对象
    font = fontObj.render(content, True, fontColor)  # 配置要显示的文字
    canvas.blit(font, pos)  # 绘制字


def showDetail():
    global city, wendu, ganmao, type
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


# 请在下方书写你的代码℃
def getToday(cityName):
    url = "http://wthrcdn.etouch.cn/weather_mini?city=" + cityName
    response = requests.get(url)
    weathDict = response.json()
    # 声明全局变量城市，温度，感冒，天气类型
    global city, wendu, ganmao, type
    city = weathDict['data']['city']
    wendu = weathDict['data']['wendu']
    ganmao = weathDict['data']['ganmao']
    type = weathDict['data']['forecast'][0]['type']
getToday("西安")
bg = pygame.image.load("images/bg.png")
canvas.blit(bg,(0,0))
showDetail()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if 680 < event.pos[0] < 934 and 63 < event.pos[1] < 134:
                print("yeah")

    pygame.display.update()
