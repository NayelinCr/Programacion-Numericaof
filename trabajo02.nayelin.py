import re

class FuncionLineal:
    def __init__(self, m, b, simbolo="*"):
        self.m = m
        self.b = b
        self.simbolo = simbolo

    def evaluar(self, x):
        return round(self.m * x + self.b)


class PlanoCartesiano:
    def __init__(self, xmin=-10, xmax=10, ymin=-10, ymax=10):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def graficar(self, funciones):
        for y in range(self.ymax, self.ymin - 1, -1):
            linea = ""
            for x in range(self.xmin, self.xmax + 1):
                simbolo = " "
                for f in funciones:
                    if f.evaluar(x) == y:
                        simbolo = f.simbolo
                if x == 0 and y == 0:
                    simbolo = "O"
                elif x == 0 and simbolo == " ":
                    simbolo = "|"
                elif y == 0 and simbolo == " ":
                    simbolo = "-"
                linea += simbolo
            print(linea)
def parsear_funcion(expr):
    expr = expr.replace(" ", "")  

   
    if "x" in expr:
        partes = expr.split("x")
        m_str = partes[0]
        b_str = partes[1] if len(partes) > 1 else "0"

        if m_str in ["", "+"]:
            m = 1
        elif m_str == "-":
            m = -1
        else:
            m = float(m_str)

        b = float(b_str) if b_str != "" else 0
    else:
        m = 0
        b = float(expr)

    return m, b

funciones_texto = []
for i in range(2):  
    f_str = input(f"Ingrese función {i+1} (ejemplo 2x+5, -x+3): ")
    funciones_texto.append(f_str)

funciones = []
simbolos = ["*", "+"]
for i, f_str in enumerate(funciones_texto):
    m, b = parsear_funcion(f_str)
    funciones.append(FuncionLineal(m, b, simbolos[i]))

plano = PlanoCartesiano()
plano.graficar(funciones)

