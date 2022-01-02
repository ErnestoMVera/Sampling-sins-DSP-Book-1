import numpy as np
import matplotlib.pyplot as plt

total_muestras = 32

# Primera grafica, se conserva la frecuencia con sampling rate multiplo entero del periodo. 

fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout = True)
N = 5 # periodo
Ts = N/(total_muestras-1) # Sampling rate
v = Ts/N # frecuencia normalizada.
k = N*v
ciclos = v*total_muestras # Total de ciclos.
print(ciclos)
n = np.arange(0, total_muestras, 1) # tiempo discreto 
y = np.sin(2*np.pi*k*n/N) # funcion de tiempo discreto.
ax1.stem(Ts*n, y)
t = np.arange(0, N, N/500)
ax1.plot(t, np.sin(2*np.pi*t/N))
ax1.set_title("periodo/sampling rate entero.")
ax1.set_xlabel("Ts*n")
ax1.set_ylabel("y[n]")
# Segunda grafica con sampling rate con numero racional.
Ts2 = N/4.5 # Sampling rate
v2 = Ts2/N # frecuencia normalizada.
k2 = N*v2
ciclos2 = v2*total_muestras # Total de ciclos.
print(ciclos2)
n2 = np.arange(0, total_muestras, 1) # tiempo discreto 
y2 = np.sin(2*np.pi*k2*n2/N) # funcion de tiempo discreto.
ax2.stem(Ts2*n, y2)
t2 = np.arange(0, ciclos2*N, ciclos2*N/500)
ax2.plot(t2, np.sin(2*np.pi*t2/N))
ax2.set_title("periodo/sampling rate racional.")
ax2.set_xlabel("Ts*n")
ax2.set_ylabel("y[n]")
plt.show()
