import pygame
import time
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
    # 声明变量canvas，并设置为全局变量
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

fileList = []   # 图片路径列表 C:/嫌疑人照片/谈俊粼.png
totalList = []  # 存储所有所需的数据
#选择图片函数
def selectPhoto():
    # 当点击选择按钮以后，打开对应的路径文件 dialog路径
    file = filedialog.askopenfilename(initialdir="C:/嫌疑人照片", title='Choose an image.')  # 图片路径
    #length 长度
    if len(file) > 0:   #判断是否选择图片“0”为取消
        fileList.append(file) # 将选中图片添加到列表中
    length = len(fileList)
    # 当图片选择超过6张时
    if length > 6:
        #使用消息对话框警告提示
         msg = messagebox.showwarning(title='请注意', message='最多选择6张照片')
    if length == 1:
        #调用显示嫌疑人函数
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

#显示嫌疑犯图片
#route 原图片
#xPos,yPos 显示的位置坐标
def showPhoto(route,xPos,yPos):
    #获取图片
    image = Image.open(route)
    #获取原图片尺寸w：width  h:height
    w, h = image.size
    #重置尺寸 recover
    resized = resize(w, h, 150, 150, image)
    #展示图片
    photo = ImageTk.PhotoImage(resized)
    photoLabel = tk.Label(window, image=photo, width=145, height=145)
    photoLabel.place(x=xPos, y=yPos)
    # 调用窗口主程序
    window.mainloop()

# 调用百度人脸识别接口，获取token值
def getToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
               '&client_id=T1KUrVlob1vUuLpQ0sOYrfoB&client_secret=obx6I60FomQIHqRwlx3mp1GXTGKOkHPu'
               #request请求   get获取
    response = requests.get(host)
    content = response.json()
    content = content['access_token']
    return content

#获取人脸识别数据
def getData():
    #请补全请求地址 request请求
    requestUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
    #请在下方完成你的代码
    # 设置token数据 --> 从百度api中获取数据
    token = getToken()
    # 设置token参数
    params = {"access_token":token}
    # 遍历图片列表
    for iUrl in fileList:
        # 获取图片存入变量f中
        f = open(iUrl,"rb")
        # 读取图片
        temp = f.read()
        # 将temp加密传输
        image = base64.b64encode(temp)
        # 设置数据 data数据  date日期
        data = {
                # 传输图片内容  "键名":键值
                "image":image,
                # 图片的加密方式
                "image_type":"BASE64",
                # 识别内容:年龄，性别，脸型
                "face_field":"age,gender,face_shape"
                }
        # post加密发送-->1.没有大小限制  2.传输加密
        response = requests.post(requestUrl,params = params,data = data)
        print(response)
        # 将response返回结果进行json解析
        content = response.json()
        print(content)
        # 获取年龄
        age = content['result']['face_list'][0]['age']
        print("年龄为:",age)
        # 性别
        gender = content['result']['face_list'][0]['gender']['type']
        pro = content['result']['face_list'][0]['gender']['probability']
        print("性别为:",gender)
        print("性别判断正确的概率为:",str(pro*100)+"%")
        # 脸型
        shape = content['result']['face_list'][0]['face_shape']['type']
        print("脸型为:",shape)
        # 性别判断
        if gender == "male":
            gender = "男性"
        else:
            gender = "女性"
        # 脸型判断
        if shape == "square":
            shape = "国字脸"
        elif shape == "triangle":
            shape = "瓜子脸"
        elif shape == "oval":
            shape = "鹅蛋脸"
        elif shape == "heart":
            shape = "心形脸"
        else :
            shape = "圆脸"
        print("转换后的脸型为:",shape)
        print("转换以后的性别为:",gender)
        # 存储全部所需数据
        tempDict = {
                    # 图片路径
                    'image':iUrl,
                    # 年龄  性别  脸型
                    'age':age,
                    'gender':gender,
                    'shape':shape
                    }
        # 将tempDict字典，存储到列表totalList中
        totalList.append(tempDict)
        print("totalList = ",totalList)
    # 关闭二级界面
    window.destroy()
    showResult()
# 创建结果展示的方法
def showResult():
    # 创建pygame界面
    canvasInit()
    # 设置背景图
    background = pygame.image.load("images/suspectInfo.png")
    # 传输图片
    canvas.blit(background,(0,0))
    # 设置窗口的关闭功能
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        #绘制传输结果(1.图片路径  2.图片年龄  3.图片性别  4.图片脸型)
        drawResult(0,(160,112),(375,155),(375,190),(397,225))
        # 设置屏幕更新
        pygame.display.update()
# 创建绘制传输结果的方法:两个参数：1.图片下标(index)  2.图片位置(position)
#                             年龄，性别，脸型
def drawResult(index,imagePos,agePos,genderPos,shapePos):
    # 从文件列表中抽取图片的路径
    image = totalList[index]['image']
    # 加载图片 --> photo
    photo = pygame.image.load(image)
    # 缩放图片 --> 115*115
    file = pygame.transform.scale(photo,(115,115))
    # 画图片
    canvas.blit(file,imagePos)
    # 获取年龄
    age = str(totalList[index]['age'])
    # 传输年龄文本
    fillText(age,agePos)
    # 获取性别
    gender = totalList[index]['gender']
    # 传输性别文本
    fillText(gender,genderPos)
    # 获取脸型
    shape = totalList[index]['shape']
    fillText(shape,shapePos)
# 绘制文本函数
def fillText(text, center):
    # 设置字体样式和大小
    my_font = pygame.font.Font("font/simhei.ttf", 22)
    # 渲染文字
    text = my_font.render(text, True, (109, 49, 9))
    textRectObj = text.get_rect()  # 获得要显示的对象的rect
    textRectObj.center = center  # 设置显示对象的坐标
    # 画图片的方法
    canvas.blit(text, textRectObj)
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
chooseBtn = tk.Button(window, text='choose', command=selectPhoto,bd=0, image=choose, width=88, height=84)
chooseBtn.place(x=917, y=51)  # 按钮位置及对齐方式

# 完成选择键
ok = ImageTk.PhotoImage(file="images/ok.png")
okBtn = tk.Button(window, text='OK', command=getData,bd=0, image=ok, width=96, height=42)
okBtn.place(x=34, y=556)
window.mainloop()