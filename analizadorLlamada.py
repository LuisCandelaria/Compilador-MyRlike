# -----------------------------------------------------------------------------
# analizadorLlamada.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# Este archivo sirve como auxiliar si en una expresión se topan con una llamada
# a una función, su propósito es bajar de nodo en nodo hasta llegar a una constante
#
# Indice:
# 1. Imports
# 2. Funciones analizadoras del árbol semántico
# 3. Función inicial
#
# -----------------------------------------------------------------------------

import analizadorArbol as aA
import analizadorExpresiones as aE
import sys

tree = []
pila = []

# Función que regresa el valor de una etiqueta
def an_label(hijo):
    global tree
    label = aA.gimmeTheLabel(tree, hijo)
    value  = aA.gimmeTheValue(label)
    return value

# Función que analiza la regla callRecursive
def an_callRecursive(callRecursive):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(callRecursive, tree)
    expression = hijos[0]
    callAux = hijos[1]
    stack = aE.init(expression, tree)
    aE.pila = []
    pila += [stack]
    an_callAux(callAux)

# Función que analiza la regla callAux
def an_callAux(callAux):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(callAux, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "expression"):
        expression = hijo
        stack = aE.init(expression, tree)
        aE.pila = []
        stack = stack
        pila += [stack]
    elif(value == "callRecursive"):
        callRecursive = hijo
        an_callRecursive(callRecursive)

# Función inicial que recibe el nodo callAux y regresa una pila que contiene la expresión (llamada a una función)
def init(callAux, lista):
    global tree
    global pila
    tree = lista
    an_callAux(callAux)
    stack = pila
    pila = []
    return stack
