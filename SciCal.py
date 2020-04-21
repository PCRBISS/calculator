"""
Created on Sun Apr 19 2020
Finished on Mon Apr 20 2020

@author: 王多益
"""
import numpy as np
import sympy as sym
import math

def MatrixD(matrix):
    a = np.linalg.det(matrix)
    print (a)
    

def MatrixFeature(matrix):
    value,vector = np.linalg.eig(matrix)
    print (round(value,2),round(vector,2))
    

def MatrixReverse(matrix):
    i = np.linalg.det(matrix)
    if i != 0 :
      a = np.linalg.inv(matrix)
    else:
      print("error")
    print(a)
    

def MatrixMultiply(matrixA,matrixB):
    if matrixA.shape[1] == matrixB.shape[0]:
       a = np.dot(matrixA,matrixB)
       print(a)
    else:
       print("error")
    
#以上为矩阵运算部分


def Integral_def(func,up,down):    #定积分，up,down都是数字
    x = sym.symbols('x')
    temp = sym.integrate(x,(func,up,down))
    a = round(temp,4)

def Integral_indef(func):    #不定积分，不含常数项
    x = sym.symbols('x')
    a = sym.integrate(func,x)

def diff_indef(func):    #求微分
    x = sym.symbols('x')
    a = sym.diff(func,x)

def diff_def(func,num):    #num为数字
    x = sym.symbols('x')
    temp = func.diff().evalf(subs={x:num})
    a = round(temp,4)

#以上为微分与积分模块


def exp(base,index):
    temp = base ** index
    a = round(temp,4)

def log(num,base):
    temp = math.log(num,base)
    a = round(temp,4)

#以上为指数，对数运算模块


def sin_an(num):    #num为角度
    temp = math.sin(num*math.pi/180)
    a = round(temp,4)

def sin_rad(num):    #num为弧度
    temp = math.sin(num)
    a = round(temp,4)

def cos_an(num):    #num为角度
    temp = math.cos(num*math.pi/180)
    a = round(temp,4)

def cos_rad(num):    #num为弧度
    temp = math.cos(num)
    a = round(temp,4)

def tan_an(num):    #num为角度
    temp = math.tan(num*math.pi/180)
    a = round(temp,4)
    a = round(temp,4)

def tan_rad(num):    #num为弧度
    temp = math.tan(num)
    a = round(temp,4)

def asin_an(num):    #输出角度
    temp = math.asin(num)*180/math.pi    
    a = round(temp,4)

def asin_rad(num):    #输出弧度
    temp = math.asin(num)
    a = round(temp,4)

def acos_an(num):    #输出角度
    temp = math.acos(num)*180/math.pi
    a = round(temp,4)

def acos_rad(num):    #输出弧度
    temp = math.acos(num)
    a = round(temp,4)

def atan_an(num):    #输出角度
    temp = math.atan(num)*180/math.pi
    a = round(temp,4)

def asin_rad(num):    #输出弧度
    temp = math.atan(num)
    a = round(temp,4)

#以上为三角函数部分