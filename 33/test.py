import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

# 因为在comboxSelect事件侦测前，需要提前准备好函数
def show(*args):
    print(cbox.get())
    if cbox.get() == "路飞":
        # 切换图片路径
        bgImg = ImageTk.PhotoImage(file="./images/lufei.jpg")
    if cbox.get() == "路飞":
        # 切换图片路径
        bgImg = ImageTk.PhotoImage(file="./images/lufei.jpg")
    if cbox.get() == "路飞":
        # 切换图片路径
        bgImg = ImageTk.PhotoImage(file="./images/lufei.jpg")

        # 配置新的背景图片
    bg.config(image=bgImg)
    bg.image = bgImg
# 创建下拉菜单
window = tk.Tk()
# 绘制一个窗口
window.geometry('800x600')
# 设置窗口不可变
window.resizable(0, 0)
# 设置窗口标题
window.title("下拉菜单")
# 设置背景图
bgImg = ImageTk.PhotoImage(file='images/haizei.jpg')
# 设置图片便签
bg = tk.Label(window, width=800, height=600, image=bgImg)
# 打包
bg.pack()
# 添加下拉列表   combobox : 下拉列表
cbox = ttk.Combobox(window, width=20)
cbox['value'] = ['路飞', '罗', '索隆']
# 定义cbox下拉列表的位置
cbox.place(x=0, y=0)
# 设置下拉列表为制度模式
cbox['state'] = 'readonly'
# 设置默认选项 0表示为默认选项
cbox.current(2)
# 给下拉菜单绑定
cbox.bind("<<ComboboxSelected>>", show)
# 设置背景图片的切换
# *args表示需要用到N个参数，但是参数的数量不确定，可能用到参数


window.mainloop()
