#码上回顾代码文件
import requests
import base64
# 调用百度人脸识别接口，获取token值
def getToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
               '&client_id=T1KUrVlob1vUuLpQ0sOYrfoB&client_secret=obx6I60FomQIHqRwlx3mp1GXTGKOkHPu'
    response = requests.get(host)
    content = response.json()
    content = content['access_token']
    return content
#1.网络请求地址
requestUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
#2.获取token
token = getToken()
params = {'access_token': token}
#3.加密图片
f = open("images/image.jpg", 'rb')
temp = f.read()
image = base64.b64encode(temp)

#请在下方编写你的代码

