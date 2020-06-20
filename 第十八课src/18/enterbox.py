import easygui
city = easygui.enterbox('请输入要查询的中国城市',title='city')
#请在下方书写你的代码
with open('message.txt','w',encoding='utf-8') as f:
    f.write(city)
