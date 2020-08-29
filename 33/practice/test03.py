import tkinter as tk
from tkinter import ttk
from PIL import ImageTk


def showImg(*args):
    #请在下方书写你的代码
    pass

global window
window = tk.Tk()
window.title('游戏选择')
window.geometry('800x450')
# 设置背景图片路径
bgPath = "./images/game1.jpg"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=800,height=450,image=bgImg)
bg.pack()
# 添加下拉列表框
cbox= ttk.Combobox(window,  width=15)
cbox['values'] = ['我的世界','第5人格','迷你世界']
cbox['state'] = 'readonly'
cbox.current(0)
cbox.place(x=0,y=0)
cbox.bind('<<ComboboxSelected>>',showImg)
cbox.place(x=0,y=0)
# 显示窗口
window.mainloop()
