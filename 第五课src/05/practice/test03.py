import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk

fileList = []
def selectPhoto():
    #下方写你的代码，最后使用file接收选择的图片
    pass

# 二级界面
window = tk.Tk()
# 设置窗口不可变
window.resizable(0, 0)
window.title('上传图片')

bg = ImageTk.PhotoImage(file="images/upload.png")
bgLabel = tk.Label(window, width=702, height=424, image=bg)
bgLabel.pack()   


btn = ImageTk.PhotoImage(file="images/btn.png")

uploadBtn = tk.Button(window, text='choose', command=selectPhoto,bd=0, image=btn, width=172, height=55)
uploadBtn.place(x=166, y=175)  


window.mainloop()

