import pygame
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def selectPhoto():
    print('你点击了按钮')

# 二级界面
window = tk.Tk()
# 设置窗口不可变
window.resizable(0, 0)
window.title('上传图片')

bg = ImageTk.PhotoImage(file="images/upload.png")
bgLabel = tk.Label(window, width=702, height=424, image=bg)
bgLabel.pack()   


btn = ImageTk.PhotoImage(file="images/btn.png")
# 下方写你的代码，添加btn并为其添加点击响应，命令属性的方法为selectPhoto



window.mainloop()

