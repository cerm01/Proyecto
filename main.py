import numpy as np
import matplotlib.pyplot as plt
import math

# Creamos la gráfica utilizando Matplotlib
fig, ax = plt.subplots()

# Establecemos la proporción de los ejes en 1 a 1
ax.set_aspect('equal')


# Definimos las coordenadas de los vértices del rectángulo
x1, y1 = 1, 1
x2, y2 = 5, 3
x3, y3 = 4, 5
x4, y4 = 0, 3

# Dibujamos las líneas que conectan los cuatro puntos
ax.plot([x1, x2], [y1, y2], color='r')
ax.plot([x2, x3], [y2, y3], color='r')
ax.plot([x3, x4], [y3, y4], color='r')
ax.plot([x4, x1], [y4, y1], color='r')

#Puerto de visión
x5, y5 = 0,0
x6, y6 = 0,1
x7, y7 = 1,1
x8, y8 = 1,0

#Dibujamos las líneas que conectan los cuatro puntos
ax.plot([x5, x6], [y5, y6], color='r')
ax.plot([x6, x7], [y6, y7], color='r')
ax.plot([x7, x8], [y7, y8], color='r')
ax.plot([x8, x5], [y8, y5], color='r')

# Definimos las funciones h(t) e i(t)
def h(t):
    return 2.5 + 0.5*np.sin(t)

def i(t):
    return 3 + 0.5*np.cos(t)

# Creamos un arreglo de valores de t
t = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Evaluamos las funciones h(t) e i(t) en los valores de t
x = h(t)
y = i(t)

# Dibujamos la gráfica de las funciones h(t) e i(t)
ax.plot(x, y)

# Sacamos la pendiente de la recta x1, y1, x2, y2
m1 = (y2-y1)/(x2-x1)

# Matriz de rotación con respecto a un punto
R = np.array([[(2/math.sqrt(5)),(1/math.sqrt(5)),(1-(3/math.sqrt(5)))],
              [(-1/math.sqrt(5)),(2/math.sqrt(5)),(1-(1/math.sqrt(5)))],
              [(0),(0),(1)]])

# Distancia entre los puntos x1, y1 y x2, y2
d1 = math.sqrt((x2-x1)**2+(y2-y1)**2)

# Distancia entre los puntos x1, y1 y x4, y4
d2 = math.sqrt((x4-x1)**2+(y4-y1)**2)

#Sx y Sy
Sx = 1/d1
Sy = 1/d2

#Matriz N 
N = np.array([[Sx, 0, -Sx],
              [0, Sy, -Sy],
              [0, 0, 1]])

# Multiplica la matriz N por la matriz R
M = np.dot(N,R)

# 
xp = []
yp = []
a = 0.0
b = 0.0

for j in range(len(t)):
    aux = t[j]
    a = h(aux)
    b = i(aux)
    c = np.array([[a],[b],[1]])
    cp = np.dot(M,c)
    xp.append(cp[0])
    yp.append(cp[1])


ax.plot(xp,yp)

# Mostramos la gráfica
plt.show()
