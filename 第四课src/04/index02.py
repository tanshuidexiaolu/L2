import tkinter as tk
from PIL import ImageTk
# 二级界面
window = tk.Tk()
# 设置窗口不可变
window.title('寻找嫌疑人')
# 请在下方书写你的代码
# 加载背景图
bg = ImageTk.PhotoImage(file='images/picShow.png')
# 渲染图片标签
bgLabel = tk.Label(window, width=1050, height=660, image=bg)
# 打包加载
bgLabel.pack()
# choose选择
choose = ImageTk.PhotoImage(file='images/choose.png')
chooseBtn = tk.Button(window, width=88, height=84, image=choose)
# 按钮定位
chooseBtn.place(x=915, y=51)
# chooseBtn.pack()
ok = ImageTk.PhotoImage(file='images/ok.png')
okBtn = tk.Button(window, width=96, height=42, image=ok,bd=0)
# okBtn.pack()
# 调用窗口主程序
window.mainloop()
