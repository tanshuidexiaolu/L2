import pygame
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import base64
import requests


def canvasInit():
    # pygame初始化
    pygame.init()
    global canvas
    canvas = pygame.display.set_mode((1050, 660), 0, 32)
    pygame.display.set_caption('寻找嫌疑人')


# 图片缩放尺寸方法
def resize(w, h, new_w, new_h, pil_image):
    f1 = 1.0 * new_w / w
    f2 = 1.0 * new_h / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


fileList = []  # 图片路径列表
totalList = []  # 储存所有所需数据


# 选择图片函数
def selectPhoto():
    file = filedialog.askopenfilename(initialdir="C:/", title='Choose an image.')  # 图片路径
    if len(file) > 0:  # 判断是否选择图片“0”为取消
        fileList.append(file)  # 将选中图片添加到列表中
    length = len(fileList)
    # 当图片选择超过6张时
    if length > 6:
        # 使用消息对话框警告提示
        msg = messagebox.showwarning(title='请注意', message='最多选择6张照片')
    if length == 1:
        # 调用显示嫌疑人函数
        showPhoto(fileList[0], 198, 160)
    elif length == 2:
        showPhoto(fileList[1], 448, 160)
    elif length == 3:
        showPhoto(fileList[2], 694, 160)
    elif length == 4:
        showPhoto(fileList[3], 198, 390)
    elif length == 5:
        showPhoto(fileList[4], 448, 390)
    elif length == 6:
        showPhoto(fileList[5], 694, 390)


# 显示嫌疑犯图片
# route 原图片
# xPos,yPos 显示的位置坐标
def showPhoto(route, xPos, yPos):
    # 获取图片
    image = Image.open(route)
    # 获取原图片尺寸
    w, h = image.size
    # 重置尺寸
    resized = resize(w, h, 150, 150, image)
    # 展示图片
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


# 获取人脸识别数据
def getData():
    # 请补全请求地址
    requestUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
    # 请在下方完成你的代码
    # 设置token参数-->从百度api中获得数据
    token = getToken()
    # 设置参数
    params = {"access_token": token}
    for iUrl in fileList:
        # 获取图片存入变量f中
        f = open(iUrl, "rb")
        # 读取图片
        temp = f.read()
        # 将temp加密传输
        image = base64.b64encode(temp)
        # 设置数据
        data = {
            # 传输的数据内容"键名":键值
            # 传输内容
            'image': image,
            # 图片的加密方式
            'image_type': "BASE64",
            # 识别内容
            'face_field': "age,gender,face_shape"
        }
        # post加密发送-->1.没有大小限制 2.传输加密
        response = requests.post(requestUrl, params=params, data=data)
        print(response)
        # 将response返回结果进行json解析
        content = response.json()
        print(content)
        # 获取年龄
        age = content['result']['face_list'][0]['age']
        print("年龄为：", age)
        # 性别
        gender = content['result']['face_list'][0]['gender']['type']
        pro = content['result']['face_list'][0]['gender']['probability']
        # 如果性别判断为男性
        if gender == 'male':
            print("性别为：", "男性")
        # 如果性别判断为女性
        if gender == 'female':
            print("性别为：", "女性")
        print("判断的正确率：" + str(pro * 100) + "%")
        # 脸型
        shape = content['result']['face_list'][0]['face_shape']['type']
        # 脸型判断
        if shape == 'square':
            shape = '国字脸'
        elif shape == 'triangle':
            shape = '瓜子脸'
        elif shape == 'oval':
            shape = '鹅蛋脸'
        elif shape == 'heart':
            shape = '心形脸'
        else:
            shape = '圆脸'
        print("脸型为：", shape)
        # 储存全部所需数据
        tempDict = {
            # 图片路径
            'image': iUrl,
            # 年龄，性别，脸型
            'age': age,
            'gender': gender,
            'shape': shape

        }
        # 将tempDict字典储存到totalList中
        totalList.append(tempDict)
        print("totalList= ", totalList)
        # 关闭二级界面
        window.destroy()
        showResult()


# 创建结果显示的方法
def showResult():
    # 创建pygame界面
    canvasInit()
    # 设置背景图
    backgroud = pygame.image.load("images/suspectInfo.png")
    # 传输图片
    canvas.blit(backgroud, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.display.update()
    
# 创建绘制传输结果的方法:两个参数：图片下标，图片位置
def drawResult(index,imagePos):
    # 绘制图片的路径
    image = totalList[index]['image']

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
bgLabel = tk.Label(window, width=1050, height=660, image=bg)  # label组件用于显示文本或图像
bgLabel.pack()  # 将组件放置在窗口中

# 图片选择键
choose = ImageTk.PhotoImage(file="images/choose.png")
chooseBtn = tk.Button(window, text='choose', command=selectPhoto, bd=0, image=choose, width=88, height=84)
chooseBtn.place(x=917, y=51)  # 按钮位置及对齐方式

# 完成选择键
ok = ImageTk.PhotoImage(file="images/ok.png")
okBtn = tk.Button(window, text='OK', command=getData, bd=0, image=ok, width=96, height=42)
okBtn.place(x=34, y=556)
window.mainloop()
