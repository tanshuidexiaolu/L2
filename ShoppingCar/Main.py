"""
购物车小项目
系统：Windows 10
语言：Python 3
IDE：PyCharm 2020.2
"""
import json

# 初始变量
uName = ''
uPwd = ''


# 购物车注册，登录
# 1.设置密码和用户名，密码为空
def login():
    uName = ""
    uPwd = ""
    if uName == "":
        print("请登录：")
        uname = input("请输入用户名：")
        upwd = input("请输入密码：")
        with open("message.json", 'r', encoding='utf-8') as f:
            a = f.read()
            fi = json.loads(a)
            username = fi["user"]["name"]
            userpassword = fi["user"]["passwod"]
            a = a.split(" ")[0]
            # 当服务器中存在用户数据
            if uname == a:
                print("用户已存在")
            else:
                # 将输入的用户名和密码统一注册
                with open("message.json", 'w', encoding="utf-8") as file:
                    fi["user"]["name"] = uname
                    fi["user"]["passwod"] = upwd
                    json.dump(fi, file)
                    shop()


def shop():
    pass


login()
