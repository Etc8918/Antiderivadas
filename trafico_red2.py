import numpy as np
import matplotlib.pyplot as plt

# Intervalo de tiempo de 1 a 100 dividido en 500 puntos
t = np.linspace(1, 100, 500)

# Función logarítmica que representa el tráfico acumulado
R = 50 * np.log(t + 1)

# Derivada numérica para analizar la tasa de crecimiento
dR_dt = np.gradient(R, t)

# Graficamos la derivada
plt.figure(figsize=(8, 5))
plt.plot(t, dR_dt, label='dR/dt', color='purple')
plt.title('Predicción de Saturación del Tráfico de Red')
plt.xlabel('Tiempo')
plt.ylabel('Tasa de Crecimiento dR/dt')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
