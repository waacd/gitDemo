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
#查看成绩函数：参数，返回无
def view():
    showinfo("学生成绩",dict_stu)
    return None
def main():
    #关闭主窗口
    close(top)
    #创建主界面窗口以及三个按钮
    main = Tk()
    main.title("学生成绩管理系统")
    button_add = Button(main,text = "添加成绩",command = add).pack()#添加成绩函数
    button_view = Button(main,text = "查看成绩",command = view).pack()#查看成绩函数
    button_exit = Button(main,text = "退出系统",command = lambda :close(main)).pack()
    main.mainloop()
    return None
