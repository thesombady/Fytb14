from sympy import *
from math import sqrt
init_printing(use_unicode=True)
m = Symbol('m', postive = True)
k = Symbol('k')
w = Symbol('w')
M = m*eye(6)
q = sqrt(3)/4
K = k*Matrix([[5/4, -1, -1/4, q, 0 , -q],
    [-1, 5/4, -1/4, 0, -q, q],
    [-1/4, -1/4, 1/2, -q, q, 0],
    [q, 0, -q, 3/4, 0, -3/4],
    [0, q, -q, 0, -3/4, 3/4],
    [-q, q, q, -3/4, 3/4, 0]])
E = (K-w**2*M)
print(E.eigenvects())
