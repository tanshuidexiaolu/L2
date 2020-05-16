import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import base64
import requests


def resize(w, h, new_w, new_h, pil_image):
    f1 = 1.0 * new_w / w
    f2 = 1.0 * new_h / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


def showPhoto(route, xPos, yPos):
    image = Image.open(route)
    w, h = image.size
    if w == 310 and h == 310:
        resized = image
    else:
        resized = resize(w, h, 310, 310, image)
    photo = ImageTk.PhotoImage(resized)
    photoLabel = tk.Label(window, image=photo, width=310, height=310)
    photoLabel.place(x=xPos, y=yPos)
    window.mainloop()


def selectPhoto():
    global file
    file = filedialog.askopenfilename(initialdir="C:/", title='Choose an image.')  # 图片路径
    if len(file) == 0:
        messagebox.showwarning(title='请注意', message='请选择一张清晰人脸图片')
    else:
        showPhoto(file, 155, 193)


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

    f = open(file, 'rb')
    temp = f.read()
    image = base64.b64encode(temp)

    data = {
        'image': image,
        'image_type': 'BASE64',
        'face_field': 'gender,beauty'
    }
    # 1.发送请求
    response = requests.post(
        # 1.服务器上传的地址2.上传参数3.上传数据data
        requestUrl,
        params=params,
        data=data
    )
    # 2.解析数据

    gender = content['result']['face_list'][0]['gender']['type']
    print('性别', gender)
    beauty = content['result']['face_list'][0]['beauty']
    print('颜值', beauty)

    # 3.匹配女性英雄

    # 4.匹配男性英雄


window = tk.Tk()

window.resizable(0, 0)
window.title('漫威之英雄集结')

bg = ImageTk.PhotoImage(file="images/bg.jpg")
bgLabel = tk.Label(window, width=1050, height=660, image=bg)
bgLabel.pack()

choose = ImageTk.PhotoImage(file="images/choose.png")
chooseBtn = tk.Button(window, command=selectPhoto, bd=0, image=choose, width=71, height=71)
chooseBtn.place(x=933, y=65)

ok = ImageTk.PhotoImage(file="images/ok.png")
okBtn = tk.Button(window, command=getData, bd=0, image=ok, width=217, height=78)
okBtn.place(x=417, y=540)
window.mainloop()
