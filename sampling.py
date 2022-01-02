import numpy as np
import matplotlib.pyplot as plt

#Ts = 1/3.5 # Sampling rate
#N = 5 # periodo
#v = Ts/N # frecuencia normalizada.
#k = 1/v
#n = np.arange(0, N, Ts) # tiempo discreto basado en Ts
#y = np.sin(2*np.pi*n) # funcion de tiempo discreto.
#plt.stem(n, y)
#plt.show()
#
total_muestras = 16

Ts = 1/3.5 # Sampling rate
N = 1 # periodo
v = Ts/N # frecuencia normalizada.
k = N*v
n = np.arange(0, total_muestras, 1) # tiempo discreto 
y = np.sin(2*np.pi*k*n) # funcion de tiempo discreto.
plt.stem(n, y)
plt.show()
