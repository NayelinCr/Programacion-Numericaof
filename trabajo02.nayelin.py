import tkinter as tk
import math
import re

def preparar_funcion(expr):

    expr = expr.replace(" ", "")

    expr = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", expr)
    return expr

def graficar():
    canvas.delete("all")


    canvas.create_line(250, 0, 250, 500, fill="black")  
    canvas.create_line(0, 250, 500, 250, fill="black")  


    funciones = [(entrada1.get(), "blue"), (entrada2.get(), "red")]

    for funcion, color in funciones:
        if funcion.strip() == "":
            continue

        funcion = preparar_funcion(funcion) 

        puntos = []
        for x_pixel in range(0, 500):
            x = (x_pixel - 250) / 25  
            try:
                y = eval(funcion, {"x": x, "math": math})
                y_pixel = 250 - y * 25
                puntos.append((x_pixel, y_pixel))
            except Exception as e:
                print("Error en función:", funcion, e)


        for i in range(len(puntos)-1):
            x1, y1 = puntos[i]
            x2, y2 = puntos[i+1]
            canvas.create_line(x1, y1, x2, y2, fill=color)

ventana = tk.Tk()
ventana.title("Graficadora de Funciones")

tk.Label(ventana, text="f1(x):").pack()
entrada1 = tk.Entry(ventana, width=40)
entrada1.pack()

tk.Label(ventana, text="f2(x):").pack()
entrada2 = tk.Entry(ventana, width=40)
entrada2.pack()

boton = tk.Button(ventana, text="Graficar", command=graficar)
boton.pack()

canvas = tk.Canvas(ventana, width=500, height=500, bg="white")
canvas.pack()

ventana.mainloop()

