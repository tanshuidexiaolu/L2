import tkinter as tk
from tkinter import ttk
from PIL import ImageTk


def nameSign():
    # 创建窗口
    global window
    window = tk.Tk()
    window.geometry('1050x660')
    window.resizable(0, 0)
    # 设置标题
    window.title('艺术签名')
    # 设置背景图片的路径
    bgPath = "./images/bg1.jpg"
    # 加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    # 设置窗口背景
    bg = tk.Label(window, width=1050, height=660, image=bgImg)
    bg.pack()
    # 设置开始按钮的图片路径
    startPath = "./images/start.png"
    # 加载开始按钮
    startImg = ImageTk.PhotoImage(file=startPath)
    # 添加开始按钮
    start = tk.Button(window, image=startImg, bd=0, width=179, height=70,
                      command=inputName)
    start.place(x=438, y=466)
    window.mainloop()


# 按钮事件函数inputName
def inputName():
    global window
    window.destroy()
    # 创建窗口
    window = tk.Tk()
    window.geometry('1050x660')
    window.resizable(0, 0)
    # 窗口标题
    window.title('艺术签名')
    bgImg = ImageTk.PhotoImage(file="./images/bg3.jpg")
    bg = tk.Label(window, width=1050, height=660, image=bgImg)
    bg.pack()
    # 字体路径
    fontPath = "./font/simhei.ttf"
    # 颜色字符
    color = '#ffd46c'
    name = tk.Label(window, text='姓名', bg=color, font=(fontPath, 18))
    style = tk.Label(window, text='样式', bg=color, font=(fontPath, 18))
    name.place(x=370, y=165)
    style.place(x=370, y=235)
    # 姓名输入框
    # 1.创建输入框，使用tkinter库中的entry方法进行创建
    # 2.输入框中的自己样式
    entry = tk.Entry(window, font=("./font/simhei.ttf", 15))
    entry.place(x=430, y=170)
    # 设置下拉列表(1.下拉框在哪，宽度)
    cbox = ttk.Combobox(window, width=30)
    # 设置下拉框的值
    cbox['values'] = ["请选择签名样式", "个性签", "连笔签", "潇洒签", "可爱签"]
    cbox.place(x=430, y=240)
    # 设置下拉框为不能输入的样式
    cbox['state'] = "readonly"
    cbox.current(0)
    # 给下拉菜单绑定showMsg事件
    # cbox.bind("<<ComboboxSelected>>", showMsg)
    okImg = ImageTk.PhotoImage(file="./images/ok.png")
    ok = tk.Button(window, image=okImg, bd=0, width=179,height=70)
    ok.place(x=436, y=465)
    window.mainloop()


# 程序开始
nameSign()
