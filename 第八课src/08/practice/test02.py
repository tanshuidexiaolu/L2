#亲自出码1代码文件

import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import base64
import requests

# 图片缩放尺寸方法
def resize( w, h, new_w, new_h, pil_image):
    f1 = 1.0 * new_w / w
    f2 = 1.0 * new_h / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)

#选择图片函数
def selectPhoto():
    global file
    file = filedialog.askopenfilename(initialdir="C:/", title='Choose an image.')  # 图片路径
    if len(file) == 0:   #判断是否选择图片“0”为取消
        messagebox.showwarning(title='请注意', message='请上传图片')
    else:
        showPhoto(file,59,50)

#显示嫌疑犯图片
#route 原图片
#xPos,yPos 显示的位置坐标
def showPhoto(route,xPos,yPos):
    #获取图片
    image = Image.open(route)
    #获取原图片尺寸
    w, h = image.size
    #重置尺寸
    resized = resize(w, h, 150, 150, image)
    #展示图片
    photo = ImageTk.PhotoImage(resized)
    photoLabel = tk.Label(window, image=photo, width=145, height=145)
    photoLabel.place(x=xPos, y=yPos)
    window.mainloop()

# 调用百度人脸识别接口，获取token值
def getToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
               '&client_id=T1KUrVlob1vUuLpQ0sOYrfoB&client_secret=obx6I60FomQIHqRwlx3mp1GXTGKOkHPu'
    response = requests.get(host)
    content = response.json()
    content = content['access_token']
    return content

#获取人脸识别数据
def getData():
    #1.网络请求地址
    requestUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
    #2.获取token
    token = getToken()
    params = {'access_token': token}
    #3.加密图片
    f = open(file, 'rb')
    temp = f.read()
    image = base64.b64encode(temp)
    # 请求的数据
    #请在下方完成你的代码


window = tk.Tk()
# 设置窗口不可变
window.resizable(0, 0)
window.geometry('500x300')
window.title('添加图片文件')
# 图片选择键
choose = ImageTk.PhotoImage(file="images/btn.png")
chooseBtn = tk.Button(window, text='choose', command=selectPhoto,bd=0, image=choose, width=150, height=35)
chooseBtn.place(x=300, y=51)  # 按钮位置及对齐方式

# 完成选择键
ok = ImageTk.PhotoImage(file="images/ok.png")
okBtn = tk.Button(window, text='OK', command=getData,bd=0, image=ok, width=80, height=40)
okBtn.place(x=34, y=250)
window.mainloop()
