#!/usr/bin/env python
# coding: utf-8


# 成功 计算器

from tkinter import *
import tkinter.font
from functools import partial
import math
import numpy as np
import random
from scipy.special import comb
import sympy as sym
import symbol

root1 = Tk()
root1.title('操作面板')

def hans1():
    root = Toplevel()
    root.title("计算器")
    root.resizable(0, 0)
    
    def get_input(entry, argu):
        entry.insert(END, argu)


    def backspace(entry):
        input_len = len(entry.get())
        entry.delete(input_len - 1)


    def clear(entry):
        entry.delete(0, END)


    def calc(entry):
        input = entry.get()
        output = str(eval(input.strip()))
        clear(entry)
        entry.insert(END, output)



    def sin_an(entry):    #num为角度
        input = entry.get()
        num = float(input.strip())
        temp = math.sin(num*math.pi/180)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)


    def sin_rad(entry):    #num为弧度
        input = entry.get()
        num = float(input.strip())
        temp = math.sin(num)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)

    def cos_an(entry):    #num为角度
        input = entry.get()
        num = float(input.strip())
        temp = math.cos(num*math.pi/180)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)

    def cos_rad(entry):    #num为弧度
        input = entry.get()
        num = float(input.strip())
        temp = math.cos(num)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)

    def tan_an(entry):    #num为角度
        input = entry.get()
        num = float(input.strip())
        temp = math.tan(num*math.pi/180)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)

    def tan_rad(entry):    #num为弧度
        input = entry.get()
        num = float(input.strip())
        temp = math.tan(num)
        a = round(temp,4)
        clear(entry)
        entry.insert(END, a)

    entry_font = tkinter.font.Font(size=12)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, sticky=N+W+S+E, padx=5,  pady=5)

    button_font = tkinter.font.Font(size=10, weight=tkinter.font.BOLD)
    button_bg = '#D5E0EE'
    button_active_bg = '#E5E35B'

    myButton = partial(Button, root, bg=button_bg, padx=10, pady=3, activebackground = button_active_bg)

    button7 = myButton(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=1, column=0, pady=5)

    button8 = myButton(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=1, column=1, pady=5)

    button9 = myButton(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=1, column=2, pady=5)

    button10 = myButton(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=1, column=3, pady=5)

    button4 = myButton(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=2, column=0, pady=5)

    button5 = myButton(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=2, column=1, pady=5)

    button6 = myButton(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=2, column=2, pady=5)

    button11 = myButton(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=2, column=3, pady=5)

    button1 = myButton(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=3, column=0, pady=5)

    button2 = myButton(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=3, column=1, pady=5)

    button3 = myButton(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=3, column=2, pady=5)

    button12 = myButton(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=3, column=3, pady=5)

    button0 = myButton(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=4, column=0, columnspan=2, padx=3, pady=5, sticky=N+S+E+W)

    button13 = myButton(text='.', command=lambda: get_input(entry, '.'))
    button13.grid(row=4, column=2, pady=5)

    button14 = Button(root, text='/', bg=button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '/'))
    button14.grid(row=4, column=3, pady=5)

    button15 = Button(root, text='<-', bg=button_bg, padx=10, pady=3,
                      command=lambda: backspace(entry), activebackground=button_active_bg)
    button15.grid(row=5, column=0, pady=5)

    button16 = Button(root, text='C', bg=button_bg, padx=10, pady=3,
                      command=lambda : clear(entry), activebackground=button_active_bg)
    button16.grid(row=5, column=1, pady=5)

    button17 = Button(root, text='=', bg=button_bg, padx=10, pady=3,
                      command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=2, columnspan=2, padx=3, pady=5, sticky=N+S+E+W)

    button18 = Button(root, text='sin', bg=button_bg, padx=10, pady=3,
                      command=lambda : sin_an(entry), activebackground=button_active_bg)
    button18.grid(row=1, column=4, pady=5)
    
    button19 = Button(root, text='sinh', bg=button_bg, padx=10, pady=3,
                      command=lambda : sin_rad(entry), activebackground=button_active_bg)
    button19.grid(row=1, column=5, pady=5)
    
    button20 = Button(root, text='cos', bg=button_bg, padx=10, pady=3,
                      command=lambda : cos_an(entry), activebackground=button_active_bg)
    button20.grid(row=2, column=4, pady=5)
    
    button21 = Button(root, text='cosh', bg=button_bg, padx=10, pady=3,
                      command=lambda : cos_rad(entry), activebackground=button_active_bg)
    button21.grid(row=2, column=5, pady=5)
    
    button22 = Button(root, text='tan', bg=button_bg, padx=10, pady=3,
                      command=lambda : tan_an(entry), activebackground=button_active_bg)
    button22.grid(row=3, column=4, pady=5)
    
    button23 = Button(root, text='tanh', bg=button_bg, padx=10, pady=3,
                      command=lambda : tan_rad(entry), activebackground=button_active_bg)
    button23.grid(row=3, column=5, pady=5)
    
    button12 = myButton(text='指数', command=lambda: get_input(entry, '**'))
    button12.grid(row=4, column=4, pady=5)
    
    button23 = Button(root, text='对数', bg=button_bg, padx=10, pady=3,
                      command=lambda : log(entry), activebackground=button_active_bg)
    button23.grid(row=4, column=5, pady=5)

def hans2():
    root2 = Toplevel()
    root2.title('解方程')

    frame = Frame(root2)
    
    def hans21():
        root21 = Toplevel()
        root21.title('解一元一次方程')

        frame = Frame(root21)

        Label(root21, text = '参数名称').grid(row = 0, column = 0)
        Label(root21, text = '值').grid(row = 0, column = 1)
        Label(root21, text = '表达式（左）').grid(row = 1, column = 0)
        Label(root21, text = '表达式（右）').grid(row = 2, column = 0)
        Label(root21, text = '未知数').grid(row = 3, column = 0)

        e1 = Entry(root21)
        e2 = Entry(root21)
        e3 = Entry(root21)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)

        v1 = StringVar()
        e4 = Entry(root21, width=10, textvariable=v1, state='readonly').grid(row=4, column=1)

        def ans():
            x=sym.symbols(str(e3.get()))
            v1.set(sym.solve(eval(e1.get()) - eval(e2.get()), x))

        Button(root21, text='求解', width=10, command=ans).grid(row=4, column=0, sticky=W, padx=10, pady=5)
        
    def hans22():
        root22 = Toplevel()
        root22.title('解二元一次方程')

        frame = Frame(root22)

        Label(root22, text = '参数名称').grid(row = 0, column = 0)
        Label(root22, text = '值').grid(row = 0, column = 1)
        Label(root22, text = '表达式一（左）').grid(row = 1, column = 0)
        Label(root22, text = '表达式一（右）').grid(row = 2, column = 0)
        Label(root22, text = '表达式二（左）').grid(row = 3, column = 0)
        Label(root22, text = '表达式二（右）').grid(row = 4, column = 0)
        Label(root22, text = '未知数一').grid(row = 5, column = 0)
        Label(root22, text = '未知数二').grid(row = 6, column = 0)

        e1 = Entry(root22)
        e2 = Entry(root22)
        e3 = Entry(root22)
        e4 = Entry(root22)
        e5 = Entry(root22)
        e6 = Entry(root22)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e4.grid(row=4, column=1, padx=10, pady=5)
        e5.grid(row=5, column=1, padx=10, pady=5)
        e6.grid(row=6, column=1, padx=10, pady=5)

        v1 = StringVar()
        e4 = Entry(root22, width=10, textvariable=v1, state='readonly').grid(row=7, column=1)
        
        def ans():
            x,y = sym.symbols(str(e5.get()) + str(e6.get()))
            v1.set(sym.solve([eval(e1.get()) - eval(e2.get()),eval(e3.get()) - eval(e4.get())], [x, y]))

        Button(root22, text='求解', width=10, command=ans).grid(row=7, column=0, sticky=W, padx=10, pady=5)
    
    def hans23():
        root23 = Toplevel()
        root23.title('解一元二次方程')

        frame = Frame(root23)

        Label(root23, text = 'ax2 + bx + c = 0').grid(row = 0, column = 0)
        Label(root23, text = '值').grid(row = 0, column = 1)
        Label(root23, text = 'a的值').grid(row = 1, column = 0)
        Label(root23, text = 'b的值').grid(row = 2, column = 0)
        Label(root23, text = 'c的值').grid(row = 3, column = 0)

        e1 = Entry(root23)
        e2 = Entry(root23)
        e3 = Entry(root23)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)

        v1 = StringVar()
        e4 = Entry(root23, width=10, textvariable=v1, state='readonly').grid(row=4, column=1)
        
        def quadratic():
            a = float(e1.get())
            b = float(e2.get())
            c = float(e3.get())
            if a == 0:
                if b == 0:
                    if c == 0:
                        d = '方程有任意解'
                    else:
                        d = '方程无解'
                else:
                    x = -c / b
                    d = '方程有解：x=%.2f' % x
            else:
                q = b * b - 4 * a * c
                if q > 0:
                    x1 = (-b + math.sqrt(q)) / a / 2
                    x2 = (-b - math.sqrt(q)) / a / 2
                    d = "一元二次方程的解为x1=%.2f，x2=%.2f" % (x1, x2)
                elif q == 0:
                    x1 = -b / a / 2
                    x2 = x1
                    d = "一元二次方程的解相同，x1=x2=%.2f" % (x1)
                else:
                    pass
                    d = "一元二次方程无解"
                    
            v1.set(d)

        Button(root23, text='求解', width=20, command=quadratic).grid(row=4, column=0, sticky=W, padx=10, pady=5) 
    
    Button21 = Button(root2, text='求一元一次方程', width=20, command = hans21).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Button22 = Button(root2, text='求二元一次方程', width=20, command = hans22).grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Button23 = Button(root2, text='求一元二次方程', width=20, command = hans23).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    

    
def hans3():
    root3 = Toplevel()
    root3.title('分解质因数')
    frame = Frame(root3)

    Label(root3, text = '参数名称').grid(row = 0, column = 0)
    Label(root3, text = '值').grid(row = 0, column = 1)
    Label(root3, text = '数字').grid(row = 1, column = 0)

    e1 = Entry(root3, width=10)
    e1.grid(row=1, column=1, padx=10, pady=5)

    v1 = StringVar()
    e2 = Entry(root3, width=10, textvariable=v1, state='readonly').grid(row=4, column=1)

    def Factorize():
        n=eval(e1.get())
        num=n    #使用num变量保留输入的原始数值
        m=[]
        while n!=1:    #n==1时，已分解到最后一个质因数
            for i in range(2,int(n+1)):
                if n % i == 0:
                    m.append(str(i))    #将i转化为字符串再追加到列表中，便于使用join函数进行输出
                    n = n/i
            if n==1:
                m.pop()
                break    #n==1时，循环停止
        v1.set(m)

    Button(root3, text='计算', width=10, command=Factorize).grid(row=4, column=0, sticky=W, padx=10, pady=5)

def hans4():
    root4 = Toplevel()
    root4.title('金融计算')


    def hans41():
        root41 = Toplevel()
        root41.title('求将来资金总值')
        frame = Frame(root41)

        Label(root41, text = '参数名称').grid(row = 0, column = 0)
        Label(root41, text = '值').grid(row = 0, column = 1)
        Label(root41, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root41, text = 'nper年数').grid(row = 2, column = 0)
        Label(root41, text = 'pmt月供').grid(row = 3, column = 0)
        Label(root41, text = 'pv现在资金总额').grid(row = 4, column = 0)

        e1 = Entry(root41)
        e2 = Entry(root41)
        e3 = Entry(root41)
        e4 = Entry(root41)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e4.grid(row=4, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root41, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Future_Value():    #利率可以是数值or矩阵
            a = np.fv(eval(e1.get()), eval(e2.get()), eval(e3.get()), eval(e4.get()))
            a = 0 - a
            v1.set(a)

        Button(root41, text='将来资金总值', width=10, command = Future_Value).grid(row=5, column=0, sticky=W, padx=10, pady=5)

    def hans42():
        root42 = Toplevel()
        root42.title('求现在需投资资金总额')
        frame = Frame(root42)

        Label(root42, text = '参数名称').grid(row = 0, column = 0)
        Label(root42, text = '值').grid(row = 0, column = 1)
        Label(root42, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root42, text = 'nper年数').grid(row = 2, column = 0)
        Label(root42, text = 'pmt月供').grid(row = 3, column = 0)
        Label(root42, text = 'fv期望资金总额').grid(row = 4, column = 0)

        e1 = Entry(root42)
        e2 = Entry(root42)
        e3 = Entry(root42)
        e4 = Entry(root42)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e4.grid(row=4, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root42, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Present_Value():
            a = np.pv(eval(e1.get()), eval(e2.get()), eval(e3.get()), eval(e4.get()))
            a = 0 - a
            v1.set(a)

        Button(root42, text='求现在需投资资金总额', width=10, command = Present_Value).grid(row=5, column=0, sticky=W, padx=10, pady=5)

    def hans43():
        root43 = Toplevel()
        root43.title('求每月利润')
        frame = Frame(root43)

        Label(root43, text = '参数名称').grid(row = 0, column = 0)
        Label(root43, text = '值').grid(row = 0, column = 1)
        Label(root43, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root43, text = 'nper年数').grid(row = 2, column = 0)
        Label(root43, text = 'pv现在资金总额').grid(row = 4, column = 0)

        e1 = Entry(root43)
        e2 = Entry(root43)
        e3 = Entry(root43)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root43, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Payment():
            a = np.pmt(eval(e1.get()), eval(e2.get()), eval(e3.get()))
            a = 0 - a
            v1.set(a)

        Button(root43, text='每月利润', width=10, command = Payment).grid(row=5, column=0, sticky=W, padx=10, pady=5)


    def hans445():
        root445 = Toplevel()
        root445.title('求月供本金、利息')
        frame = Frame(root445)

        Label(root445, text = '参数名称').grid(row = 0, column = 0)
        Label(root445, text = '值').grid(row = 0, column = 1)
        Label(root445, text = 'rate欠款利率(小数)').grid(row = 1, column = 0)
        Label(root445, text = 'nper总期数').grid(row = 2, column = 0)
        Label(root445, text = 'pv现在欠款总额').grid(row = 3, column = 0)
        Label(root445, text = 'per第n个偿还期').grid(row = 4, column = 0)

        e1 = Entry(root445)
        e2 = Entry(root445)
        e3 = Entry(root445)
        e4 = Entry(root445)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e4.grid(row=4, column=1, padx=10, pady=5)

        v1 = StringVar()
        e5 = Entry(root445, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        v2 = StringVar()
        e6 = Entry(root445, width=10, textvariable=v2, state='readonly').grid(row=6, column=1)


        def Payment_Principal():    #求月供中的本金,per表示在第几个偿还期
            a = np.ppmt(eval(e1.get()), eval(e2.get()), eval(e3.get()), eval(e4.get()))
            a = 0 - a
            v1.set(a)

        def Payment_Interest():     #要求同上
            a = np.ipmt(eval(e1.get()), eval(e2.get()), eval(e3.get()), eval(e4.get()))
            a = 0 - a
            v2.set(a)

        Button(root445, text='求月供本金', width=10, command = Payment_Principal).grid(row=5, column=0, sticky=W, padx=10, pady=5)
        Button(root445, text='求月供利息', width=10, command = Payment_Interest).grid(row=6, column=0, sticky=W, padx=10, pady=5)    


    def hans467():
        root467 = Toplevel()
        root467.title('求净现值、内部回报率')
        frame = Frame(root467)

        Label(root467, text = '参数名称').grid(row = 0, column = 0)
        Label(root467, text = '值').grid(row = 0, column = 1)
        Label(root467, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root467, text = '每日现金(输入一组数)').grid(row = 2, column = 0)

        e1 = Entry(root467)
        e2 = Entry(root467)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)

        v1 = StringVar()
        e5 = Entry(root467, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        v2 = StringVar()
        e6 = Entry(root467, width=10, textvariable=v2, state='readonly').grid(row=6, column=1)

        def Net_pv():    #values是一个array
            a = np.npv(eval(e1.get()), eval(e2.get()))
            v1.set(a)

        def Internal_Rate_Return():    #要求同上
            a = np.irr(eval(e2.get()))
            v2.set(a)                                                                           


        Button(root467, text='求净现值', width=10, command = Net_pv).grid(row=5, column=0, sticky=W, padx=10, pady=5)
        Button(root467, text='求内部回报率', width=10, command = Internal_Rate_Return).grid(row=6, column=0, sticky=W, padx=10, pady=5)    

    def hans48():
        root48 = Toplevel()
        root48.title('求偿还年数')
        frame = Frame(root48)

        Label(root48, text = '参数名称').grid(row = 0, column = 0)
        Label(root48, text = '值').grid(row = 0, column = 1)
        Label(root48, text = 'rate利率(小数)').grid(row = 1, column = 0)
        Label(root48, text = 'pmt月供').grid(row = 2, column = 0)
        Label(root48, text = 'pv现在欠款总额').grid(row = 3, column = 0)

        e1 = Entry(root48)
        e2 = Entry(root48)
        e3 = Entry(root48)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root48, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Year_nper():
            a = np.nper(float(e1.get())), eval(e2.get()), eval(e3.get())
            a = int(a) + 1
            v1.set(a)

        Button(root48, text='求偿还年数', width=10, command = Year_nper).grid(row=5, column=0, sticky=W, padx=10, pady=5)



    Button1 = Button(root4, text='将来资金总值', width=15, command = hans41).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Button2 = Button(root4, text='现在需投资资金总额', width=15, command = hans42).grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Button3 = Button(root4, text='每月利润', width=15, command = hans43).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Button4 = Button(root4, text='月供本金、利息', width=15, command = hans445).grid(row=3, column=0, sticky=W, padx=10, pady=5)       
    Button5 = Button(root4, text='净现值、内部回报率', width=15, command = hans467).grid(row=4, column=0, sticky=W, padx=10, pady=5)       
    Button6 = Button(root4, text='偿还年数', width=15, command = hans48).grid(row=5, column=0, sticky=W, padx=10, pady=5)       


def hans5():
    root5 = Toplevel()
    root5.title('微积分')


    def hans51():
        root51 = Toplevel()
        root51.title('求解定积分')
        frame = Frame(root51)

        Label(root51, text = '参数名称').grid(row = 0, column = 0)
        Label(root51, text = '值').grid(row = 0, column = 1)
        Label(root51, text = '函数').grid(row = 1, column = 0)
        Label(root51, text = '积分变量').grid(row = 2, column = 0)
        Label(root51, text = '下界').grid(row = 3, column = 0)
        Label(root51, text = '上界').grid(row = 4, column = 0)

        e1 = Entry(root51)
        e2 = Entry(root51)
        e3 = Entry(root51)
        e4 = Entry(root51)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e4.grid(row=4, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root51, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Integral_def():    #定积分，up,down都是数字
            x = sym.symbols(str(e2.get()))
            temp = sym.integrate(x,(eval(e1.get()), eval(e4.get()),eval(e3.get())))
            a = round(temp,4)
            v1.set(a)

        Button(root51, text='计算', width=10, command=Integral_def).grid(row=5, column=0, sticky=W, padx=10, pady=5)

    def hans52():
        root52 = Toplevel()
        root52.title('求解不定积分')
        frame = Frame(root52)

        Label(root52, text = '参数名称').grid(row = 0, column = 0)
        Label(root52, text = '值').grid(row = 0, column = 1)
        Label(root52, text = '函数').grid(row = 1, column = 0)
        Label(root52, text = '积分变量').grid(row = 2, column = 0)

        e1 = Entry(root52)
        e2 = Entry(root52)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root52, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def Integral_indef():    #不定积分，不含常数项
            x = sym.symbols(str(e2.get()))
            a = sym.integrate(eval(e1.get()), x)
            v1.set(a)

        Button(root52, text='计算', width=10, command=Integral_indef).grid(row=5, column=0, sticky=W, padx=10, pady=5)

    def hans53():
        root53 = Toplevel()
        root53.title('求解微分')
        frame = Frame(root53)

        Label(root53, text = '参数名称').grid(row = 0, column = 0)
        Label(root53, text = '值').grid(row = 0, column = 1)
        Label(root53, text = '函数').grid(row = 1, column = 0)
        Label(root53, text = '积分变量').grid(row = 2, column = 0)

        e1 = Entry(root53)
        e2 = Entry(root53)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root53, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def diff_indef():    #求微分
            x = sym.symbols(str(e2.get()))
            a = sym.diff(eval(e1.get()),x)
            v1.set(a)

        Button(root53, text='计算', width=10, command=diff_indef).grid(row=5, column=0, sticky=W, padx=10, pady=5)

    def hans54():
        root54 = Toplevel()
        root54.title('求解微分')
        frame = Frame(root54)

        Label(root54, text = '参数名称').grid(row = 0, column = 0)
        Label(root54, text = '值').grid(row = 0, column = 1)
        Label(root54, text = '函数').grid(row = 1, column = 0)
        Label(root54, text = '积分变量').grid(row = 2, column = 0)
        Label(root54, text = '数字').grid(row = 3, column = 0)

        e1 = Entry(root54)
        e2 = Entry(root54)
        e3 = Entry(root54)
        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        v1 = StringVar()
        e5 = Entry(root54, width=10, textvariable=v1, state='readonly').grid(row=5, column=1)

        def diff_def():    #num为数字
            x = sym.symbols(str(e2.get()))
            temp = eval(e1.get()).diff().evalf(subs={x:eval(e3.get())})
            a = round(temp,4)
            v1.set(a)

        Button(root54, text='计算', width=10, command=diff_def).grid(row=5, column=0, sticky=W, padx=10, pady=5)




    Button51 = Button(root5, text='定积分', width=10, command = hans51).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Button52 = Button(root5, text='不定积分', width=10, command = hans52).grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Button53 = Button(root5, text='微分', width=10, command = hans53).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Button54 = Button(root5, text='微分(有数字)', width=10, command = hans54).grid(row=3, column=0, sticky=W, padx=10, pady=5)       


def hans61():
    root61 = Toplevel()
    root61.title('伤害计算')
    frame = Frame(root61)
    
    def hans6():
        root6 = Toplevel()
        root6.title('伤害计算')
        frame = Frame(root6)

        Label(root6, text = '参数名称').grid(row = 0, column = 0)
        Label(root6, text = '值').grid(row = 0, column = 1)
        Label(root6, text = 'ATK').grid(row = 1, column = 0)
        Label(root6, text = '宝具倍率NP').grid(row = 2, column = 0)
        Label(root6, text = 'RGB卡色(选择以下三种)').grid(row = 3, column = 0)
        Label(root6, text = 'Buster/Art/Quick').grid(row = 4, column = 0) #
        Label(root6, text = 'Class职阶(以下三大类中选择)').grid(row = 5, column = 0)
        Label(root6, text = 'Saber/Archer/Lancher').grid(row = 6, column = 0)
        Label(root6, text = 'Assassin/Caster/Rider/Berseker').grid(row = 7, column = 0)
        Label(root6, text = 'Foreigner/Ruler/Avenger/Mooncacer/Alteregon/Shielder').grid(row = 8, column = 0)
        Label(root6, text = '阵营(克制/被克制/非克制)').grid(row = 9, column = 0)
        Label(root6, text = '职阶相性(克制/被克制/非克制/狂克制)').grid(row = 10, column = 0)
        Label(root6, text = '我方加攻(小数)').grid(row = 11, column = 0)
        Label(root6, text = '敌方加防(小数)').grid(row = 12, column = 0)
        Label(root6, text = '我方魔攻(小数)').grid(row = 13, column = 0)
        Label(root6, text = '我方特攻(小数)').grid(row = 14, column = 0)
        Label(root6, text = '敌方特攻(小数)').grid(row = 15, column = 0)
        Label(root6, text = '宝具威力(小数)').grid(row = 16, column = 0)
        Label(root6, text = '宝具特攻(小数)').grid(row = 17, column = 0)
        Label(root6, text = '我方固定伤害').grid(row = 18, column = 0)
        Label(root6, text = '敌方固定减伤').grid(row = 19, column = 0)

        e1 = Entry(root6)
        e2 = Entry(root6)
        e3 = Entry(root6)
        e5 = Entry(root6)
        e9 = Entry(root6)
        e10 = Entry(root6)
        e11 = Entry(root6)
        e12 = Entry(root6)
        e13 = Entry(root6)
        e14 = Entry(root6)
        e15 = Entry(root6)
        e16 = Entry(root6)
        e17 = Entry(root6)
        e18 = Entry(root6)
        e19 = Entry(root6)

        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e5.grid(row=5, column=1, padx=10, pady=5)
        e9.grid(row=9, column=1, padx=10, pady=5)
        e10.grid(row=10, column=1, padx=10, pady=5)
        e11.grid(row=11, column=1, padx=10, pady=5)
        e12.grid(row=12, column=1, padx=10, pady=5)
        e13.grid(row=13, column=1, padx=10, pady=5)
        e14.grid(row=14, column=1, padx=10, pady=5)
        e15.grid(row=15, column=1, padx=10, pady=5)
        e16.grid(row=16, column=1, padx=10, pady=5)
        e17.grid(row=17, column=1, padx=10, pady=5)
        e18.grid(row=18, column=1, padx=10, pady=5)
        e19.grid(row=19, column=1, padx=10, pady=5)


        v1 = StringVar()
        e21 = Entry(root6, width=30, textvariable=v1, state='readonly').grid(row=20, column=1)

        v2 = StringVar()
        e22 = Entry(root6, width=30, textvariable=v2, state='readonly').grid(row=21, column=1)

        v3 = StringVar()
        e23 = Entry(root6, width=30, textvariable=v3, state='readonly').grid(row=22, column=1)

        Class_Value = 0
        RGB_Value = 0

        def NP_Damage():    #利率可以是数值or矩阵

            global Class_Value, RGB_Value

            ATK = eval(e1.get())
            NP = eval(e2.get())
            RGB = str(eval(e3.get()))
            Class = str(eval(e5.get()))
            Team = str(eval(e9.get()))
            Weak = str(eval(e10.get()))
            ATKbuff = float(e11.get())
            DEFbuff = float(e12.get())
            Cardbuff = float(e13.get())
            SAbuff = float(e14.get())
            SDbuff = float(e15.get())
            NPDbuff = float(e16.get())
            NPSA = float(e17.get())
            RDbuff = eval(e18.get())
            RDdebuff = eval(e19.get())


            List1 = ['Caster','Assassin']
            List2 = ['Saber','Foreigner','Mooncancer', 'Rider','Shielder','Alterego']
            List3 = ['Berserker','Ruler','Avenger']

            if Class in List1:
                Class_Value = 0.9
            if Class == 'Archer':
                Class_Value = 0.95
            if Class in List2:
                Class_Value = 1
            if Class == 'Lancer':
                Class_Value = 1.05 
            if Class in List3:
                Class_Value = 1.1
            #职阶补正

            if RGB == 'Buster':
                RGB_Value = 1.5
            elif RGB == 'Arts':
                RGB_Value = 1
            elif RGB == 'Quick':
                RGB_Value = 0.8
            #卡牌伤害倍率

            if Weak == '克制':
                Weak_Value = 2
            elif Weak == '非克制':
                Weak_Value = 1
            elif Weak == '被克制':
                Weak_Value = 0.5
            elif Weak == '狂克制':
                Weak_Value = 1.5
            #职阶相性

            if Team == '克制':
                Team_Value = 1.1
            elif Team == '非克制':
                Team_Value = 1
            elif Team == '被克制':
                Team_Value = 0.9
            #阵营相性

            Value1 = ATK * 0.23
            Value2 = NP / 100 * RGB_Value * (1+Cardbuff/100)
            Value3 = Class_Value * Weak_Value * Team_Value
            Value4 = 1 + (ATKbuff-DEFbuff) / 100
            Value5 = 1 + (SAbuff-SDbuff+NPDbuff) / 100
            Value6 = 1 + NPSA / 100
            Value7 = RDbuff-RDdebuff
            Value_without_Factor = Value1 * Value2 *Value3 * Value4 * Value5 * Value6
            #简便计算

            Highest = 1.1 * Value_without_Factor + Value7
            Lowest = 0.9 * Value_without_Factor + Value7
            Average = Value_without_Factor + Value7

            a = '最高宝具伤害为：{}'.format(Highest)
            b = '最低宝具伤害为：{}'.format(Lowest)
            c = '平均宝具伤害为：{}'.format(Average)

            v1.set(a)
            v2.set(b)
            v3.set(c)

        Button(root6, text='计算', width=10, command = NP_Damage).grid(row=20, column=0, sticky=W, padx=10, pady=5)

    def hans7():
        root7 = Toplevel()
        root7.title('模拟抽卡')
        frame = Frame(root7)

        Label(root7, text = '参数名称').grid(row = 0, column = 0)
        Label(root7, text = '值').grid(row = 0, column = 1)
        Label(root7, text = 'UP率(小数)').grid(row = 1, column = 0)
        Label(root7, text = '抽几个').grid(row = 2, column = 0)
        Label(root7, text = '抽几次').grid(row = 3, column = 0)

        e1 = Entry(root7)
        e2 = Entry(root7)
        e3 = Entry(root7)

        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)

        v1 = StringVar()
        e5 = Entry(root7, width=10, textvariable=v1, state='readonly').grid(row=4, column=1)

        def gachapro(): #在UP概率下，抽times次，出num个的概率
            UP = eval(e1.get())
            num = eval(e2.get())
            times = eval(e3.get())

            result_comb = comb(times, num)
            UP_New = UP
            result = result_comb * (UP_New**num) * (1-UP_New)**(times-num)
            res_final = str(result*100)[:5] + '%'
            a = res_final
            v1.set(a)

        Button(root7, text='计算', width=10, command = gachapro).grid(row=4, column=0, sticky=W, padx=10, pady=5)
    
    def hans8():
        root8 = Toplevel()
        root8.title('计算概率')
        frame = Frame(root8)

        Label(root8, text = '参数名称').grid(row = 0, column = 0)
        Label(root8, text = '值').grid(row = 0, column = 1)
        Label(root8, text = 'UP率(小数)').grid(row = 1, column = 0)
        Label(root8, text = 'SSR概率(小数)').grid(row = 2, column = 0)
        Label(root8, text = 'SR概率(小数)').grid(row = 3, column = 0)
        Label(root8, text = 'R概率(小数)').grid(row = 4, column = 0)

        e1 = Entry(root8)
        e2 = Entry(root8)
        e3 = Entry(root8)
        e4 = Entry(root8)
        

        e1.grid(row=1, column=1, padx=10, pady=5)
        e2.grid(row=2, column=1, padx=10, pady=5)
        e3.grid(row=3, column=1, padx=10, pady=5)
        e4.grid(row=4, column=1, padx=10, pady=5)

        v1 = StringVar()
        e5 = Entry(root8, width=30, textvariable=v1, state='readonly').grid(row=5, column=1)

        
        def Gacha():    #UPSSR率，SSR概率，SR概率，R概率
            UP = float(e1.get())
            SSR = float(e2.get())
            SR = float(e3.get())
            R = float(e4.get())
            
            
            R_x = int(R * 1000)
            SR_x = int(SR * 1000)
            SSR_x = int(SSR * 1000)
            UP_x = int(UP * 1000)
            List = ['R'] * R_x + ['SR'] * SR_x + ['SSR'] * (SSR_x-UP_x) + ['UP'] * UP_x
            res = []
            for i in range(0,10):
                temp = random.choice(List) 
                res.append(temp)
            if 'SR' and 'SSR' and 'UP' not in res:
                res.pop()
                res.append('SR')
            v1.set(res)

        Button(root8, text='计算', width=5, command = Gacha).grid(row=5, column=0, sticky=W, padx=10, pady=5)

    
    
    Button51 = Button(root61, text='抽卡概率', width=10, command = hans8).grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Button52 = Button(root61, text='模拟抽卡', width=10, command = hans7).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Button53 = Button(root61, text='伤害计算', width=10, command = hans6).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    
Button1 = Button(root1, text='计算器', width=10, command = hans1).grid(row=0, column=0, sticky=W, padx=10, pady=5)
Button2 = Button(root1, text='解方程', width=10, command = hans2).grid(row=1, column=0, sticky=W, padx=10, pady=5)
Button3 = Button(root1, text='分解质因数', width=10, command = hans3).grid(row=2, column=0, sticky=W, padx=10, pady=5)
Button4 = Button(root1, text='金融计算', width=10, command = hans4).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button5 = Button(root1, text='微积分', width=10, command = hans5).grid(row=4, column=0, sticky=W, padx=10, pady=5)
Button6 = Button(root1, text='游戏攻略', width=10, command = hans61).grid(row=5, column=0, sticky=W, padx=10, pady=5)

mainloop()
