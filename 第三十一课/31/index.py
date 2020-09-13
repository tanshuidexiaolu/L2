import tkinter as tk
import pygame
from PIL import ImageTk


def inputName():
    global window
    # 1.关闭当前窗口
    window.destroy()
    # 2.创建新的窗口
    window = tk.Tk()
    # 设置窗口大小
    window.geometry("1050x660")
    # 设置窗口标题
    window.title("写字达人2号界面")
    # 设置背景图片
    bgImg = ImageTk.PhotoImage(file='./images/bg3.jpg')
    # 加载图片
    bg = tk.Label(window, width=1050, height=660, image=bgImg)
    # 布局
    bg.pack()
    # 设置字体路径
    fontPath = "./font/simhei.ttf"
    # 设置字体颜色
    color = '#ffd46c'
    # 设置问题样式
    name = tk.Label(window, text='姓名', bg=color, font=(fontPath, 20))
    style = tk.Label(window, text='样式', bg=color, font=(fontPath, 20))
    name.place(x=370,y=165)
    style.place(x=370,y=235)
    window.mainloop()


def nameSign():
    # 请在下方书写你的代码
    # 创建全局变量
    global window
    # 创建窗口
    window = tk.Tk()
    # 创建窗口大小
    window.geometry("1050x660")
    # 不能改变窗口大小
    window.resizable(0, 0)
    # 设置标题
    window.title("写字达人")
    # 设置图片路径 相对路径的开头 ./
    bg = './images/bg1.jpg'
    # 加载背景图1.加载图片
    bgImg = ImageTk.PhotoImage(file=bg)
    # 加载背景图2.将图片渲染到程序当中
    bg = tk.Label(window, width=1050, height=660, image=bgImg)
    # 开始按钮の图片
    startPath = "./images/start.png"
    # 加载开始按钮
    startImg = ImageTk.PhotoImage(file=startPath)
    start = tk.Button(window, image=startImg, width=179, height=70, bd=0, command=inputName)
    start.place(x=438, y=466)
    # 布局
    bg.pack()
    # 窗口挂载
    window.mainloop()


# 程序开始
nameSign()
