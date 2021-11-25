# -----------------------------------------------------------------------------
# analizadorExpressiones.py
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
import analizadorLlamada as aLl
import sys

tree = []
pila = []

def an_label(hijo):
    global tree
    label = aA.gimmeTheLabel(tree, hijo)
    value  = aA.gimmeTheValue(label)
    return value

def an_someConstant(constant):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(constant, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    pila += [value]

def an_identLonely(identLonely):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(identLonely, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    pila += [value]

def an_identArray(identArray):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(identArray, tree)
    ID = hijos[0]
    expression = hijos[1]
    ID = an_label(ID)
    stack = [ID, '-[-']
    pila += stack
    an_expression(expression)
    stack = '-]-'
    pila += [stack]

def an_identifier(identifier):
    global tree
    hijos = aA.gimmeTheChildren(identifier, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "identLonely"):
        identLonely = hijo
        an_identLonely(identLonely)
    else:
        identArray = hijo
        an_identArray(identArray)

def an_constant(constant):
    global tree
    hijos = aA.gimmeTheChildren(constant, tree)
    constant = hijos[0]
    an_someConstant(constant)

def an_functionCall(functionCall):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(functionCall, tree)
    ID = hijos[0]
    ID = an_label(ID)
    callAux = hijos[1]
    length = len(pila)
    auxPila = pila[0:length]
    pila = []
    expresiones = aLl.init(callAux, tree)
    stack = []
    for i in expresiones:
        stack += [i]
    funcStack = ['callFunction', ID] + stack
    era = ['era', ID]
    pila += [era] + [funcStack] + [auxPila]

def an_varianceFunc(varianceFunc):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(varianceFunc, tree)
    ID = hijos[0]
    ID = an_label(ID)
    pila += [['variance', ID]]

def an_modeFunc(modeFunc):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(modeFunc, tree)
    ID = hijos[0]
    ID = an_label(ID)
    pila += [['mode', ID]]

def an_averageFunc(averageFunc):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(averageFunc, tree)
    ID = hijos[0]
    ID = an_label(ID)
    pila += [['average', ID]]

def an_otherExpression(otherExpression):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(otherExpression, tree)
    expression = hijos[0]
    pila += ['(']
    an_expression(expression)
    pila += [')']

def an_auction(auction):
    global tree
    hijos = aA.gimmeTheChildren(auction, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "constant"):
        constant = hijo
        an_constant(constant)
    elif(value == "otherExpression"):
        otherExpression = hijo
        an_otherExpression(otherExpression)
    elif(value == "identifier"):
        identifier = hijo
        an_identifier(hijo)
    elif(value == "averageFunc"):
        averageFunc = hijo
        an_averageFunc(averageFunc)
    elif(value == "modeFunc"):
        modeFunc = hijo
        an_modeFunc(modeFunc)
    elif(value == "varianceFunc"):
        varianceFunc = hijo
        an_varianceFunc(varianceFunc)
    else:
        functionCall = hijo
        an_functionCall(functionCall)

def an_idiomsOperation(idiomsOperation):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(idiomsOperation, tree)
    auction = hijos[0]
    operador = hijos[1]
    idioms = hijos[2]
    operador = an_label(operador)
    an_auction(auction)
    pila += [operador]
    an_idioms(idioms)

def an_idioms(idioms):
    global tree
    hijos = aA.gimmeTheChildren(idioms, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "auction"):
        auction = hijo
        an_auction(auction)
    else:
        idiomsOperation = hijo
        an_idiomsOperation(idiomsOperation)

def an_factorOperation(factorOperation):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(factorOperation, tree)
    idioms = hijos[0]
    operador = hijos[1]
    factor = hijos[2]
    operador = an_label(operador)
    an_idioms(idioms)
    pila += [operador]
    an_factor(factor)

def an_factor(factor):
    global tree
    hijos = aA.gimmeTheChildren(factor, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "idioms"):
        idioms = hijo
        an_idioms(idioms)
    else:
        factorOperation = hijo
        an_factorOperation(factorOperation)

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

def init(expression, lista):
    global tree
    global pila
    tree = lista
    an_expression(expression)
    stack = pila
    pila = []
    return stack