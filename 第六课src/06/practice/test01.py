
import pygame
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def selectPhoto():
        messagebox.showwarning(title='登录窗口', message='你已登录成功')

# 二级界面
window = tk.Tk()
# 设置窗口不可变
window.resizable(0, 0)
window.title('登录页面')

bg = ImageTk.PhotoImage(file='images/ym.png')
bgLabel = tk.Label(window, width=1276, height=707, image=bg)
bgLabel.pack()   


btn = ImageTk.PhotoImage(file='images/denglu.png')
#以下写你的代码 创建登陆按钮，实现登陆效果



window.mainloop()

