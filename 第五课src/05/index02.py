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


# 请在下方书写你的代码
# 创建按钮对应的函数
fileList = []


def selectPhoto():
    # 声明file-->储存选择的文件
    file = filedialog.askopenfilename(initialdir='C:/Users/Administrator/Desktop',
                                      title='寻人启事')
    if len(file) > 0:
        fileList.append(file)


window = tk.Tk()
window.resizable(0, 0)
window.title('寻找嫌疑人')

bg = ImageTk.PhotoImage(file="images/picShow.png")
bgLabel = tk.Label(window, width=1050, height=660, image=bg)  # label组件用于显示文本或图像
bgLabel.pack()
# 图片选择键
choose = ImageTk.PhotoImage(file="images/choose.png")
chooseBtn = tk.Button(window, command=selectPhoto, text='choose', bd=0, image=choose, width=88, height=84)
chooseBtn.place(x=917, y=51)

# 完成ok键
ok = ImageTk.PhotoImage(file="images/ok.png")
okBtn = tk.Button(window, text='OK', bd=0, image=ok, width=96, height=42)
okBtn.place(x=34, y=556)

window.mainloop()
