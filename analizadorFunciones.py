# -----------------------------------------------------------------------------
# analizadorFunciones.py
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
from classFunciones import *

dictFunciones = {}
tree = []

def IDinDict(ID):
    global dictFunciones
    keys = dictFunciones.keys()
    try:
        if(ID in keys):
            return True
        else:
            return False
    except:
        return False

def an_label(hijo):
    global tree
    label = aA.gimmeTheLabel(tree, hijo)
    value  = aA.gimmeTheValue(label)
    return value

def an_withParameters(withParameters):
    global tree
    hijos = aA.gimmeTheChildren(withParameters, tree)
    parameters = hijos[0]
    hijo = hijos[1]
    value = an_label(hijo)
    if(value == "funcVer1"):
        funcVer1 = hijo
    else:
        funcVer2 = hijo

def an_funcAux(funcAux):
    global tree
    hijos = aA.gimmeTheChildren(funcAux, tree)
    typeFunction = hijos[0]
    ID = hijos[1]
    hijo = hijos[2]
    tipo = an_label(typeFunction)
    ID = an_label(ID)
    value = an_label(hijo)
    if(value == "withParameters"):
        withParameters = hijo
    elif(value == "funcVer1"):
        funcVer1 = hijo
    else:
        funcVer2 = hijo

def an_functions(functions):
    global tree
    hijos = aA.gimmeTheChildren(functions, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "funcAux"):
        funcAux = hijo
    else:
        recursiveFunc = hijo

def init(functions, lista):
    global tree
    global dictFunciones
    tree = lista
    return dictFunciones