# -----------------------------------------------------------------------------
# analizadorVarGlobales.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# El objetivo de este archivo es obtener todas las variables globales del
# archivo de prueba, al recorrer el arbol de usarán las clases de classVariables.py
# y se anexarán al diccionario de variables globales.
#
# Indice:
#
# -----------------------------------------------------------------------------

from classVariables import *
import analizadorArbol as aA
import analizadorExpresionesEsp as expVar
import sys

dictVariablesGlobales = {}
tree = []

def an_identLonely(identLonely):
    global tree
    hijos = aA.gimmeTheChildren(identLonely, tree)
    ID = hijos[0]
    label = aA.gimmeTheLabel(tree, ID)
    ID = aA.gimmeTheValue(label)
    return [ID]

def an_identArrayVar(identArrayVar):
    global tree
    hijos = aA.gimmeTheChildren(identArrayVar, tree)
    ID = hijos[0]
    expressionVar = hijos[1]
    label = aA.gimmeTheLabel(tree, ID)
    ID = aA.gimmeTheValue(label)
    arr = [[ID, expressionVar]]
    return arr

def an_typeVar(typeVar):
    global tree
    label = aA.gimmeTheLabel(tree, typeVar)
    tipo = aA.gimmeTheValue(label)
    return tipo

def an_identifierVar(identifierVar):
    global tree
    hijos = aA.gimmeTheChildren(identifierVar, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "identLonely"):
        ID = an_identLonely(hijo)
    else:
        ID = an_identArrayVar(hijo)
    return ID

def an_oneVar(oneVar):
    global tree
    hijos = aA.gimmeTheChildren(oneVar, tree)
    typeVar = hijos[0]
    identifierVar = hijos[1]
    tipo = an_typeVar(typeVar)
    ID = an_identifierVar(identifierVar)
    createVar(ID, tipo)

def an_sameType(sameType):
    global tree
    hijos = aA.gimmeTheChildren(sameType, tree)
    typeVar = hijos[0]
    identifierVar = hijos[1]
    reglaSintaxis = hijos[2]
    tipo = an_typeVar(typeVar)
    ID = an_identifierVar(identifierVar)
    label = aA.gimmeTheLabel(tree, reglaSintaxis)
    value = aA.gimmeTheValue(label)
    if(value == "sameTypeFinal"):
        sameTypeFinal = reglaSintaxis
        IDFinal = an_sameTypeFinal(sameTypeFinal)
        arr = []
        arr += ID
        arr += IDFinal
    else:
        sameTypeRecursive = reglaSintaxis
        IDs = an_sameTypeRecursive(sameTypeRecursive)
        arr = []
        arr += ID
        arr += IDs
    createVarFromList(arr, tipo)

def an_sameTypeFinal(sameTypeFinal):
    global tree
    hijos = aA.gimmeTheChildren(sameTypeFinal, tree)
    identifierVar = hijos[0]
    ID = an_identifierVar(identifierVar)
    return ID

def an_sameTypeRecursive(sameTypeRecursive):
    global tree
    hijos = aA.gimmeTheChildren(sameTypeRecursive, tree)
    identifierVar = hijos[0]
    reglaSintaxis = hijos[1]
    ID = an_identifierVar(identifierVar)
    label = aA.gimmeTheLabel(tree, reglaSintaxis)
    value = aA.gimmeTheValue(label)
    if(value == "sameTypeRecursive"):
        sameTypeRecursive = reglaSintaxis
        IDs = an_sameTypeRecursive(sameTypeRecursive)
        arr = []
        arr += ID
        arr += IDs
        return arr
    elif(value == "sameTypeFinal"):
        sameTypeFinal = reglaSintaxis
        IDFinal = an_sameTypeFinal(sameTypeFinal)
        arr = []
        arr += ID
        arr += IDFinal
        return arr
    else:
        varAux = reglaSintaxis
        an_varAux(varAux)
        arr = ID
        return arr

def an_newType(newType):
    global tree
    hijos = aA.gimmeTheChildren(newType, tree)
    typeVar = hijos[0]
    identifierVar = hijos[1]
    varAux = hijos[2]
    tipo = an_typeVar(typeVar)
    ID = an_identifierVar(identifierVar)
    createVar(ID, tipo)
    an_varAux(varAux)

def createVarFromList(IDs, tipo):
    global tree
    global dictVariablesGlobales
    for i in IDs:
        if(isinstance(i, list)):
            #its an array
            expressionVar = i[1]
            ID = i[0]
            if(IDinDict(ID)):
                #ID already in dictionary
                print(ID + " already in dictionary")
                sys.exit()
            else:
                tamaño = expVar.init(expressionVar, tree)
                try:
                    obj = VariableArreglo(ID, tamaño, tipo)
                    dictVariablesGlobales[ID] = obj
                except:
                    print("El arreglo debe ser tamaño entero (VarGlobal)")
                    sys.exit()
        else:
            ID = i
            if(IDinDict(ID)):
                #ID already in dictionary
                print(ID + " already in dictionary")
                sys.exit()
            else:
                obj = VariableComun(ID, tipo)
                dictVariablesGlobales[ID] = obj

def createVar(ID, tipo):
    global tree
    global dictVariablesGlobales
    if(isinstance(ID, list)):
        #its an array
        ID = ID[0]
        expressionVar = ID[1]
        ID = ID[0]
        if(IDinDict(ID)):
            #ID already in dictionary
            print(ID + " already in dictionary")
            sys.exit()
        else:
            tamaño = expVar.init(expressionVar, tree)
            try:
                obj = VariableArreglo(ID, tamaño, tipo)
                dictVariablesGlobales[ID] = obj
            except:
                print("aqui")
                print("El arreglo debe ser tamaño entero (VarGlobal)")
                sys.exit()
    else:
        ID = ID[0]
        if(IDinDict(ID)):
            #ID already in dictionary
            print(ID + " already in dictionary")
            sys.exit()
        else:
            obj = VariableComun(ID, tipo)
            dictVariablesGlobales[ID] = obj

def IDinDict(ID):
    global dictVariablesGlobales
    keys = dictVariablesGlobales.keys()
    try:
        if(ID in keys):
            return True
        else:
            return False
    except:
        return False

def an_varAux(varAux):
    global tree
    hijos = aA.gimmeTheChildren(varAux, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "oneVar"):
        an_oneVar(hijo)
    elif(value == "sameType"):
        an_sameType(hijo)
    else:
        an_newType(hijo)

def an_vars(vars):
    global tree
    hijos = aA.gimmeTheChildren(vars, tree)
    varAux = hijos[0]
    an_varAux(varAux)

def printInfo(dictionary):
    keys = dictionary.keys()
    for i in keys:
        dictionary[i].imprimirDatos()

def init(vars, lista):
    global dictVariablesGlobales
    global tree
    tree = lista
    an_vars(vars)
    #printInfo(dictVariablesGlobales)
    return dictVariablesGlobales
