# -----------------------------------------------------------------------------
# solver.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# Este archivo resuelve una expresión que específicamente busca obtener el tamaño
# de un arreglo
#
# Indice:
# 1. Análisis de expresión
#
# -----------------------------------------------------------------------------

# Función que resuelve una expresión
def resolve(first, operator, second):
    first = int(first)
    second = int(second)
    result = 0
    if(operator == '*'):
        result = first * second
    elif(operator == '/'):
        result = first / second
    elif(operator == '+'):
        result = first + second
    else:
        result = first - second
    return result

# Función que resuelve toda una pila (debe ser corta)
def fastResolve(pila):
    first = int(pila[0])
    operator = pila[1]
    second = int(pila[2])
    result = 0
    if(operator == '*'):
        result = first * second
    elif(operator == '/'):
        result = first / second
    elif(operator == '+'):
        result = first + second
    else:
        result = first - second
    return result

# Función que checa la prioridad de los operadores
def checkPriority(operator, nextOperator):
    if(operator == '*' or operator == '/'):
        return True
    else:
        if(nextOperator == '+' or nextOperator == '-'):
            return True
        else:
            return False

# Función que inicia la solución de una expresión
def solve(pila):
    if(len(pila) == 1):
        return int(pila[0])
    if(len(pila) == 3):
        result = fastResolve(pila)
        return result
    else:
        first = pila[0]
        operator = pila[1]
        second = pila[2]
        nextOperator = pila[3]
        third = pila[4]
        if(checkPriority(operator, nextOperator)):
            result = resolve(first, operator, second)
            pila.pop(0)
            pila.pop(0)
            pila[0] = result
            return solve(pila)
        else:
            result = resolve(second, nextOperator, third)
            pila.pop(2)
            pila.pop(2)
            pila[2] = result
            return solve(pila)

# Función inicial que recibe una pila representante de la expresión y regresa un valor entero
# que represeenta el tamaño de una arreglo
def init(pila):
    result = solve(pila)
    if(isinstance(result, int)):
        return result
    else:
        return "no es entero"