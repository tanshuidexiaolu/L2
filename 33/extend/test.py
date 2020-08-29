import tkinter as tk
from tkinter import ttk
#请在下方书写你的代码


window = tk.Tk()
window.title('下拉列表')
window.geometry('400x300')
window.resizable(0,0)

# 添加下拉列表框
cbox = ttk.Combobox(window,  width=15)
cbox['values'] = ['1','2','3','4']
cbox['state'] = 'readonly'
cbox.current(0)

# 下拉列表框绑定选择事件函数
cbox.bind('<<ComboboxSelected>>',showMsg)
cbox.place(x=0,y=0)

# 显示窗口
window.mainloop()


