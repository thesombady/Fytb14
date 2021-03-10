import matplotlib.pyplot as plt
from sympy import *
import math
import numpy as np
init_printing(use_unicode=True)
m1 = Symbol('m1', postive = True)
m2 = Symbol('m2', postive = True)
m3 = Symbol('m3', postive = True)
m = Symbol('m', postive = True)

k = Symbol('k')
w = Symbol('w')
M_m = m*eye(6)
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

eigenvectors = (K2-w**2*M_m).eigenvects()
for i in range(len(eigenvectors)):
    try:
        print("new vector")
        print(K2*Matrix(eigenvectors[i][2]))
        print(eigenvectors[i][0])
        print(eigenvectors[i][2])
    except Exception as e:
        print(e)
