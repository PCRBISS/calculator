"""
Created on Tue Apr 21 2020
Finished on Tue Apr 21 2020

@author: 王多益
"""

import sympy as sym

def Sol_equation(left,var):    #支持一元一次，一元二次，二元一次
    a = sym.solve(left,var)
    print(a)

'''测试代码
x,y = sym.symbols('x,y')
func = []
moto = input('输入方程:')
func = moto.split(',')
var = []
for i in range(0,len(moto)):
    if moto[i] == 'x' :
        var.append(x)
    if moto[i] == 'y' :
        var.append(y)
var = list(set(var))
print(func)
print(var)
Sol_equation(func,var)
'''