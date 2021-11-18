# -----------------------------------------------------------------------------
# analizadorVarLocales.py
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
import analizadorExpresionesVar as aEV
from classVariables import *
import sys

dictVariablesLocales = {}
tree = []

def IDinDict(ID):
    global dictVariablesLocales
    keys = dictVariablesLocales.keys()
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

def createVarFromList(IDs, tipo):
    global tree
    global dictVariablesLocales
    for i in IDs:
        if(isinstance(i, list)):
            #its an array
            expression = i[1]
            ID = i[0]
            if(IDinDict(ID)):
                #ID already in dictionary
                print(ID + " already in dictionary")
                sys.exit()
            else:
                tamaño = aEV.init(expression, tree)
                try:
                    obj = VariableArreglo(ID, tamaño, tipo)
                    dictVariablesLocales[ID] = obj
                except:
                    print("El arreglo debe ser tamaño entero")
                    sys.exit()
        else:
            ID = i
            if(IDinDict(ID)):
                #ID already in dictionary
                print(ID + " already in dictionary")
                sys.exit()
            else:
                obj = VariableComun(ID, tipo)
                dictVariablesLocales[ID] = obj

def createVar(ID, tipo):
    global tree
    global dictVariablesLocales
    index = ID[0]
    if(isinstance(index, list)):
        #its an array
        ID = index[0]
        expression = index[1]
        if(IDinDict(ID)):
            #ID already in dictionary
            print(ID + " already in dictionary")
            sys.exit()
        else:
            tamaño = aEV.init(expression, tree)
            try:
                obj = VariableArreglo(ID, tamaño, tipo)
                dictVariablesLocales[ID] = obj
            except:
                print("El arreglo debe ser tamaño entero")
                sys.exit()
    else:
        ID = index
        if(IDinDict(ID)):
            #ID already in dictionary
            print(ID + " already in dictionary")
            sys.exit()
        else:
            obj = VariableComun(ID, tipo)
            dictVariablesLocales[ID] = obj

def an_identLonely(identLonely):
    global tree
    hijos = aA.gimmeTheChildren(identLonely, tree)
    ID = hijos[0]
    ID = an_label(ID)
    return [ID]

def an_identArray(identArray):
    global tree
    hijos = aA.gimmeTheChildren(identArray, tree)
    ID = hijos[0]
    expression = hijos[1]
    ID = an_label(ID)
    return [[ID, expression]]

def an_identifier(identifier):
    global tree
    hijos = aA.gimmeTheChildren(identifier, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "identLonely"):
        identLonely = hijo
        ID = an_identLonely(identLonely)
        return ID
    else:
        identArray = hijo
        ID = an_identArray(identArray)
        return ID

def an_oneVarLoc(oneVarLoc):
    global tree
    hijos = aA.gimmeTheChildren(oneVarLoc, tree)
    typeVar = hijos[0]
    tipo = an_label(typeVar)
    identifier = hijos[1]
    ID = an_identifier(identifier)
    createVar(ID, tipo)

def an_newTypeLoc(newTypeLoc):
    global tree
    hijos = aA.gimmeTheChildren(newTypeLoc, tree)
    typeVar = hijos[0]
    identifier = hijos[1]
    varAuxLoc = hijos[2]
    tipo = an_label(typeVar)
    ID = an_identifier(identifier)
    createVar(ID, tipo)
    an_varAuxLoc(varAuxLoc)

def an_sameTypeFinalLoc(sameTypeFinalLoc):
    global tree
    hijos = aA.gimmeTheChildren(sameTypeFinalLoc, tree)
    identifier = hijos[0]
    ID = an_identifier(identifier)
    return ID

def an_sameTypeRecursiveLoc(sameTypeRecursiveLoc):
    global tree
    hijos = aA.gimmeTheChildren(sameTypeRecursiveLoc, tree)
    identifier = hijos[0]
    hijo = hijos[1]
    ID = an_identifier(identifier)
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "sameTypeRecursiveLoc"):
        sameTypeRecursiveLoc = hijo
        return ID + an_sameTypeRecursiveLoc(sameTypeRecursiveLoc)
    elif(value == "sameTypeFinalLoc"):
        sameTypeFinalLoc = hijo
        return ID + an_sameTypeFinalLoc(sameTypeFinalLoc)
    else:
        varAuxLoc = hijo
        an_varAuxLoc(varAuxLoc)
        return ID

def an_sameTypeLoc(sameTypeLoc):
    global tree
    hijos = aA.gimmeTheChildren(sameTypeLoc, tree)
    typeVar = hijos[0]
    identifier = hijos[1]
    hijo = hijos[2]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    tipo = an_label(typeVar)
    ID = an_identifier(identifier)
    arr = ID
    if(value == "sameTypeFinalLoc"):
        sameTypeFinalLoc = hijo
        arr += an_sameTypeFinalLoc(sameTypeFinalLoc)
    else:
        sameTypeRecursiveLoc = hijo
        arr += an_sameTypeRecursiveLoc(sameTypeRecursiveLoc)
    createVarFromList(arr, tipo)

def an_varAuxLoc(varAuxLoc):
    global tree
    hijos = aA.gimmeTheChildren(varAuxLoc, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "oneVarLoc"):
        oneVarLoc = hijo
        an_oneVarLoc(oneVarLoc)
    elif(value == "sameTypeLoc"):
        sameTypeLoc = hijo
        an_sameTypeLoc(sameTypeLoc)
    else:
        newTypeLoc = hijo
        an_newTypeLoc(newTypeLoc)

def init(varAuxLoc, lista):
    global tree
    global dictVariablesLocales
    tree = lista
    an_varAuxLoc(varAuxLoc)
    return dictVariablesLocales