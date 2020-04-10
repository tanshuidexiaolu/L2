# tkinter应用窗口
# 导入tkinter类
import tkinter as tk

from PIL import ImageTk

letter = "爱问:“‘知止而后有定’朱子以为‘事事物物皆有定理’”"

# 创建主窗口
window = tk.Tk()
# 调整窗口大小resizable
window.resizable(0, 0)
# 设置窗口标题
window.title(letter)
# 加载图片
bg = ImageTk.PhotoImage(file="images/bg.png")
# 将图片挂载到窗口当中
bgLabel = tk.Label(window, image=bg,
                   text=letter,
                   font=('田英章行书', 29),
                   foreground='white',
                   compound='center'
                   )
# 打包上传
bgLabel.pack()
# 调用窗口主程序
window.mainloop()
