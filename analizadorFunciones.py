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
import analizadorVarLocales as aVL
import analizadorParametros as aP
import analizadorBloqueFun as aBF
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
    parameters = aP.init(parameters, tree)
    aP.diccionarioParametros = {}
    if(value == "funcVer1"):
        funcVer1 = hijo
        diccionario = an_funcVer1(funcVer1)
        variablesLocales = diccionario["varLoc"]
        estatutos = diccionario["estatutos"]
        diccionario = {
            "parameters" : parameters,
            "varLoc" : variablesLocales,
            "estatutos" : estatutos
        }
        return diccionario
    else:
        funcVer2 = hijo
        diccionario = an_funcVer2(funcVer2)
        estatutos = diccionario["estatutos"]
        diccionario = {
            "parameters" : parameters,
            "estatutos" : estatutos
        }
        return diccionario

def an_variablesLoc(variablesLoc):
    global tree
    hijos = aA.gimmeTheChildren(variablesLoc, tree)
    varAuxLoc = hijos[0]
    dictVarLocales = aVL.init(varAuxLoc, tree)
    return dictVarLocales

def an_funcVer2(funcVer2):
    global tree
    hijos = aA.gimmeTheChildren(funcVer2, tree)
    block = hijos[0]
    estatutos = aBF.init(block, tree)
    return {
        "estatutos" : estatutos
    }

def an_funcVer1(funcVer1):
    global tree
    hijos = aA.gimmeTheChildren(funcVer1, tree)
    variablesLoc = hijos[0]
    block = hijos[1]
    variablesLocales = an_variablesLoc(variablesLoc)
    estatutos = aBF.init(block, tree)
    return {
        "varLoc" : variablesLocales,
        "estatutos" : estatutos
    }

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
        diccionario = an_withParameters(withParameters)
        parametros = diccionario["parameters"]
        variablesLocales = diccionario["varLoc"]
        estatutos = diccionario["estatutos"]
        if(tipo == "void"):
            obj = FunctionVoid(ID, parametros, variablesLocales, estatutos)
            dictFunciones[ID] = obj
        else:
            obj = FuncionReturn(ID, tipo, parametros, variablesLocales, estatutos)
            dictFunciones[ID] = obj
    elif(value == "funcVer1"):
        funcVer1 = hijo
        diccionario = an_funcVer1(funcVer1)
        variablesLocales = diccionario["varLoc"]
        estatutos = diccionario["estatutos"]
        parametros = "vacio"
        if(tipo == "void"):
            obj = FunctionVoid(ID, parametros, variablesLocales, estatutos)
            dictFunciones[ID] = obj
        else:
            obj = FuncionReturn(ID, tipo, parametros, variablesLocales, estatutos)
            dictFunciones[ID] = obj
    else:
        funcVer2 = hijo
        diccionario = an_funcVer2(funcVer2)
        estatutos = diccionario["estatutos"]
        variablesLocales = "vacio"
        parametros = "vacio"
        if(tipo == "void"):
            obj = FunctionVoid(ID, parametros, variablesLocales, estatutos)
            dictFunciones[ID] = obj
        else:
            obj = FuncionReturn(ID, tipo, parametros, variablesLocales, estatutos)
            dictFunciones[ID] = obj

def an_recursiveFunc(recursiveFunc):
    global tree
    hijos = aA.gimmeTheChildren(recursiveFunc, tree)
    funcAux = hijos[0]
    functions = hijos[1]
    an_funcAux(funcAux)
    an_functions(functions)

def an_functions(functions):
    global tree
    hijos = aA.gimmeTheChildren(functions, tree)
    hijo = hijos[0]
    label = aA.gimmeTheLabel(tree, hijo)
    value = aA.gimmeTheValue(label)
    if(value == "funcAux"):
        funcAux = hijo
        an_funcAux(funcAux)
    else:
        recursiveFunc = hijo
        an_recursiveFunc(recursiveFunc)

def printInfo(dictionary):
    keys = dictionary.keys()
    for i in keys:
        dictionary[i].imprimirDatos()

def init(functions, lista):
    global tree
    global dictFunciones
    tree = lista
    an_functions(functions)
    #printInfo(dictFunciones)
    return dictFunciones