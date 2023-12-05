import random

def esta_dentro_circulo(x, y):
    
    # Verifica si un punto (x, y) está dentro de la circunferencia de radio 1 centrada en el origen.
    # La condición para estar dentro es x^2 + y^2 <= 1.
    
    condicion_dentro = x**2 + y**2 <= 1
    return condicion_dentro

def estimar_pi(n):
    
    #Estima el valor de pi utilizando el método de Monte Carlo con n puntos aleatorios.
    #Devuelve la estimación de pi basada en la proporción de puntos dentro de la circunferencia.
    
    contador_dentro = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        dentro = esta_dentro_circulo(x, y)

        if dentro:
            contador_dentro += 1

    estimacion_pi = (contador_dentro / n) * 4
    return estimacion_pi

if __name__ == "__main__":
    num_puntos = 100
    aproximacion_pi = estimar_pi(num_puntos)
    print(f"Aproximación de Pi con {num_puntos} puntos aleatorios: {aproximacion_pi}")