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
#主界面函数，参数，无，返回值
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
#登陆函数,参数，无，返回值None
def login():
    # 获取文本框内容
    admin = textbox_admin.get(1.0, END)[0:-1]
    pwd = textbox_pwd.get(1.0, END)[0:-1]
    #若输入的用户名没有存在于字典中,调用tipFalse函数（用户名或密码错误）
    if admin in dict_tech.keys():
        #若密码符合，调用主界面函数(main())
        if pwd == dict_tech[admin]['pwd']:
            showinfo(title = '登陆成功',message = '欢迎，教师'+dict_tech[admin]['name'])
            main()
        else:showinfo(title = '登录失败',message = '用户名或密码错误')
    else:
        showinfo(title = '登录失败',message = '用户名或密码错误')
    return None
