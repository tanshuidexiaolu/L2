# 亲自出码代码文件
import tkinter as tk

from PIL import ImageTk

# tkinter实现界面
# 窗口标题:'王者荣耀' 窗口宽800  高500
window = tk.Tk()
window.title('王者荣耀')
window.geometry('800x500')

# 设置背景图片 图片路径'./images/kingBg.png'  宽800  高500
bgPath = "./images/kingBg.png"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=800,height=500,image=bgImg)
bg.pack()

# 请在下方书写你的代码


# 显示窗口
window.mainloop()

