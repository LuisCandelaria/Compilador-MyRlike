# -----------------------------------------------------------------------------
# solver.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# Este archivo analiza el árbol semántico a partir del nodo que inicia el
# análisis de parámetros
#
# Indice:
# 1. Imports
# 2. Funciones auxiliares
# 3. Funciones analizadoras del árbol semántico
# 4. Función inicial
#
# -----------------------------------------------------------------------------

import analizadorArbol as aA
import sys
from classVariables import *

diccionarioParametros = {}
tree = {}

# Función que verifica si un ID se repite entre los parámetros
def IDinDict(ID):
    global diccionarioParametros
    keys = diccionarioParametros.keys()
    try:
        if(ID in keys):
            return True
        else:
            return False
    except:
        return False

# Función que regresa el valor de una etiqueta
def an_label(hijo):
    global tree
    label = aA.gimmeTheLabel(tree, hijo)
    value  = aA.gimmeTheValue(label)
    return value

# Función que crea variables a partir de una lista de IDs
def createVarFromList(IDs, tipo):
    global tree
    global diccionarioParametros
    for i in IDs:
        ID = i
        if(IDinDict(ID)):
            #ID already in dictionary
            print(ID + " already in dictionary")
            sys.exit()
        else:
            obj = VariableComun(ID, tipo)
            diccionarioParametros[ID] = obj

# Función que crea una variable
def createVar(ID, tipo):
    global tree
    global diccionarioParametros
    ID = ID[0]
    if(IDinDict(ID)):
        #ID already in dictionary
        print(ID + " already in dictionary")
        sys.exit()
    else:
        obj = VariableComun(ID, tipo)
        diccionarioParametros[ID] = obj

# Función que analiza la regla identLonely
def an_identLonely(identLonely):
    global tree
    hijos = aA.gimmeTheChildren(identLonely, tree)
    ID = hijos[0]
    label = aA.gimmeTheLabel(tree, ID)
    ID = aA.gimmeTheValue(label)
    return [ID]

# Función que analiza la regla identifierVar
def an_identifierVar(identifierVar):
    global tree
    hijos = aA.gimmeTheChildren(identifierVar, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "identLonely"):
        ID = an_identLonely(hijo)
    else:
        print("No quiero arreglos en los parametros")
        sys.exit()
    return ID

# Función que analiza la regla sameTypeParamRecursive
def an_sameTypeParamRecursive(sameTypeParamRecursive, tipo):
    global tree
    hijos = aA.gimmeTheChildren(sameTypeParamRecursive, tree)
    identifierVar = hijos[0]
    hijo = hijos[1]
    ID = an_identifierVar(identifierVar)
    createVar(ID, tipo)
    value = an_label(hijo)
    if(value == "sameTypeParamFinal"):
        sameTypeParamFinal = hijo
        an_sameTypeParamFinal(sameTypeParamFinal, tipo)
    elif(value == "sameTypeParamRecursive"):
        sameTypeParamRecursive = hijo
        an_sameTypeParamRecursive(sameTypeParamRecursive, tipo)
    else:
        parameters = hijo
        an_parameters(parameters)

# Función que analiza la regla sameTypeParamFinal
def an_sameTypeParamFinal(sameTypeParamFinal, tipo):
    global tree
    hijos = aA.gimmeTheChildren(sameTypeParamFinal, tree)
    identifierVar = hijos[0]
    ID = an_identifierVar(identifierVar)
    createVar(ID, tipo)

# Función que analiza la regla sameTypeParam
def an_sameTypeParam(sameTypeParam):
    global tree
    hijos = aA.gimmeTheChildren(sameTypeParam, tree)
    typeVar = hijos[0]
    identifierVar = hijos[1]
    hijo = hijos[2]
    tipo = an_label(typeVar)
    ID = an_identifierVar(identifierVar)
    createVar(ID, tipo)
    value = an_label(hijo)
    if(value == "sameTypeParamFinal"):
        sameTypeParamFinal = hijo
        an_sameTypeParamFinal(sameTypeParamFinal, tipo)
    else:
        sameTypeParamRecursive = hijo
        an_sameTypeParamRecursive(sameTypeParamRecursive, tipo)

# Función que analiza la regla newParam
def an_newParam(newParam):
    global tree
    hijos = aA.gimmeTheChildren(newParam, tree)
    typeVar = hijos[0]
    identifierVar = hijos[1]
    parameters = hijos[2]
    tipo = an_label(typeVar)
    ID = an_identifierVar(identifierVar)
    createVar(ID, tipo)
    an_parameters(parameters)

# Función que analiza la regla oneParam
def an_oneParam(oneParam):
    global tree
    hijos = aA.gimmeTheChildren(oneParam, tree)
    typeVar = hijos[0]
    identifierVar = hijos[1]
    tipo = an_label(typeVar)
    ID = an_identifierVar(identifierVar)
    createVar(ID, tipo)

# Función que analiza la regla paremeters
def an_parameters(parameters):
    global tree
    hijos = aA.gimmeTheChildren(parameters, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "oneParam"):
        oneParam = hijo
        an_oneParam(oneParam)
    elif(value == "sameTypeParam"):
        sameTypeParam = hijo
        an_sameTypeParam(sameTypeParam)
    else:
        newParam = hijo
        an_newParam(newParam)

# Función inicial que recibe el nodo parameters y regresa un diccionario de variables
def init(parameters, lista):
    global tree
    global diccionarioParametros
    tree = lista
    an_parameters(parameters)
    return diccionarioParametros