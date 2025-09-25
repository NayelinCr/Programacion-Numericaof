class Restriccion:
    def __init__(self, expresion):
        """
        La expresión debe ser una función lambda con x,y.
        Ejemplo: Restriccion(lambda x,y: x + y <= 15)
        """
        self.expresion = expresion

    def cumple(self, x, y):
        return self.expresion(x, y)


class FuncionLineal:
    def __init__(self, m, b, simbolo="*"):
        self.m = m
        self.b = b
        self.simbolo = simbolo

    def evaluar(self, x):
        return round(self.m * x + self.b)


class PlanoCartesiano:
    def __init__(self, xmin=-1, xmax=20, ymin=-1, ymax=20):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def graficar(self, funciones, restricciones=[]):
        for y in range(self.ymax, self.ymin - 1, -1):
            linea = ""
            for x in range(self.xmin, self.xmax + 1):
                simbolo = " "
                
              
                if restricciones and all(r.cumple(x, y) for r in restricciones):
                    simbolo = "."

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
    """
    Convierte 'y=-x+15' o 'y=2x+3' en (m,b).
    """
    expr = expr.replace(" ", "").lower()
    if expr.startswith("y="):
        expr = expr[2:]

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

funciones = []
restricciones = []

n = int(input("¿Cuántas funciones quieres graficar? "))
for i in range(n):
    f_str = input(f"Ingrese función {i+1} en forma y=mx+b: ")
    m, b = parsear_funcion(f_str)
    funciones.append(FuncionLineal(m, b, simbolo="*"))

m = int(input("¿Cuántas restricciones quieres ingresar? "))
print("Usa 'x' y 'y'. Ejemplo: x+y<=15, x>=5, y>=0")
for i in range(m):
    expr = input(f"Ingrese restricción {i+1}: ")
    try:
        restricciones.append(Restriccion(eval(f"lambda x,y: {expr}")))
    except:
        print(f"Restricción inválida: {expr}. Usa operadores como <=, >=, ==, <, >")
        exit()

plano = PlanoCartesiano()
plano.graficar(funciones, restricciones)
