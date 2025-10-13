"""
Método de Newton-Raphson 
Propio de: Nayelin Cutipa
Curso: Programación Numérica
Fecha: 08/10/2025
"""

import math

def derivada_numerica(f, x, h=1e-6):
    """Aproximación de la derivada de f en x usando diferencias centradas."""
    return (f(x + h) - f(x - h)) / (2 * h)

def newton_raphson(f, x0, tol=1e-12, max_iter=100):
    """
    Método de Newton-Raphson con derivada numérica automática.
    f: función
    x0: valor inicial
    tol: tolerancia
    max_iter: número máximo de iteraciones
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = derivada_numerica(f, x)

        if dfx == 0:
            print(f"Error: la derivada se anuló en la iteración {i}.")
            return None

        x_next = x - fx / dfx

        if abs(x_next - x) < tol:
            print(f"Convergencia alcanzada en la iteración {i+1}")
            return x_next

        x = x_next

    print("El método no convergió en el número máximo de iteraciones.")
    return None

print("=== MÉTODO DE NEWTON-RAPHSON ===\n")

funcion = input("Ingresa f(x): ")     
x0 = float(input("Ingresa el valor inicial x0: "))

f = lambda x: eval(funcion)

raiz = newton_raphson(f, x0)

if raiz is not None:
    print(f"\nRaíz aproximada: {raiz:.12f}")
