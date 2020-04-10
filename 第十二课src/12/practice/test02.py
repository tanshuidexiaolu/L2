#亲自出码1代码文件

import pygame
from sys import exit
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def shut():
	window.destroy()
	
	pygame.init()
	canvas = pygame.display.set_mode((648, 480), 0, 32)
	pygame.display.set_caption('desktop')
	#2.加载图片

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		#3.绘制界面

		
		pygame.display.update()

window = tk.Tk()
window.resizable(0, 0)
window.title('登录')

bg = ImageTk.PhotoImage(file="images/start.png")
bgLabel = tk.Label(window, width=1018, height=718, image=bg) #label组件用于显示文本或图像
bgLabel.pack()  


#1.添加关闭按钮


window.mainloop()






