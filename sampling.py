import numpy as np
import matplotlib.pyplot as plt

total_muestras = 14

# Primera grafica, se conserva la frecuencia con sampling rate multiplo entero del periodo. 

plt.figure(1)
N = 1 # periodo
Ts = N/(total_muestras-1) # Sampling rate
v = Ts/N # frecuencia normalizada.
k = N*v
ciclos = v*total_muestras # Total de ciclos.
print(ciclos)
n = np.arange(0, total_muestras, 1) # tiempo discreto 
y = np.sin(2*np.pi*k*n) # funcion de tiempo discreto.
plt.stem(Ts*n, y)
t = np.arange(0, N, N/500)
plt.plot(t, np.sin(2*np.pi*t))

# Segunda grafica con sampling rate con numero racional.
plt.figure(2)
Ts2 = N/8.5 # Sampling rate
v2 = Ts2/N # frecuencia normalizada.
k2 = N*v2
ciclos2 = v2*total_muestras # Total de ciclos.
print(ciclos2)
n2 = np.arange(0, total_muestras, 1) # tiempo discreto 
y2 = np.sin(2*np.pi*k2*n2) # funcion de tiempo discreto.
plt.stem(Ts2*n, y2)
t2 = np.arange(0, ciclos2*N, ciclos2*N/500)
plt.plot(t2, np.sin(2*np.pi*t2))
plt.show()
