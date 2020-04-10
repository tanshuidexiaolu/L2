import tkinter as tk
from PIL import ImageTk

window = tk.Tk()
window.resizable(0, 0)
window.title('举杯')
bg = ImageTk.PhotoImage(file="images/li.png")
content = '一杯敬朝阳\n一杯敬月光'
#1.下方写你的代码 字体为我“微软雅黑”字号为：20 字体颜色：white  compound='center'


window.mainloop()
