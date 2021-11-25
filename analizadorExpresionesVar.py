# -----------------------------------------------------------------------------
# analizadorExpresionesVar.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# Este archivo analiza las expresiones dentro de los corchetes de una variable local
# o parmámetro. Luego se tomó en cuenta que no se aceptarán arreglos como parámetros
# de una función.
#
# Indice:
# 1. Imports
# 2. Analizador del árbol semántico
# 3. Función inicial
#
# -----------------------------------------------------------------------------

import analizadorArbol as aA
import solver as svr
import sys

tree = []

pila = []

# Función que regresa el valor de una etiqueta
def an_label(hijo):
    global tree
    label = aA.gimmeTheLabel(tree, hijo)
    value  = aA.gimmeTheValue(label)
    return value

# Función que analiza la regla de la constante entera
def an_someInt(someInt):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(someInt, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    pila += [value]

# Función que analiza la regla identLonely
def an_identLonely(identLonely):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(identLonely, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    pila += [value]

# Función que analiza la regla identifier
def an_identifier(identifier):
    global tree
    hijos = aA.gimmeTheChildren(identifier, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "identLonely"):
        identLonely = hijo
    else:
        print("No quiero arreglos en el tamaño")
        sys.exit()

# Función que analiza la regla constant
def an_constant(constant):
    global tree
    hijos = aA.gimmeTheChildren(constant, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "someInt"):
        someInt = hijo
        an_someInt(someInt)
    else:
        print("Debe ser entero")
        sys.exit()

# Función que analiza la regla auction
def an_auction(auction):
    global tree
    hijos = aA.gimmeTheChildren(auction, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "constant"):
        constant = hijo
        an_constant(constant)
    elif(value == "otherExpression"):
        print("No quiero parentesis")
        sys.exit()
    elif(value == "identifier"):
        print("No quiero IDs")
        sys.exit()
    else:
        print("No quiero otra cosa que no sea entero")
        sys.exit()

# Función que analiza la regla idioms
def an_idioms(idioms):
    global tree
    hijos = aA.gimmeTheChildren(idioms, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "auction"):
        auction = hijo
        an_auction(auction)
    else:
        print("El tamaño debe ser entero")
        sys.exit()

# Función que analiza la regla factor
def an_factor(factor):
    global tree
    hijos = aA.gimmeTheChildren(factor, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "idioms"):
        idioms = hijo
        an_idioms(idioms)
    else:
        print("El tamaño debe ser entero")
        sys.exit()

# Función que analiza la regla termOperation
def an_termOperation(termOperation):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(termOperation, tree)
    factor = hijos[0]
    operador = hijos[1]
    term = hijos[2]
    operador = an_label(operador)
    an_factor(factor)
    pila += [operador]
    an_term(term)

# Función que analiza la regla term
def an_term(term):
    global tree
    hijos = aA.gimmeTheChildren(term, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "factor"):
        factor = hijo
        an_factor(factor)
    else:
        termOperation = hijo
        an_termOperation(termOperation)

# Función que analiza la regla expressionOperation
def an_expressionOperation(expressionOperation):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(expressionOperation, tree)
    term = hijos[0]
    operador = hijos[1]
    expression = hijos[2]
    operador = an_label(operador)
    an_term(term)
    pila += [operador]
    an_expression(expression)

# Función que analiza la regla expression
def an_expression(expression):
    global tree
    hijos = aA.gimmeTheChildren(expression, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "term"):
        term = hijo
        an_term(term)
    else:
        expressionOperation = hijo
        an_expressionOperation(expressionOperation)

# Función inicial que recibe el nodo expression y regresa la solución de la expresión
# llamando al archivo solver
def init(expression, lista):
    global tree
    global pila
    tree = lista
    an_expression(expression)
    result = svr.init(pila)
    return result