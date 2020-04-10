import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import base64
import requests

def resize( w, h, new_w, new_h, pil_image):
    f1 = 1.0 * new_w / w
    f2 = 1.0 * new_h / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)

def showPhoto(route,xPos,yPos):
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

#2.下方写你的代码，创建图片选择方法

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
        'image':image,
        'image_type':'BASE64',
        'face_field':'gender,beauty'
    }
    
    gender = content['result']['face_list'][0]['gender']['type']
    print('性别',gender)
    beauty = content['result']['face_list'][0]['beauty']
    print('颜值',beauty)

  

#1.下方写你的代码，搭建程序界面


#3.下方写你的代码，添加按钮










