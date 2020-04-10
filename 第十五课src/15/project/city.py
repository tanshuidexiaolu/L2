import sys
import time
import requests
import matplotlib.pyplot as plt
import platform

def getToday(cityName):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + cityName
    response = requests.get(url)
    weatherDict = response.json()
    print(weatherDict)
    if weatherDict['desc'] == 'OK':
        print('你输入的城市是正确的')
        # 获取城市名
        global city, wendu,month,forecast
        city = weatherDict['data']['city']
        print('城市名称', city)
        # 获取当前温度
        wendu = weatherDict['data']['wendu'] + '℃ '

        # 获取月份
        month = time.strftime('%m')
        print(month)
        forecast = weatherDict['data']['forecast']
        # 获取日期
        global date, type, high, low
        date = month + '月' + forecast[0]['date']
        # 获取天气类型
        type = forecast[0]['type']
        # 获取最高温度
        high = forecast[0]['high']
        # 获取最低温度
        low = forecast[0]['low']

    else:
        print('你输入的城市是错误的')

def getData(cityName):
    getToday(cityName)
    # 获取未来天气信息
    global dates,types,highs,lows
    dates = []
    types = []
    highs = []
    lows = []
    for info in forecast:
        dates.append(month + '月' + info['date'])
        types.append(info['type'])
        highs.append(info['high'])
        print(highs)
        lows.append(info['low'])
    plot()


#请在下方书写你的代码
# 完成未来几天天气情况曲线图,Python数据可视化
def plot():
    # 给出x,y值
    y_high = []
    y_low = []
    for high in highs:
        y_high.append(int(high.split(' ')[1].split('℃')[0]))
    for low in lows:
        y_low.append(int(low.split(' ')[1].split('℃')[0]))
    #y_high = [int(high.split(' ')[1].split('℃')[0]) for high in highs]
    #y_low = [int(low.split(' ')[1].split('℃')[0]) for low in lows]
    # 绘图
    plt.figure(figsize=(8, 6), dpi=100)
    plt.style.use('ggplot')  # 可以绘制出ggplot的风格
    if platform.system() == 'Windows':
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    else:
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.xticks(size=13, color='w')
    plt.yticks(size=13, color='w')
    plt.xlabel('日期(天)', size=15, color='w')
    plt.ylabel('温度(℃)', size=15, color='w')
    plt.title('未来天气走势图', color='w', fontsize=30)
    plt.plot(dates, y_high)
    plt.plot(dates, y_low)
    plt.legend(labels=['高温走势', '低温走势'], loc=0)
    plt.savefig("images/test.png", format='png', transparent=True)

if __name__ == "__main__":
    city = sys.argv[1]
    print('city ',city)
    getData(city)
