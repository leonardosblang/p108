# -*- coding: utf-8 -*-
"""
Shortest Path solved by Integer Linear Programming.

Solution of Example 1, class P108 at Inatel.

@author: guilherme

From book Pesquisa Operacional - Oitava Edicao - Hamdy A. Taha
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
x12, x13, x14, x25, x26, x35, x36, x37, x46, x47, x58, x68, x78 = m.Array(m.Var,13,integer=True,lb=0)
m.Minimize(U*x12 + T*x13 + S*x14 + P*x25 + Q*x26 + R*x35 + K*x36 + L*x37 + M*x46 + N*x47 + B*x58 + C*x68 + D*x78)
m.Equations([1 == x12 + x13 + x14,
x12 == x25 + x26,
x13 == x35 + x36 + x37,
x14 == x46 + x47,
x25 + x35 == x58,
x26 + x36 + x46 == x68,
x37 + x47 == x78,
x58 + x68 + x78 == 1])
m.options.SOLVER = 1
m.solve()
print('Objective: ', m.options.OBJFCNVAL)
print('x12: ', x12.value[0])
print('x13: ', x13.value[0])
print('x14: ', x14.value[0])
print('x25: ', x25.value[0])
print('x26: ', x26.value[0])
print('x35: ', x35.value[0])
print('x36: ', x36.value[0])
print('x37: ', x37.value[0])
print('x46: ', x46.value[0])
print('x47: ', x47.value[0])
print('x58: ', x58.value[0])
print('x68: ', x68.value[0])
print('x78: ', x78.value[0])
