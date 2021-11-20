# -----------------------------------------------------------------------------
# analizadorLlamada.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
#
# Indice:
#
# -----------------------------------------------------------------------------

import analizadorArbol as aA
import analizadorExpresiones as aE
import sys

tree = []
pila = []

def an_label(hijo):
    global tree
    label = aA.gimmeTheLabel(tree, hijo)
    value  = aA.gimmeTheValue(label)
    return value

def an_callRecursive(callRecursive):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(callRecursive, tree)
    expression = hijos[0]
    callAux = hijos[1]
    stack = aE.init(expression, tree)
    pila += [stack]
    an_callAux(callAux)

def an_callAux(callAux):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(callAux, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "expression"):
        expression = hijo
        stack = aE.init(expression, tree)
        stack = stack
        pila += [stack]
    elif(value == "callRecursive"):
        callRecursive = hijo
        an_callRecursive(callRecursive)

def init(callAux, lista):
    global tree
    global pila
    tree = lista
    an_callAux(callAux)
    stack = pila
    pila = []
    return stack
