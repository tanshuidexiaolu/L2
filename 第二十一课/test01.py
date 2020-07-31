import matplotlib.pyplot as plt
import random

l1 = []
l2 = ['Mon', 'Tur', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
while True:
    for i in range(7):
        a = random.randint(0, 30)
        l1.append(a)
    plt.figure(figsize=(8, 6))
    # 加载风格
    plt.style.use('seaborn')
    print(plt.style.available)
    plt.xticks(size=15, color='yellow')
    plt.yticks(size=15, color='black')
    # 设置标题
    plt.title(label='Li Wen Qi‘s hair ', fontsize=20, color='black')
    plt.xlabel('date', size=15, color='black')
    plt.ylabel('Tem', size=15, color='black')
    plt.plot(l2, l1)
    plt.show()
