import re
import tkinter.messagebox
import tkinter
from turtle import onclick
from math import *
# 定义界面
jsq= tkinter.Tk()
jsq.geometry('450x500+500+200')
jsq.resizable(False, False)
jsq.title("计算器")

# 定义输出文本框
contentVar = tkinter.StringVar(jsq, "")
contentEnter = tkinter.Entry(jsq, textvariable=contentVar)
contentEnter['state'] = "readonly"
contentEnter.place(x=25, y=30, width=400, height=50)
contentEnter.configure(font=('Helvetica', 20))
# 定义按钮和布局
bvalue = ['C', '(', ')', '/', '*', 'back', '1', '2', '3', '+', '-', '**', '4', '5', '6', 'sin', 'cos', 'tan',
          '7', '8', '9', 'asin', 'acos', 'atan', '0', '.']
index = -1
for i in range(6):
    for j in range(5):
        index += 1
        if index > 25:
            break
        d = bvalue[index]
        btnDigit = tkinter.Button(jsq, text=d, command=lambda x=d: onclick(x))
        btnDigit.place(x=25+j*70, y=100+i*80, width=60, height=60)
        btnDigit.configure(font=('Helvetica', 20))

btnDigit = tkinter.Button(jsq, text='=', command=lambda x="=": onclick(x))
btnDigit.place(x=95, y=500, width=130, height=60)
btnDigit.configure(font=('Helvetica', 20))

# 定义运算方法
def onclick(btn):
    nop = ('+', '-', '*', '/')
    hop = ('sin', 'cos', 'tan', '**', 'asin', 'acos', 'atan')
    content = contentVar.get()

    if content.startswith('.'):
        content = '0' + content

    if btn in '0123456789':
        content += btn

    elif btn == 'back':
        content = content[0:-1]

    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:
            tkinter.messagebox.showerror('错误', '已有小数点')
            return
        content += btn

    elif btn == 'C':
        content = ''

    elif btn == '(' or btn == ')':
        content += btn

    elif btn == '=':
        content = str(method(content))

    elif btn in nop:
        if content.endswith(nop):
            tkinter.messagebox.showerror('错误', '不允许存在连续运算符')
            return
        content += btn

    elif btn in hop:

        if content.endswith(hop):
            tkinter.messagebox.showerror('错误', '表达式有误')
            return
        if btn != '**':
            content += btn
            content += "("
        else:
            content += btn

    contentVar.set(content)

def method(result):
    try:
        x = eval(result)
    except:
        tkinter.messagebox.showerror('错误', '表达式有误')
    return x

# 运行
if __name__ == '__main__':
    jsq.mainloop()
