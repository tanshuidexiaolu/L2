import pygame
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def canvasInit():
    # pygame初始化
    pygame.init()
    global canvas
    canvas = pygame.display.set_mode((1050, 660), 0, 32)
    pygame.display.set_caption('寻找嫌疑人')


window = tk.Tk()
window.resizable(0, 0)
window.title('寻找嫌疑人')

bg = ImageTk.PhotoImage(file="images/picShow.png")
bgLabel = tk.Label(window, width=1050, height=660, image=bg)  # label组件用于显示文本或图像
bgLabel.pack()
fileList = []


# 选择图片方法
def selectPhoto():
    file = filedialog.askopenfilename(initialdir="C:/", title='Choose an image.')  # 图片路径
    if len(file) > 0:
        fileList.append(file)
    # 下方写你的代码
    # 声明变量length用于储存fileList的列表长度
    length = len(fileList)
    if length == 1:
        showPhoto(fileList[0], 198, 160)


choose = ImageTk.PhotoImage(file="images/choose.png")
chooseBtn = tk.Button(window, text='choose', command=selectPhoto, bd=0, image=choose, width=88, height=84)
chooseBtn.place(x=917, y=51)

ok = ImageTk.PhotoImage(file="images/ok.png")
okBtn = tk.Button(window, text='OK', bd=0, image=ok, width=96, height=42)
okBtn.place(x=34, y=556)


# 图片缩放尺寸方法
def resize(w, h, new_w, new_h, pil_image):
    f1 = 1.0 * new_w / w
    f2 = 1.0 * new_h / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


# 展示图片方法
def showPhoto(route, xPos, yPos):
    # 获取图片
    image = Image.open(route)
    # 获取原图片尺寸
    w, h = image.size
    # 重置尺寸
    resized = resize(w, h, 150, 150, image)
    # 展示图片
    photo = ImageTk.PhotoImage(resized)
    photoLabel = tk.Label(window, image=photo, width=145, height=145)
    photoLabel.place(x=xPos, y=yPos)
    window.mainloop()


window.mainloop()
