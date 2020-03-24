from tkinter import *
from tkinter.messagebox import showinfo
import tkinter.simpledialog as simpledialog
#函数
#函数：关闭窗口  参数：窗体 返回值，None
def close(window):
    window.destroy()
    return None
#函数：添加姓名窗口，参数，无，返回值
def add():
    #添加成绩窗口
    stuname = simpledialog.askstring('添加姓名','请输入学生姓名')
    if stuname in dict_stu.keys():
        showinfo(title = '错误',message='该学生已存在！')
    else:
        #添加成绩
        score = simpledialog.askstring('添加成绩','请输入学生成绩')
        #写入字典
        dict_stu[stuname] = score
        showinfo('提示','添加成功！')
    return None
