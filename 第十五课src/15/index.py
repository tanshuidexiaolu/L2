# 请在下方完成你的代码
# 准备请求/返回模块
import requests

city = input("输入城市：")


# 创建函数(getToday)-->用于设置获取返回值，以及发送请求
def getToday(cityName):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+cityName
    data = {'city': cityName}
    reponse = requests.get(url, data)
    # 解析response返回的内容通过json字符串进行解析
    weatherDict = reponse.json()
    # 只有当城市名称为中国城市的时候，才显示ok，其他国家城市都显示无效
    if weatherDict['desc'] == "OK":
        print("城市输入正确")
    else:
        print("无效城市名称")

getToday(city)
