import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid


# TIEMPO DE 0 A 10 HORAS
t = np.linspace(0, 10, 100)

# Función de tasa de transferencia: R(t)
R = 5 + 2 * np.sin(np.pi * t)


# Integral acumulada: volumen total de datos transmitidos
D = cumulative_trapezoid(R, t, initial=0)

# Derivada de R(t): variación de la tasa
dR = np.gradient(R, t)

# Modelo logístico de crecimiento de tráfico
P0 = 10   # Valor inicial
r = 0.5   # Tasa de crecimiento
K = 100   # Capacidad máxima
P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, R, color='blue')
plt.title('Tasa de Transferencia R(t)')
plt.ylabel('Mbps')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, D, color='green')
plt.title('Volumen Acumulado de Datos ∫R(t) dt')
plt.ylabel('MB aprox.')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, dR, color='red', label='dR/dt')
plt.plot(t, P, 'k--', label='Crecimiento Logístico')
plt.title('Variación de Tráfico y Modelo Logístico')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Mbps / Usuarios')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
