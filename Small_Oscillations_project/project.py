import matplotlib.pyplot as plt
from sympy import *
import math
import numpy as np
init_printing(use_unicode=True)
m1 = Symbol('m1', postive = True)
m2 = Symbol('m2', postive = True)
m3 = Symbol('m3', postive = True)
m = Symbol('m', postive = True)
import SacraMathEngine as s

M=Matrix([[m1,0,0,0,0,0],[0,m2,0,0,0,0], [0,0,m3,0,0,0],[0,0,0,m1,0,0],[0,0,0,0,m2,0],[0,0,0,0,0,m3]])
k = Symbol('k')
w = Symbol('w')

M_m = Matrix([[m,0,0,0,0,0],[0,m,0,0,0,0], [0,0,m,0,0,0],[0,0,0,m,0,0],[0,0,0,0,m,0],[0,0,0,0,0,m]])

q = np.sqrt(3)/4
K = k*Matrix([[5/4,-1,-1/4,q,0,-q],
    [-1,5/4, -1/4,0,-q, q],
    [-1/4,-1/4,1/2,-q,q,0],
    [q,0,-q,3/4,0,-3/4],
    [0,-q,q,0,3/4,-3/4],
    [-q,-q,0,-3/4,-3/4,3/2]])
K2 = k*Matrix([[5/4, -1, -1/4, q, 0, -q],
    [-1, 5/4, -1/4, 0, -q, q],
    [-1/4, -1/4, 1/2, -q, q, 0],
    [q, 0, -q, 3/4, 0, -3/4],
    [0,-q, q, 0, 3/4, -3/4],
    [-q, q, 0, -3/4,-3/4, 3/2]])


#print((K-w**2*M_m).eigenvals())
#print(K2.shape)
eigenvectors = (K2-w**2*M_m).eigenvects()
#print((K2-w**2*M_m).det())
"""
for i in range(len(eigenvectors)):
    print("Eigenvalue:", eigenvectors[i][0])
    print("multiplicity:", eigenvectors[i][1])
    print("Eigenvectors:", eigenvectors[i][2])
"""

for i in range(len(eigenvectors)):
    try:
        print("new vector")
        print(K2*Matrix(eigenvectors[i][2]))
        print(eigenvectors[i][0])
        print(eigenvectors[i][2])
    except Exception as e:
        print(e)
