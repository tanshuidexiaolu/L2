import pygame
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


# 二级界面
window = tk.Tk()
# 设置窗口不可变
window.resizable(0, 0)
window.title('音乐播放器')

bg = ImageTk.PhotoImage(file="images/music.png")
bgLabel = tk.Label(window, width=394, height=700, image=bg)
bgLabel.pack()   


btn = ImageTk.PhotoImage(file="images/play.png")
#下方写你的代码，为音乐播放器添加播放按钮



window.mainloop()

