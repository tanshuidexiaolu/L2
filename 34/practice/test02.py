import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

global window
window = tk.Tk()
window.title('登录')
window.geometry('556x557')
bgPath = "./images/login.jpg"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=556,height=557,image=bgImg)
bg.pack()

#请在下方书写你的代码


# 显示窗口
window.mainloop()



