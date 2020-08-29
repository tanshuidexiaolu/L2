import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

global window
window = tk.Tk()
window.title('王者荣耀')
window.geometry('800x500')
bgPath = "./images/kingBg.png"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=800,height=500,image=bgImg)
bg.pack()
btnPath = "./images/kingBtn.png"
btnImg = ImageTk.PhotoImage(file=btnPath)
btn = tk.Button(window,image=btnImg,bd=0,width=250,height=50)
btn.place(x=290, y=350)

#请在下方书写你的代码
# 添加下拉列表框

# 显示窗口
window.mainloop()

