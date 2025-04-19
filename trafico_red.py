from scipy.integrate import quad

print("Función lineal: R(t) = a + b·t")
a = float(input("Ingresa el valor de a (Mbps): "))
b = float(input("Ingresa el valor de b (Mbps/h): "))
inicio = float(input("Ingresa el tiempo de inicio (en horas): "))
fin = float(input("Ingresa el tiempo final (en horas): "))

# definimos la función R(t)
def R(t):
    return a + b * t

# volumen de datos transmitidos
volumen, _ = quad(R, inicio, fin)

# Mbps·h a GB 
gb = volumen * 450 / 1024

print(f"\nResultados:")
print(f"- Total transmitido: {volumen:.2f} Mbps·h")
print(f"- Aproximadamente: {gb:.2f} GB transmitidos")
