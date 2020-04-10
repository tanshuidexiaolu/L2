import pygame
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import base64
import requests

def canvasInit():
    #pygame初始化
    pygame.init()
    global canvas
    canvas = pygame.display.set_mode((1050, 660), 0, 32)
    pygame.display.set_caption('寻找嫌疑人')

# 图片缩放尺寸方法
def resize( w, h, new_w, new_h, pil_image):
    f1 = 1.0 * new_w / w
    f2 = 1.0 * new_h / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)

fileList = []   # 图片路径列表


#选择图片函数
def selectPhoto():
    file = filedialog.askopenfilename(initialdir="C:/", title='Choose an image.')  # 图片路径
    if len(file) > 0:   #判断是否选择图片“0”为取消
        fileList.append(file) # 将选中图片添加到列表中
    length = len(fileList)
    if length > 6:
         msg = messagebox.showwarning(title='请注意', message='最多选择6张照片')
    if length == 1:
        showPhoto(fileList[0],198,160)
    elif length == 2:
        showPhoto(fileList[1],448,160)
    elif length == 3:
        showPhoto(fileList[2],694,160)
    elif length == 4:
        showPhoto(fileList[3],198,390)
    elif length == 5:
        showPhoto(fileList[4],448,390)
    elif length == 6:
        showPhoto(fileList[5],694,390)


def showPhoto(route,xPos,yPos):
    image = Image.open(route)
    w, h = image.size
    resized = resize(w, h, 150, 150, image)
    photo = ImageTk.PhotoImage(resized)
    photoLabel = tk.Label(window, image=photo, width=145, height=145)
    photoLabel.place(x=xPos, y=yPos)
    window.mainloop()

def getToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
               '&client_id=T1KUrVlob1vUuLpQ0sOYrfoB&client_secret=obx6I60FomQIHqRwlx3mp1GXTGKOkHPu'
    response = requests.get(host)
    content = response.json()
    content = content['access_token']
    return content


def getData():
    requestUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
    token = getToken()
    params = {'access_token': token}
    for imgUrl in fileList:
        f = open(imgUrl, 'rb')
        temp = f.read()
        image = base64.b64encode(temp)
        data = {
            'image':image,
            'image_type':'BASE64',
            'face_field':'age,gender,face_shape'
        }
        response = requests.post(requestUrl, params=params, data=data)
        print('响应结果：', response)
        content = response.json()
        print('解析结果：', content)
        age = content['result']['face_list'][0]['age']  # 人脸得分
        gender = content['result']['face_list'][0]['gender']['type']
        shape = content['result']['face_list'][0]['face_shape']['type']
        if gender == 'male':
            gender='男'
        else:
            gender='女'
        if shape == 'square':
            shape = '国字脸'
        elif shape == 'triangle':
            shape = '瓜子脸'
        elif shape == 'oval':
            shape = '鹅蛋脸'
        elif shape == 'heart':
            shape = '心形脸'
        else:
            shape = '圆形脸'
        #请在下方完成你的代码



# 二级界面
window = tk.Tk()
# 设置窗口不可变
window.resizable(0, 0)
window.title('寻找嫌疑人')

bg = ImageTk.PhotoImage(file="images/picShow.png")
bgLabel = tk.Label(window, width=1050, height=660, image=bg) #label组件用于显示文本或图像
bgLabel.pack()   #将组件放置在窗口中

# 图片选择键
choose = ImageTk.PhotoImage(file="images/choose.png")
chooseBtn = tk.Button(window, command=selectPhoto,bd=0, image=choose, width=88, height=84)
chooseBtn.place(x=917, y=51)  # 按钮位置及对齐方式

# 完成选择键
ok = ImageTk.PhotoImage(file="images/ok.png")
okBtn = tk.Button(window, command=getData,bd=0, image=ok, width=96, height=42)
okBtn.place(x=34, y=556)
window.mainloop()


