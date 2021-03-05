import numpy as np
import matplotlib.pyplot as plt

mg = 10

xlist = np.linspace(0,np.pi/2,100)
f1 = 3*mg/2*(np.sin(xlist)*np.cos(xlist)*3/2-np.cos(xlist))
f2 = 3*mg/2*(-np.sin(xlist)+(3*np.sin(xlist)**2-1)/2) + mg

plt.plot(xlist, f1, '-', markersize=1, label = r"$F_x$")
plt.plot(xlist, f2, '-', markersize=1, label = r"$F_y$")
plt.title("Constraint forces")
plt.xlabel(r"$\varphi$")
plt.ylabel("mg")
plt.grid()
plt.legend()
plt.show()
