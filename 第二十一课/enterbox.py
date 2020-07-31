# coding:utf-8
import easygui

city = easygui.enterbox("请输入城市：")
with open('message.txt', 'w', encoding='utf-8') as f:
    f.write(city)

