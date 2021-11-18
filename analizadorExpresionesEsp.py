# -----------------------------------------------------------------------------
# analizadorExpresionesEsp.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# Este archivo intepretará las expresiones escritas en los corchetes que señalan
# el tamaño de un arreglo, la ejecución regresará una pila con cada numero y
# operador que incluya la expresión para posteriormente resolverla. Este archivo
# será de utilidad solo para el análisis de las variables, ya sean globales o
# locales, ya que solo en esas reglas se usan este tipo "especial" de
# expresiones.
#
# Indice:
#
# -----------------------------------------------------------------------------

import analizadorArbol as aA
import solver as svr
import sys

tree = []

pila = []

def an_operadorAndconstant(hijo):
    global tree
    global pila
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    pila += [value]

def an_termOperationVar(termOperationVar):
    global tree
    hijos = aA.gimmeTheChildren(termOperationVar, tree)
    auctionVar = hijos[0]
    operador = hijos[1]
    termVar = hijos[2]
    an_auctionVar(auctionVar)
    an_operadorAndconstant(operador)
    an_termVar(termVar)

def an_expressionOperationVar(expressionOperationVar):
    global tree
    hijos = aA.gimmeTheChildren(expressionOperationVar, tree)
    termVar = hijos[0]
    operador = hijos[1]
    expressionVar = hijos[2]
    an_termVar(termVar)
    an_operadorAndconstant(operador)
    an_expressionVar(expressionVar)

def an_otherExpressionVar(otherExpressionVar):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(otherExpressionVar, tree)
    expressionVar = hijos[0]
    pila += ['(']
    an_expressionVar(expressionVar)
    pila += [')']

def an_auctionVar(auctionVar):
    global tree
    hijos = aA.gimmeTheChildren(auctionVar, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "constantVar"):
        constantVar = hijo
        hijos = aA.gimmeTheChildren(constantVar, tree)
        constant = hijos[0]
        an_operadorAndconstant(constant)
    else:
        print("No quiero parentesis en los corchetes")
        sys.exit()
        #otherExpressionVar = hijo
        #an_otherExpressionVar(otherExpressionVar)

def an_termVar(termVar):
    global tree
    hijos = aA.gimmeTheChildren(termVar, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "termOperationVar"):
        termOperationVar = hijo
        an_termOperationVar(termOperationVar)
    else:
        auctionVar = hijo
        an_auctionVar(auctionVar)

def an_expressionVar(expressionVar):
    global tree
    hijos = aA.gimmeTheChildren(expressionVar, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "expressionOperationVar"):
        expressionOperationVar = hijo
        an_expressionOperationVar(expressionOperationVar)
    else:
        termVar = hijo
        an_termVar(termVar)

def init(expressionVar, lista):
    global tree
    global pila
    tree = lista
    an_expressionVar(expressionVar)
    result = svr.init(pila)
    return result