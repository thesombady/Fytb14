import matplotlib.pyplot as plt
from sympy import *
import math
import numpy as np
init_printing(use_unicode=True)
m1 = Symbol('m1', postive = True)
m2 = Symbol('m2', postive = True)
m3 = Symbol('m3', postive = True)
m = Symbol('m', postive = True)

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
for i in range(len(eigenvectors)):
    try:
        print(f"Eigenvalue:",eigenvectors[i][0])
        a = K2*Matrix([eigenvectors[i][2]])
        print(f"Compuation:", a)
        print(f"Actual eigenvector:",eigenvectors[i][2])
    except Exception as e:
        print(e)
"""
vectors = (K2-w**2*M_m).eigenvects()
#print(vectors[1][2])
for i in range(len(vectors)):
    eigenvalue = vectors[i][0]
    eigenvector = Matrix(vectors[i][2])
    try:
        print(f"Mul{K*eigenvector}, eigenvalue {eigenvalue}")
    except:
        print(eigenvector.shape, "first is multiplicity of two")
#
print(vectors)
#E = K-w*M
#print(E.det())
"""
"""
#E = K-w**2*M
#print(E.det())
#print(M.shape)
#print(E.shape)
q1x = Symbol('q1x')
q2x = Symbol('q2x')
q3x = Symbol('q3x')
q1y = Symbol('q1y')
q2y = Symbol('q2y')
q3y = Symbol('q3y')

l = Symbol('l')
s1 = (q2x+l-q1x)
s2 = (1/2*(q2x+l/2-q3x)-np.sqrt(3)/2*(q2y-q3y-np.sqrt(3)/2*l))
s3 = (1/2*(q3x+l/2-q1x)+np.sqrt(3)/2*(q3y+np.sqrt(3)/2*l-q1y))
L = 1/2*k*(s1**2+s2**2+s3**2-2*l*(s1+s2+s3)+3*l**2)
print("Differented L with q1x:",diff(L, q1x))
print("Differented L with q2x:",diff(L, q2x))
print("Differented L with q3x:",diff(L, q3x))
print("Differented L with q1y:",diff(L, q1y))
print("Differented L with q2y:",diff(L, q2y))
print("Differented L with q3y:",diff(L, q3y))
"""
