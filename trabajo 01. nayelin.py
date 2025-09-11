import re

def analizar_expresion(expresion):
    # Buscar variables (letras o combinaciones de letras)
    variables = re.findall(r'[a-zA-Z]+', expresion)

    # Buscar operaciones (+, -, *, /, ^)
    operaciones = re.findall(r'[\+\-\*/\^]', expresion)

    return variables, operaciones

# Programa principal
def main():
    expresion = input("Ingresa una expresión matemática: ")
    variables, operaciones = analizar_expresion(expresion)

    print("Variables encontradas:", variables)
    print("Operaciones encontradas:", operaciones)

if __name__ == "__main__":
    main()
