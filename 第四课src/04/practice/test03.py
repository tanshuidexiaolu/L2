import tkinter as tk
from tkinter import *
from PIL import ImageTk 
window = tk.Tk()
window.resizable(0, 0)
window.title('手机')
#1.下方写你的代码，使用Label绘制手机页面
bg = ImageTk.PhotoImage(file="images/iphone.png")


#2.下方写你的代码，为手机添加可以点击的home按键
btnImage = ImageTk.PhotoImage(file="images/btn.png")


window.mainloop()


