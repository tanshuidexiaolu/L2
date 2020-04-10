import easygui

t = easygui.enterbox('请输入要查询的中国城市',title='city')
with open('message.txt','w') as f:
    f.write(t)
