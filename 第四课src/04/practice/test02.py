import tkinter as tk
from tkinter import *
from PIL import ImageTk

window = tk.Tk()
window.resizable(0, 0)
window.title('house')

#1.下方写你的代码，使用Label显示house画面，最后显示不要忘记pack()
bg = ImageTk.PhotoImage(file="images/house.png")


#2.下方写你的代码，使用button组件实现可按动的房门 
door = ImageTk.PhotoImage(file="images/door.png")


window.mainloop()


