# -*- coding: utf-8 -*-
"""
Maxmum flow solved by Integer Linear Programming.

Solution of Example 1, class P108 at Inatel.

@author: guilherme

"""







from gekko import GEKKO


matricula = 17
a = (matricula%5)+1
b = 1+7

A = a+b
B = a
C = b
D = a+5
E = b-2
F = a+3
G = b-3
H = a+4
I = b-4
J = a
K = a+b
L = b-2
M = a+4
N = b-4
O = b
P = a+5
Q = b-3
R = a+1
S = a+3
T = b-2
U = b-4





m = GEKKO()
x14,x24,x25,x26,x35,x45,x46,x47,x56,x58,x67,x68 =m.Array(m.Var,12,integer=True,lb=0)
m.Maximize(x47+x67+x58+x68) #Maximizing input.
m.Equations([x14+x24==x45+x46+x47,
             x25+x35+x45==x56+x58,
             x26+x46+x56==x67+x68,
             x14<=A,
             x24<=B,
             x25<=D,
             x26<=C,
             x45<=H,
             x35<=E,
             x46<=G,
             x47<=F,
             x56<=I,
             x58<=J,
             x67<=K,
             x68<=L])
m.options.SOLVER = 1
m.solve()
print('Objective: ', -m.options.OBJFCNVAL)

print('x14: ', x14.value[0])
print('x24: ', x24.value[0])
print('x25: ', x25.value[0])
print('x26: ', x26.value[0])
print('x35: ', x35.value[0])
print('x45: ', x45.value[0])
print('x46: ', x46.value[0])
print('x47: ', x47.value[0])
print('x56: ', x56.value[0])
print('x58: ', x58.value[0])
print('x67: ', x67.value[0])
print('x68: ', x68.value[0])